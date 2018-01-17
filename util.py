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


class pins(object):

  def __init__(self):
    self.units = []

  def add_unit(self, u):
    self.units.append(u)

class unit(object):

  def __init__(self):
    self.groups = []

  def add_group(self, g):
    self.groups.append(g)

class group(object):

  def __init__(self, align):
    assert align in ('L','R','T','B'), 'bad alignment %s' % align
    self.align = align
    self.pins = []

  def add_pin(self, p):
    self.pins.append(p)

class pin(object):

  def __init__(self, name, pin_type):
    assert pin_type in pin_types.keys(), 'bad pin type %s' % pin_type
    self.name = name
    self.ptype = pin_type

#-----------------------------------------------------------------------------

class component(object):

  def __init__(self, name, descr):
    self.name = name
    self.descr = descr
    self.tags = [name,]

  def add_tags(self, tags):
    """add tags to the component"""
    self.tags.extend(tags)
    return self

  def set_url(self, url):
    self.url = url
    return self

  def lib(self, fp=None):
    """return the kicad schematic symbol string"""
    return ''

  def dcm_str(self):
    """return the kicad device documentation string"""
    dcm = kicad.dcm_component(self.name, self.descr)
    dcm.add_keywords(self.tags)
    dcm.add_url(self.url)
    return str(dcm)

  def mod_str(self, fp=None):
    """return the kicad pcb footprint string"""
    return ''

#-----------------------------------------------------------------------------
