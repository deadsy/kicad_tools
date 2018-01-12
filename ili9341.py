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

#-----------------------------------------------------------------------------

name = 'ILI9341'
descr = 'LCD Module 2.8 inch 240x320 SPI TFT with touch sensor and SD card'
tags = (name, 'LCD',)
url = 'https://www.amazon.com/gp/product/B017FZTIO6/ref=od_aui_detailpages00?ie=UTF8&psc=1'

pinset = (
  (1, 'LCD_SDO', 'O'),
  (2, 'LCD_LED', 'I'),
  (3, 'LCD_SCK', 'I'),
  (4, 'LCD_SDI', 'I'),
  (5, 'LCD_DC', 'I'),
  (6, 'LCD_RESET', 'I'),
  (7, 'LCD_CS', 'I'),
  (8, 'GND', 'W'),
  (9, 'VCC', 'W'),
  (10, 'TS_IRQ', 'O'),
  (11, 'TS_DO', 'O'),
  (12, 'TS_DI', 'I'),
  (13, 'TS_CS', 'I'),
  (14, 'TS_CLK', 'I'),
  (15, 'SD_CS', 'I'),
  (16, 'SD_MOSI', 'I'),
  (17, 'SD_MISO', 'O'),
  (18, 'SD_CLK', 'I'),
)

#-----------------------------------------------------------------------------
# part documentation

dcm = kicad.dcm_component(name, descr)
dcm.add_keywords(tags)
dcm.add_url(url)

#-----------------------------------------------------------------------------
# schematic symbol

p_len = 200
p_delta = 100
r_extra = 100
rw = 600
rh = ((len(pinset) - 1) * p_delta) + (2 * r_extra)

def set_pins(unit, pins, w, h):
  """add the pins to the component unit"""
  for (pin_number, pin_name, pin_type) in pins:
    p = kicad.lib_pin('%d' % pin_number, pin_name)
    x = w/2 + p_len
    y = h/2 - r_extra - ((pin_number - 1) * p_delta)
    p.ofs_xy(x, y)
    p.set_orientation('L')
    p.set_type(pin_type)
    p.set_length(p_len)
    unit.add_pin(p)

lib = kicad.lib_component(name, 'M')
lib.get_text(0).set_bl().ofs_xy(-rw/2, rh/2 + 50) # set the reference location
lib.get_text(1).set_tl().ofs_xy(-rw/2, -rh/2 - 50) # set the name location
lib.add_footprint('ggm', name)

u = kicad.lib_unit()
u.add_shape(kicad.lib_rect(rw, rh))
set_pins(u, pinset, rw, rh)
lib.add_unit(u)

# pin alignment
lib.ofs_xy(0, 50)

#-----------------------------------------------------------------------------
# pcb footprint

mod = kicad.mod_module(name, descr)
mod.add_tags(tags)

t = kicad.mod_text('REF**', 'reference')
t.set_layer('F.SilkS')
mod.add_shape(t)

t = kicad.mod_text(name, 'value')
t.set_layer('F.Fab')
mod.add_shape(t)

mod.add_rect(50, 86, 'F.CrtYd', 0.05)

mod.add_pad(kicad.mod_pad('10', ptype='smd', shape='rect'))

#-----------------------------------------------------------------------------
