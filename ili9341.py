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

dcm = kicad.doc_component(name, 'ILI9341 LCD Module')
dcm.add_keywords((name, 'LCD',))

#-----------------------------------------------------------------------------

p_len = 200
p_delta = 150
r_extra = 100
rw = 600
rh = ((len(pinset) - 1) * p_delta) + (2 * r_extra)

def set_pins(unit, pinset, w, h):
  for (pin_number, pin_name, pin_type) in pinset:
    p = kicad.sch_pin('%d' % pin_number, pin_name)
    x = w/2 + p_len
    y = h/2 - r_extra - ((pin_number - 1) * p_delta)
    p.ofs_xy(x, y)
    p.set_orientation('L')
    p.set_type(pin_type)
    p.set_length(p_len)
    unit.add_pin(p)

#-----------------------------------------------------------------------------

lib = kicad.sch_component(name, 'M')
lib.get_text(0).set_bl().ofs_xy(-rw/2, rh/2 + 50)
lib.get_text(1).set_tl().ofs_xy(-rw/2, -rh/2 - 50)

u = kicad.sch_unit()
u.add_shape(kicad.sch_rect(rw, rh))
set_pins(u, pinset, rw, rh)
lib.add_unit(u)

# pin alignment
lib.ofs_xy(0, 25)

#-----------------------------------------------------------------------------