#-----------------------------------------------------------------------------
"""

Utility Functions

"""
#-----------------------------------------------------------------------------

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

  def __init__(self, name):
    self.name = name
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

# map a user friendly string onto the kicad pin type
pin_types = {
  'in': 'I', # Input
  'out': 'O', # Output
  'inout': 'B', # Bidirectional
  'tristate': 'T', # Tristate
  'passive': 'P', # Passive
  'open_collector': 'C', # Open Collector
  'open_emitter': 'E', # Open Emitter
  'nc': 'N', # Non-connected
  'unspecified': 'U', # Unspecified
  'power_in': 'W', # Power input
  'power_out': 'w', # Power output
}

class pin(object):
  """single component pin"""

  def __init__(self, name, pin_type, side=None, group=0, unit=0):
    assert pin_type in pin_types.keys(), 'bad pin type %s' % pin_type
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

#-----------------------------------------------------------------------------

pin_length = 200 # length of schematic pin (mils)
pin_corner_space = 50 # space on corner of the symbols (mils)
pin_delta_space = 100 # pin to pin spacing (mils)
pin_group_space = 100 # space btween pin groups (mils)

class pinset(object):
  """combined component/footprint pin set"""

  def __init__(self, component, footprint):
    # do a join between the component pin names and the footprint pin numbers
    self.pins = []
    for pin_name, pin_numbers in footprint.name2number.iteritems():
      for pin_number in pin_numbers:
        self.pins.append((pin_number, component.name2pin[pin_name]))

  def num_pins(self, side):
    """return the number of pins on a side"""
    return len([True for (_, p) in self.pins if p.side == side])

  def on_side(self, side):
    """return the pins on a side sorted by the group number"""
    pins = [(n, p) for (n, p) in self.pins if p.side == side]
    # sort by group
    pins.sort(key = lambda (n, p) : p.group)
    return pins

  def num_groups(self, side):
    """return the number of pin groups on a side"""
    groups = {}
    for (_ , p) in self.pins:
      if p.side == side:      
        groups[p.group] = True
    return len(groups.keys())

  def len_side(self, side):
    """return a side length large enough for the pins on this side"""
    l = 2 * pin_corner_space
    l += (self.num_pins(side) - 1) * pin_delta_space
    l += (self.num_groups(side) - 1) * pin_group_space
    return l

  def rect_size(self):
    """return the size of a rectangular symbol large enough for all the pins"""
    w = max(self.len_side('T'), self.len_side('B'))
    h = max(self.len_side('L'), self.len_side('R'))
    return (w, h)

#-----------------------------------------------------------------------------

class component(object):

  def __init__(self, name, descr):
    self.name = name
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
    print pins.rect_size()
    pins.on_side('T')
    pins.on_side('B')
    pins.on_side('L')
    pins.on_side('R')
    return ''

  def dcm_str(self):
    """return the kicad device documentation"""
    dcm = kicad.dcm_component(self.name, self.descr)
    dcm.add_keywords(self.tags)
    dcm.add_url(self.url)
    return str(dcm)

  def mod_str(self, fp=None):
    """return the kicad pcb footprint"""
    return ''

#-----------------------------------------------------------------------------
