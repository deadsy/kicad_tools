#-----------------------------------------------------------------------------
"""

Utility Functions

"""
#-----------------------------------------------------------------------------

import string
import kicad

#-----------------------------------------------------------------------------

def build_symbol(name, reference, pins, w):
  """return a component symbol - single unit"""
  # work out the rectangle dimensions
  p_len = 200
  p_delta = 100
  r_extra = 100
  npins = (len(pins) & ~1) + 1
  h = ((npins - 1) * p_delta) + (2 * r_extra)
  # create the component
  lib = kicad.lib_component(name, reference)
  # put the reference at the top right
  lib.get_text(0).set_bl().ofs_xy(-w/2, h/2 + 50)
  # put the name in the lower left
  lib.get_text(1).set_tl().ofs_xy(-w/2, -h/2 - 50)
  # create the unit
  u = kicad.lib_unit()
  u.add_shape(kicad.lib_rect(w, h))
  # add the pins
  for i, v in enumerate(pins):
    (pin_number, pin_name, pin_type) = v
    p = kicad.lib_pin(pin_number, pin_name)
    x = w/2 + p_len
    y = h/2 - r_extra - (i * p_delta)
    p.ofs_xy(x, y)
    p.set_orientation('L')
    p.set_type(pin_type)
    p.set_length(p_len)
    u.add_pin(p)
  # add the unit
  lib.add_unit(u)
  return lib

#-----------------------------------------------------------------------------

class footprint(object):

  def __init__(self, name, lib):
    self.name = name
    self.lib = lib
    self.name2number = {}

  def get_pin_numbers(self, pin_name):
    """return the pin numbers associated with a pin name"""
    return self.name2number[pin_name]

  def get_pin_names(self):
    """return the pin names in the footprint"""
    return list(set(self.name2number.keys()))

  def set_pin_map(self, pin_map):
    """set the pin name to pin number mapping"""
    # each pin number must be unique
    all_numbers = {}
    for name, numbers in pin_map.iteritems():
      numbers = [str(x) for x in numbers]
      # check for duplicates
      for number in numbers:
        assert all_numbers.has_key(number) is False, 'duplicate pin number %s' % number
        all_numbers[number] = True
      self.name2number[name] = numbers

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
      elif self.name in ('VCC',):
        side = 'T'
      elif self.name in ('GND',):
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

#-----------------------------------------------------------------------------

pin_length = 200 # length of schematic pin (mils)
pin_corner_space = 100 # space on corner of the symbols (mils)
pin_delta_space = 100 # pin to pin spacing (mils)
pin_group_space = 100 # space btween pin groups (mils)
pin_text_size = 50 # size of pin text

class pinset(object):
  """combined component/footprint pin set"""

  def __init__(self, c, fp):
    # do a join between the component pin names and the footprint pin numbers
    self.pins = []
    for pin_name, pin_numbers in fp.name2number.iteritems():
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

class component(object):
  """an electronic component/module"""

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

  def add_footprint(self, fp):
    """add a footprint"""
    # check that all the names in the footprint map are in the component
    for name in fp.get_pin_names():
      assert self.name2pin.has_key(name) is True, 'footprint pin name %s (%s) not found in component %s' % (name, fp.name, self.name)
    self.footprints.append(fp)

  def footprint_lookup(self, fp_name):
    """lookup a footprint by name"""
    assert len(self.footprints) != 0, 'no footprints defined'
    if fp_name is None:
      return self.footprints[0]
    for fp in self.footprints:
      if fp.name == fp_name:
        return fp
    assert False, 'no footprint "%s" found for %s' % (fp_name, self.name)

  def lib_str(self, fp_name=None):
    """return the kicad schematic symbol"""
    fp = self.footprint_lookup(fp_name)
    pins = pinset(self, fp)
    # work out the symbol rectangle
    (w, h) = pins.rect_size()
    # create the component
    lib = kicad.lib_component(self.name, self.ref)
    # put the reference at the top right
    lib.get_text(0).set_bl().ofs_xy(-w/2, h/2 + 50)
    # put the name in the lower left
    lib.get_text(1).set_tl().ofs_xy(-w/2, -h/2 - 50)
    # add the footprint
    lib.add_footprint(fp.lib, fp.name)
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

  def dcm_str(self):
    """return the kicad device documentation"""
    dcm = kicad.dcm_component(self.name, self.descr)
    dcm.add_keywords(self.tags)
    dcm.add_url(self.url)
    return str(dcm)

  def mod_str(self, fp_name=None):
    """return the kicad pcb footprint"""
    return ''

#-----------------------------------------------------------------------------
