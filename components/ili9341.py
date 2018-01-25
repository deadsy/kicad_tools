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
tags = ('LCD',)
url = 'https://www.amazon.com/gp/product/B017FZTIO6/ref=od_aui_detailpages00?ie=UTF8&psc=1'

#-----------------------------------------------------------------------------

dev = component(name, 'M', descr)
dev.add_tags = (tags)
dev.set_url(url)

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

dev.add_footprint(name, pin_map)

#-----------------------------------------------------------------------------

class ili9341(object):

  def __init__(self):
    global name
    self.name = name
    self.w = 50.0 # board width
    self.h = 86.0 # board height

  def pad_xy(self, i):
    """return the x, y position of pad i (i is zero based)"""
    if i < 14:
      group = 0
      idx = i
    else:
      group = 1
      idx = i - 14
    pin_spacing = kicad.mil2mm(100)
    x = group * kicad.mil2mm(500)
    y = group * kicad.mil2mm(-3175)
    x += idx * pin_spacing
    return (x, y)

  def courtyard(self, mod):
    """add a courtyard"""
    x = (kicad.mil2mm(1300) - self.w)/2.0
    y = kicad.mil2mm(50) - self.h
    mod.add_rect(x, y, self.w, self.h, 'F.CrtYd', 0.05)

  def fab(self, mod):
    """add a fab layer"""
    # fab name at top left
    t = kicad.mod_text(name, 'value', 'F.Fab')
    t.set_xy(kicad.mil2mm(0), kicad.mil2mm(-3250))
    mod.add_shape(t)
    # fab reference at top left
    t = kicad.mod_text('%R', 'user', 'F.Fab')
    t.set_xy(kicad.mil2mm(0), kicad.mil2mm(-3150))
    mod.add_shape(t)
    # board outline
    x = (kicad.mil2mm(1300) - self.w)/2.0
    y = kicad.mil2mm(50) - self.h
    mod.add_rect(x, y, self.w, self.h, 'F.Fab', 0.1)

  def silk(self, mod):
    """add a silk layer"""
    # silk reference
    t = kicad.mod_text('REF**', 'reference', 'F.SilkS')
    t.set_xy(0, kicad.mil2mm(-100))
    mod.add_shape(t)
    # silk pin 1
    t = kicad.mod_text('1', 'user', 'F.SilkS')
    t.set_xy(kicad.mil2mm(-100), 0)
    mod.add_shape(t)
    # add the connector outlines
    ch = kicad.mil2mm(100)
    dx = kicad.mil2mm(50)
    dy = kicad.mil2mm(50)
    # large connector
    (cx, cy) = self.pad_xy(0)
    cx -= dx
    cy -= dy
    mod.add_rect(cx, cy, kicad.mil2mm(14 * 100), ch, 'F.SilkS', 0.12)
    # small connector
    (cx, cy) = self.pad_xy(14)
    cx -= dx
    cy -= dy
    mod.add_rect(cx, cy, kicad.mil2mm(4 * 100), ch, 'F.SilkS', 0.12)

  def holes(self, mod):
    """add mounting holes"""
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

  def pads(self, mod):
    """add the pads"""
    pad_size = kicad.mil2mm(68)
    hole_size = kicad.mil2mm(40)
    for i in range(18):
      pad_shape = ('circle', 'rect')[i == 0]
      p = kicad.mod_pad('%d' % (i + 1), 'thru_hole', pad_shape, ('*.Cu', '*.Mask'))
      p.set_size(pad_size, pad_size).set_drill(hole_size)
      (x, y) = self.pad_xy(i)
      p.set_xy(x, y)
      mod.add_pad(p)

  def __str__(self):
    """return the kicad_mod code for this footprint"""
    global descr, tags
    mod = kicad.mod_module(self.name, descr)
    mod.add_tags(tags)
    self.pads(mod)
    self.courtyard(mod)
    self.fab(mod)
    self.silk(mod)
    self.holes(mod)
    return str(mod)

footprint.db.add(ili9341())

#-----------------------------------------------------------------------------
