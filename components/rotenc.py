#-----------------------------------------------------------------------------
"""

com-10982 - Rotary Encoder - Illuminated (RGB)
https://cdn.sparkfun.com/datasheets/Components/Switches/EC12PLRGBSDVBF-D-25K-24-24C-6108-6H.pdf

"""
#-----------------------------------------------------------------------------

import kicad
import footprint
import component

#-----------------------------------------------------------------------------

name = 'RE10982'
descr = 'Rotary Encoder Illuminated (RGB)'
tags = (name, 'rotary', 'encoder', 'switch',)
url = 'https://www.sparkfun.com/products/10982'

#-----------------------------------------------------------------------------

dev = component.component(name, 'S', descr)
dev.add_tags = (tags)
dev.set_url(url)

pins = (
  component.pin('PH_A', 'out'),
  component.pin('PH_Com', 'out'),
  component.pin('PH_B', 'out'),
  component.pin('LED_R', 'in'),
  component.pin('LED_G', 'in'),
  component.pin('PB', 'out'),
  component.pin('LED_B', 'in'),
  component.pin('Com', 'power_in'),
)

dev.add_pins(pins)
component.db.add(dev)

#-----------------------------------------------------------------------------

pin_map = {
  'PH_A': ('A',),
  'PH_Com': ('C',),
  'PH_B': ('B',),
  'LED_R': (1,),
  'LED_G': (2,),
  'PB': (3,),
  'LED_B': (4,),
  'Com': (5,),
}

dev.add_footprint(name, pin_map)

#-----------------------------------------------------------------------------

class re10982(object):

  def __init__(self):
    global name
    self.name = name

  def pad_name(self, i):
    return ('A', 'C', 'B', '1', '2', '3', '4', '5')[i]

  def pad_xy(self, i):
    if i <= 2:
      x = (i * 2.5) + 1.5
      y = 14.5
    else:
      x = (i - 3) * 2.0
      y = 0.0
    return (x, y)

  def add_pads(self, mod):
    """add the pads"""
    pad_size = kicad.mil2mm(68)
    for i in range(8):
      hole_size = (1.0, 1.1)[i <= 2]
      pad_shape = ('circle', 'rect')[i == 0]
      p = kicad.mod_pad(self.pad_name(i), 'thru_hole', pad_shape, ('*.Cu', '*.Mask'))
      p.set_size(pad_size, pad_size).set_drill(hole_size)
      p.set_xy(self.pad_xy(i))
      mod.add_pad(p)

  def add_courtyard(self, mod):
    """add a courtyard"""
    w = 14.5
    h = 17.5
    x = (8.0 - w) / 2.0
    y = -1.5
    mod.add_rect(x, y, w, h, 'F.CrtYd', 0.05)

  def add_fab(self, mod):
    """add a fab layer"""
    # device outline
    w = 14.0
    h = 13.2
    x = (8.0 - w) / 2.0
    y = (14.5 - h) / 2.0
    mod.add_rect(x, y, w, h, 'F.Fab', 0.1)
    # fab name
    t = kicad.mod_text(self.name, 'value', 'F.Fab')
    t.set_xy((4.0, 7.0)) # center
    mod.add_shape(t)
    # fab reference
    t = kicad.mod_text('%R', 'user', 'F.Fab')
    t.set_xy((-0.5, 2.0)) # top left
    mod.add_shape(t)

  def add_silk(self, mod):
    """add a silk layer"""
    # silk reference
    t = kicad.mod_text('REF**', 'reference', 'F.SilkS')
    t.set_xy((-1.0, 15.0)) # bottom left
    mod.add_shape(t)
    # silk pin 1
    t = kicad.mod_text('1', 'user', 'F.SilkS')
    t.set_xy((-1.5, 0))
    mod.add_shape(t)

  def add_holes(self, mod):
    """add mounting holes"""
    hole_size = 2.0
    pad_size = 3.0
    d = 13.2
    x0 = (8.0 - d) / 2.0
    y0 = 7.0
    lh = (x0, y0)
    rh = (x0 + d, y0)
    for v in (lh, rh):
      p = kicad.mod_pad('', 'thru_hole', 'circle', ('*.Cu', '*.Mask'))
      p.set_size(pad_size, pad_size).set_drill(hole_size)
      p.set_xy(v)
      mod.add_pad(p)

  def __str__(self):
    """return the kicad_mod code for this footprint"""
    global descr, tags
    mod = kicad.mod_module(self.name, descr)
    mod.add_tags(tags)
    self.add_pads(mod)
    self.add_courtyard(mod)
    self.add_fab(mod)
    self.add_silk(mod)
    self.add_holes(mod)
    return str(mod)

footprint.db.add(re10982())

#-----------------------------------------------------------------------------
