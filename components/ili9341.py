#-----------------------------------------------------------------------------
"""

ILI9341 LCD Module

There are 3 SPI connected subsystems in this module:
* An LCD controller
* Touch screen
* SD card

"""
#-----------------------------------------------------------------------------

import kicad
import footprint
from component import *

#-----------------------------------------------------------------------------

name = 'ILI9341'
descr = 'LCD Module 2.8 inch 240x320 SPI TFT with touch sensor and SD card'

#-----------------------------------------------------------------------------

dev = component(name, 'M', descr)
dev.add_tags = (('LCD',))
dev.set_url('https://www.amazon.com/gp/product/B017FZTIO6/ref=od_aui_detailpages00?ie=UTF8&psc=1')

pins = (
  # power
  pin('VCC', 'power_in'),
  pin('GND', 'power_in'),
  # lcd
  pin('LCD_CS', 'in'),
  pin('LCD_RESET', 'in'),
  pin('LCD_DC', 'in'),
  pin('LCD_SDI', 'in'),
  pin('LCD_SCK', 'in'),
  pin('LCD_LED', 'in'),
  pin('LCD_SDO', 'out'),
  # touch screen
  pin('TS_CLK', 'in', group=1),
  pin('TS_CS', 'in', group=1),
  pin('TS_DI', 'in', group=1),
  pin('TS_DO', 'out', group=1),
  pin('TS_IRQ', 'out', group=1),
  # SD card
  pin('SD_CS', 'in', group=2),
  pin('SD_MOSI', 'in', group=2),
  pin('SD_MISO', 'out', group=2),
  pin('SD_CLK', 'in', group=2),
)

dev.add_pins(pins)

#-----------------------------------------------------------------------------

pin_map = {
  'VCC': (1,),
  'GND': (2,),
  'LCD_CS': (3,),
  'LCD_RESET': (4,),
  'LCD_DC': (5,),
  'LCD_SDI': (6,),
  'LCD_SCK': (7,),
  'LCD_LED': (8,),
  'LCD_SDO': (9,),
  'TS_CLK': (10,),
  'TS_CS': (11,),
  'TS_DI': (12,),
  'TS_DO': (13,),
  'TS_IRQ': (14,),
  'SD_CS': (15,),
  'SD_MOSI': (16,),
  'SD_MISO': (17,),
  'SD_CLK': (18,),
}

dev.add_footprint('ILI9341', pin_map)

#-----------------------------------------------------------------------------

class ili9341(object):

  def __init__(self, name, descr):
    self.name = name
    self.descr = descr

  def __str__(self):
    """return the kicad_mod code for this footprint"""
    mod = kicad.mod_module(self.name, self.descr)
    return str(mod)

footprint.db.add(ili9341(name, descr))

#-----------------------------------------------------------------------------


"""


# pin_number, pin_name, pin_type, pad_position
pins = (
  (1, 'VCC', 'W', (0, 0)),
  (3, 'LCD_CS', 'I', (0, 2)),
  (4, 'LCD_RESET', 'I', (0, 3)),
  (5, 'LCD_DC', 'I', (0, 4)),
  (6, 'LCD_SDI', 'I', (0, 5)),
  (7, 'LCD_SCK', 'I', (0, 6)),
  (8, 'LCD_LED', 'I', (0, 7)),
  (9, 'LCD_SDO', 'O', (0, 8)),
  (10, 'TS_CLK', 'I', (0, 9)),
  (11, 'TS_CS', 'I', (0, 10)),
  (12, 'TS_DI', 'I', (0, 11)),
  (13, 'TS_DO', 'O', (0, 12)),
  (14, 'TS_IRQ', 'O', (0, 13)),
  (15, 'SD_CS', 'I', (1, 0)),
  (16, 'SD_MOSI', 'I', (1, 1)),
  (17, 'SD_MISO', 'O', (1, 2)),
  (18, 'SD_CLK', 'I', (1, 3)),
  (2, 'GND', 'W', (0, 1)),
)

board_width = 50.0
board_height = 86.0

def pad_name(pin_number):
  return '%d' % pin_number



#-----------------------------------------------------------------------------
# schematic symbol

p_len = 200
p_delta = 100
r_extra = 100
rw = 600
rh = ((len(pins) - 1) * p_delta) + (2 * r_extra)

def set_pins(unit, pins, w, h):

  i = 0
  for (pin_number, pin_name, pin_type, _) in pins:
    p = kicad.lib_pin(pad_name(pin_number), pin_name)
    x = w/2 + p_len
    y = h/2 - r_extra - (i * p_delta)
    p.ofs_xy(x, y)
    p.set_orientation('L')
    p.set_type(pin_type)
    p.set_length(p_len)
    unit.add_pin(p)
    i += 1

lib = kicad.lib_component(name, 'M')
lib.get_text(0).set_bl().ofs_xy(-rw/2, rh/2 + 50) # set the reference location
lib.get_text(1).set_tl().ofs_xy(-rw/2, -rh/2 - 50) # set the name location
lib.add_footprint('ggm', name)

u = kicad.lib_unit()
u.add_shape(kicad.lib_rect(rw, rh))
set_pins(u, pins, rw, rh)
lib.add_unit(u)

# pin alignment
lib.ofs_xy(0, 50)

#-----------------------------------------------------------------------------
# pcb footprint

def pad_xy(pad_position):

  pin_spacing = kicad.mil2mm(100)
  (group, idx) = pad_position
  x = group * kicad.mil2mm(500)
  y = group * kicad.mil2mm(-3175)
  x += idx * pin_spacing
  return (x, y)

def mod_add_pads(mod, pins):
  pad_size = kicad.mil2mm(68)
  hole_size = kicad.mil2mm(40)
  for (pin_number, pin_name, pin_type, pad_position) in pins:
    pad_shape = ('circle', 'rect')[pin_number == 1]
    p = kicad.mod_pad(pad_name(pin_number), 'thru_hole', pad_shape, ('*.Cu', '*.Mask'))
    p.set_size(pad_size, pad_size).set_drill(hole_size)
    (x, y) = pad_xy(pad_position)
    p.set_xy(x, y)
    mod.add_pad(p)

def mod_add_connector_outline(mod):

  ch = kicad.mil2mm(100)
  dx = kicad.mil2mm(50)
  dy = kicad.mil2mm(50)
  # large connector, group = 0
  (cx, cy) = pad_xy((0, 0))
  cx -= dx
  cy -= dy
  mod.add_rect(cx, cy, kicad.mil2mm(14 * 100), ch, 'F.SilkS', 0.12)
  # small connector, group = 1
  (cx, cy) = pad_xy((1, 0))
  cx -= dx
  cy -= dy
  mod.add_rect(cx, cy, kicad.mil2mm(4 * 100), ch, 'F.SilkS', 0.12)

def mod_add_board_outline(mod):

  bw = board_width
  bh = board_height
  bx = (kicad.mil2mm(1300) - bw)/2.0
  by = kicad.mil2mm(50) - bh
  mod.add_rect(bx, by, bw, bh, 'F.CrtYd', 0.05)
  mod.add_rect(bx, by, bw, bh, 'F.Fab', 0.1)

def mod_add_mounting_holes(mod):
  hole_size = kicad.mil2mm(120)
  pad_size = kicad.mil2mm(150)
  w = 44.0
  h = 76.0
  x0 = (kicad.mil2mm(1300) - w) / 2.0
  y0 = -4.0
  tl = (x0, y0 - h)
  tr = (x0 + w, y0 - h)
  bl = (x0, y0)
  br = (x0 + w, y0)
  for (x, y) in (tl, tr, bl, br):
    p = kicad.mod_pad('', 'thru_hole', 'circle', ('*.Cu', '*.Mask'))
    p.set_size(pad_size, pad_size).set_drill(hole_size)
    p.set_xy(x, y)
    mod.add_pad(p)

def mod_add_text(mod):
  # silk reference
  t = kicad.mod_text('REF**', 'reference', 'F.SilkS')
  t.set_xy(0, kicad.mil2mm(-100))
  mod.add_shape(t)
  # silk pin 1
  t = kicad.mod_text('1', 'user', 'F.SilkS')
  t.set_xy(kicad.mil2mm(-100), 0)
  mod.add_shape(t)
  # fab name at top left
  t = kicad.mod_text(name, 'value', 'F.Fab')
  t.set_xy(kicad.mil2mm(0), kicad.mil2mm(-3250))
  mod.add_shape(t)
  # fab reference at top left
  t = kicad.mod_text('%R', 'user', 'F.Fab')
  t.set_xy(kicad.mil2mm(0), kicad.mil2mm(-3150))
  mod.add_shape(t)

def mod_init(mod):
  mod.add_tags(tags)
  mod_add_pads(mod, pins)
  mod_add_connector_outline(mod)
  mod_add_board_outline(mod)
  mod_add_mounting_holes(mod)
  mod_add_text(mod)

mod = kicad.mod_module(name, descr)
mod_init(mod)

"""
#-----------------------------------------------------------------------------
