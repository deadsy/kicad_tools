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
