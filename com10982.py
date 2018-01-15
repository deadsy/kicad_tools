#-----------------------------------------------------------------------------
"""

com-10982 - Rotary Encoder - Illuminated (RGB)
https://cdn.sparkfun.com/datasheets/Components/Switches/EC12PLRGBSDVBF-D-25K-24-24C-6108-6H.pdf

"""
#-----------------------------------------------------------------------------

import util
import kicad

#-----------------------------------------------------------------------------

name = 'COM10982'
descr = 'Rotary Encoder Illuminated (RGB)'
tags = (name, 'rotary', 'encoder', 'switch',)
url = 'https://www.sparkfun.com/products/10982'

# (pin_number, pin_name, pin_type)
pins = (
  ('A', 'PH_A', 'P'),
  ('B', 'PH_B', 'P'),
  ('C', 'PH_Com', 'P'),
  ('1', 'LED_R',  'P'),
  ('2', 'LED_G', 'P'),
  ('3', 'PB', 'P'),
  ('4', 'LED_B',  'P'),
  ('5', 'Com', 'P'),
)

#-----------------------------------------------------------------------------
# part documentation

dcm = kicad.dcm_component(name, descr)
dcm.add_keywords(tags)
dcm.add_url(url)

#-----------------------------------------------------------------------------
# schematic symbol

lib = util.build_symbol(name, 'S', pins, 400)
lib.add_footprint('ggm', name)

#-----------------------------------------------------------------------------
# pcb footprint

def pad_xy(pin_number):
  """return the pad x,y position"""
  if pin_number in ('A','B','C'):
    x = ((ord(pin_number) - ord('A')) * 2.5) + 1.5
    y = 14.5
  else:
    x = (int(pin_number) - 1) * 2.0
    y = 0.0
  return (x, y)

def mod_add_pads(mod, pins):
  pad_size = kicad.mil2mm(68)
  for (pin_number, pin_name, pin_type) in pins:
    hole_size = (1.0, 1.1)[pin_number in ('A', 'B', 'C')]
    pad_shape = ('circle', 'rect')[pin_number == '1']
    p = kicad.mod_pad(pin_number, 'thru_hole', pad_shape, ('*.Cu', '*.Mask'))
    p.set_size(pad_size, pad_size).set_drill(hole_size)
    (x, y) = pad_xy(pin_number)
    p.set_xy(x, y)
    mod.add_pad(p)

def mod_add_device_outline(mod):
  """add a device outline"""
  w = 14.5
  h = 17.5
  x = (8.0 - w) / 2.0
  y = -1.5
  mod.add_rect(x, y, w, h, 'F.CrtYd', 0.05)
  w = 14.0
  h = 13.2
  x = (8.0 - w) / 2.0
  y = (14.5 - h) / 2.0
  mod.add_rect(x, y, w, h, 'F.Fab', 0.1)

def mod_add_text(mod):
  # silk reference
  t = kicad.mod_text('REF**', 'reference', 'F.SilkS')
  t.set_xy(kicad.mil2mm(25), kicad.mil2mm(-100))
  mod.add_shape(t)
  # silk pin 1
  t = kicad.mod_text('1', 'user', 'F.SilkS')
  t.set_xy(kicad.mil2mm(-100), 0)
  mod.add_shape(t)
  # fab name at top left
  t = kicad.mod_text(name, 'value', 'F.Fab')
  t.set_xy(kicad.mil2mm(-125), kicad.mil2mm(-1300))
  mod.add_shape(t)
  # fab reference at top left
  t = kicad.mod_text('%R', 'user', 'F.Fab')
  t.set_xy(kicad.mil2mm(-125), kicad.mil2mm(-1200))
  mod.add_shape(t)

def mod_init(mod):
  mod.add_tags(tags)
  mod_add_pads(mod, pins)
  mod_add_device_outline(mod)
  mod_add_text(mod)

mod = kicad.mod_module(name, descr)
mod_init(mod)

#-----------------------------------------------------------------------------

