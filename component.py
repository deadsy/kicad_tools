#-----------------------------------------------------------------------------
"""

Component Functions

"""
#-----------------------------------------------------------------------------

import string
import kicad

#-----------------------------------------------------------------------------

class pin(object):
  """single component pin"""

  def __init__(self, name, pin_type, side=None, group=0, unit=0):
    self.name = name
    self.pin_type = pin_type
    self.group = group # pin grouping on schematic symbol
    self.unit = unit # symbol unit E.g. 0..5 for a hex inverter
    # work out the side of the symbol the pin is on
    if side is None:
      if self.pin_type == 'out':
        side = 'R'
      elif pin_type == 'in':
        side = 'L'
      elif self.name in ('VCC', 'VDD', '3V', '5V'):
        side = 'T'
      elif self.name in ('VEE', 'VSS', 'GND',):
        side = 'B'
      else:
        # default to right hand side
        side = 'R'
    else:
      assert side in ('T', 'L', 'R', 'B'), 'bad symbol side %s' % side
    self.side = side

  def sort_key(self):
    """return a sort key, sort pins by group and then lexicographically by name"""
    tmp = ''
    state = None
    x = [self.group,]
    for c in self.name:
      if c in string.digits:
        if state == 'str':
          x.append(tmp)
          tmp = c
        else:
          tmp = tmp + c
        state = 'int'
      else:
        if state == 'int':
          x.append(int(tmp))
          tmp = string.lower(c) + c
        else:
          tmp = tmp + string.lower(c) + c
        state = 'str'
    # append the last term
    if state == 'int':
      x.append(int(tmp))
    else:
      x.append(tmp)
    return x

def rename_pin(pins, old_name, new_name):
  """rename a pin in the pin list"""
  for p in pins:
    if p.name == old_name:
      p.name = new_name
      return

def append_pin_name(pins, name, more_names):
  """append more names to a named pin"""
  for p in pins:
    if p.name == name:
      p.name = '%s/%s' % (name, more_names)
      return
  assert False, 'pin name %s not found' % name

def remove_pin(pins, name):
  """remove a named pin from the list"""
  for (i,p) in enumerate(pins):
    if p.name == name:
      del pins[i]
      return
  assert False, 'pin name %s not found' % name

#-----------------------------------------------------------------------------

pin_length = 200 # length of schematic pin (mils)
pin_corner_space = 100 # space on corner of the symbols (mils)
pin_delta_space = 100 # pin to pin spacing (mils)
pin_group_space = 100 # space btween pin groups (mils)
pin_text_size = 50 # size of pin text

class pinset(object):
  """combined component/footprint pin set"""

  def __init__(self, c, fp_map):
    # do a join between the component pin names and the footprint pin numbers
    self.pins = []
    for pin_name, pin_numbers in fp_map.name2number.iteritems():
      for pin_number in pin_numbers:
        self.pins.append((pin_number, c.name2pin[pin_name]))

  def num_pins(self, side):
    """return the number of pins on a side"""
    return len([True for (_, p) in self.pins if p.side == side])

  def on_side(self, side):
    """return the pins on a side sorted by the group number"""
    pins = [(n, p) for (n, p) in self.pins if p.side == side]
    # sort by group
    pins.sort(key=lambda (n, p): p.sort_key())
    return pins

  def name_size(self, side):
    """return the maximum size of the pin name text on this side"""
    x = 0
    for (_, p) in self.pins:
      if p.side == side:
        x = max(x, (len(p.name) + 2) * pin_text_size)
    return x

  def pin_size(self, side):
    """return a side length large enough for the pins on this side"""
    l = (self.num_pins(side) - 1) * pin_delta_space
    l += (self.num_groups(side) - 1) * pin_group_space
    return l

  def num_groups(self, side):
    """return the number of pin groups on a side"""
    groups = {}
    for (_, p) in self.pins:
      if p.side == side:
        groups[p.group] = True
    return len(groups.keys())

  def rect_size(self):
    """return the size of a rectangular symbol large enough for all the pins"""
    # consider the number of pins
    wp = max(self.pin_size('T'), self.pin_size('B'))
    hp = max(self.pin_size('L'), self.pin_size('R'))
    # extra space for the corners
    wp += (2 * pin_corner_space)
    hp += (2 * pin_corner_space)
    # consider the pin names
    wn = self.name_size('L') + self.name_size('R')
    hn = self.name_size('T') + self.name_size('B')
    # extra space for the middle
    wn += 2 * pin_text_size
    hn += 2 * pin_text_size
    w = max(wp, wn)
    h = max(hp, hn)
    # round up to 200 mil increments
    w = w + (200 - (w % 200))
    h = h + (200 - (h % 200))
    return (w, h)

#-----------------------------------------------------------------------------

class footprint_map(object):

  def __init__(self, pin_map):
    """setup a pin name to pin number mapping for a footprint"""
    # each pin number must be unique
    self.name2number = {}
    all_numbers = {}
    for name, numbers in pin_map.iteritems():
      numbers = [str(x) for x in numbers]
      # check for duplicates
      for number in numbers:
        assert all_numbers.has_key(number) is False, 'duplicate pin number %s' % number
        all_numbers[number] = True
      self.name2number[name] = numbers

  def get_pin_numbers(self, pin_name):
    """return the pin numbers associated with a pin name"""
    return self.name2number[pin_name]

  def get_pin_names(self):
    """return the pin names in the footprint"""
    return list(set(self.name2number.keys()))

#-----------------------------------------------------------------------------

class component(object):
  """an electronic device/module"""

  def __init__(self, name, ref, descr):
    self.name = name
    self.ref = ref
    self.descr = descr
    self.url = None
    self.tags = [name,]
    self.footprints = []
    self.name2pin = {}

  def add_tags(self, tags):
    """add keyword/tags for documentation"""
    self.tags.extend(tags)
    return self

  def set_url(self, url):
    """set a reference url for documentation"""
    self.url = url
    return self

  def add_pins(self, pins):
    """add a set of pins"""
    for p in pins:
      assert self.name2pin.has_key(p.name) is False, 'duplicate pin name %s in component %s' % (p.name, self.name)
      self.name2pin[p.name] = p

  def add_footprint(self, fp_name, pin_map):
    """add a footprint"""
    self.footprints.append((fp_name, pin_map))

  def component_str(self, fp_name, fp_lib, pins):
    """return the kicad schematic symbol"""
    # work out the symbol rectangle
    (w, h) = pins.rect_size()
    # create the component
    c_name = ('%s_%s' % (self.name, fp_name), self.name)[fp_name == self.name]
    lib = kicad.lib_component(c_name, self.ref)
    # put the reference at the top right
    lib.get_text(0).set_bl().ofs_xy(-w/2, h/2 + 50)
    # put the name in the lower left
    lib.get_text(1).set_tl().ofs_xy(-w/2, -h/2 - 50)
    # add the footprint
    lib.add_footprint(fp_lib, fp_name)
    # create the unit
    u = kicad.lib_unit()
    u.add_shape(kicad.lib_rect(w, h))
    # top pins
    x0 = -pins.pin_size('T')/2
    y0 = h/2 + pin_length
    for i, v in enumerate(pins.on_side('T')):
      (pin_number, pin) = v
      x = x0 + (i * pin_delta_space) + (pin.group * pin_group_space)
      (pin_number, pin) = v
      p = kicad.lib_pin(pin_number, pin.name)
      p.ofs_xy(x, y0)
      p.set_orientation('D')
      p.set_type(pin.pin_type)
      p.set_length(pin_length)
      u.add_pin(p)
    # bottom pins
    x0 = -pins.pin_size('B')/2
    y0 = -h/2 - pin_length
    for i, v in enumerate(pins.on_side('B')):
      (pin_number, pin) = v
      p = kicad.lib_pin(pin_number, pin.name)
      x = x0 + (i * pin_delta_space) + (pin.group * pin_group_space)
      p.ofs_xy(x, y0)
      p.set_orientation('U')
      p.set_type(pin.pin_type)
      p.set_length(pin_length)
      u.add_pin(p)
    # left pins
    x0 = -w/2 - pin_length
    y0 = h/2 - pin_corner_space
    for i, v in enumerate(pins.on_side('L')):
      (pin_number, pin) = v
      p = kicad.lib_pin(pin_number, pin.name)
      y = y0 - (i * pin_delta_space) - (pin.group * pin_group_space)
      p.ofs_xy(x0, y)
      p.set_orientation('R')
      p.set_type(pin.pin_type)
      p.set_length(pin_length)
      u.add_pin(p)
    # right pins
    x0 = w/2 + pin_length
    y0 = h/2 - pin_corner_space
    for i, v in enumerate(pins.on_side('R')):
      (pin_number, pin) = v
      p = kicad.lib_pin(pin_number, pin.name)
      y = y0 - (i * pin_delta_space) - (pin.group * pin_group_space)
      p.ofs_xy(x0, y)
      p.set_orientation('L')
      p.set_type(pin.pin_type)
      p.set_length(pin_length)
      u.add_pin(p)
    # add the unit
    lib.add_unit(u)
    return str(lib)

  def lib_str(self, fp_lib):
    """generate the schematic symbol for each footprint in this component"""
    s = []
    for (fp_name, pin_map) in self.footprints:
      # check that all the names in the footprint map are in the component
      for name in pin_map.iterkeys():
        assert self.name2pin.has_key(name) is True, 'footprint %s pin name %s not found in component %s' % (fp_name, name, self.name)
      fp_map = footprint_map(pin_map)
      s.append(self.component_str(fp_name, fp_lib, pinset(self, fp_map)))
    return '\n'.join(s)

  def dcm_str(self):
    """return the kicad device documentation"""
    s = []
    for (fp_name, _) in self.footprints:
      c_name = ('%s_%s' % (self.name, fp_name), self.name)[fp_name == self.name]
      dcm = kicad.dcm_component(c_name, self.descr)
      dcm.add_keywords(self.tags)
      dcm.add_url(self.url)
      s.append(str(dcm))
    return '\n'.join(s)

#-----------------------------------------------------------------------------

class component_database(object):

  def __init__(self):
    self.components = {}

  def lookup(self, name):
    """lookup a component by name"""
    assert self.components.has_key(name), 'component %s not found' % name
    return self.components[name]

  def values(self):
    return self.components.values()

  def add(self, c):
    """add a component to the database"""
    assert self.components.has_key(c.name) is False, 'component database already has %s' % c.name
    self.components[c.name] = c

db = component_database()

#-----------------------------------------------------------------------------
