#-----------------------------------------------------------------------------
"""

Utility Functions

"""
#-----------------------------------------------------------------------------

import kicad


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
  for i,v in enumerate(pins):
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
    self.pin_map = None

  def set_pin_map(self, pin_map):
    """set the pin name to pin number mapping"""
    # each pin number must be unique
    pin_numbers = {}
    for x in pin_map.itervalues():
      print x


#-----------------------------------------------------------------------------

class pin(object):

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
      assert side in ('T','L','R','B'), 'bad symbol side %s' % side
    self.side = side


#-----------------------------------------------------------------------------

class component(object):

  def __init__(self, name, descr):
    self.name = name
    self.descr = descr
    self.tags = [name,]
    self.pins = []
    self.footprints = []

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
    self.pins.extend(pins)

  def add_footprint(self, footprint):
    """add a footprint"""
    self.footprints.append(footprint)

  def lib(self, fp=None):
    """return the kicad schematic symbol"""
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
