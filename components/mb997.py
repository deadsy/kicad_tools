#-----------------------------------------------------------------------------
"""

MB997 - STM32F4 Discovery Board

"""
#-----------------------------------------------------------------------------

import kicad
import footprint
from component import *

#-----------------------------------------------------------------------------

name = 'MB997'
descr = 'STM32F4 Discovery Board'
tags = (name, 'STM32', 'STM32F4', 'STM32F407', 'Discovery',)
url = 'http://www.st.com/en/evaluation-tools/stm32f4discovery.html'

#-----------------------------------------------------------------------------

dev = component(name, 'M', descr)
dev.add_tags = (tags)
dev.set_url(url)

pins = []
# add all the io pins
for port in ('A','B','C','D','E',):
  for i in range(16):
    pins.append(pin('P%s%d' % (port, i), 'inout'))

# fixups
append_pin_name(pins, 'PA0', 'SW_PUSH')
append_pin_name(pins, 'PA1', 'system_reset')
append_pin_name(pins, 'PA4', 'I2S3_WS')
append_pin_name(pins, 'PA5', 'SPI1_SCK')
append_pin_name(pins, 'PA6', 'SPI1_MISO')
append_pin_name(pins, 'PA7', 'SPI1_MOSI')
append_pin_name(pins, 'PA9', 'VBUS_FS')
append_pin_name(pins, 'PA10', 'OTG_FS_ID')
append_pin_name(pins, 'PA13', 'SWDIO')
append_pin_name(pins, 'PA14', 'SWCLK')
append_pin_name(pins, 'PB3', 'SWO')
append_pin_name(pins, 'PB6', 'Audio_SCL')
append_pin_name(pins, 'PB9', 'Audio_SDA')
append_pin_name(pins, 'PB10', 'CLK_IN')
append_pin_name(pins, 'PC0', 'OTG_FS_PSON')
append_pin_name(pins, 'PC3', 'PDM_OUT')
append_pin_name(pins, 'PC7', 'I2S3_MCK')
append_pin_name(pins, 'PC10', 'I2S3_SCK')
append_pin_name(pins, 'PC12', 'I2S3_SD')
append_pin_name(pins, 'PC14', 'osc_in')
append_pin_name(pins, 'PC15', 'osc_out')
append_pin_name(pins, 'PD4', 'Audio_RST')
append_pin_name(pins, 'PD5', 'OTG_FS_OC')
append_pin_name(pins, 'PD12', 'LED4')
append_pin_name(pins, 'PD13', 'LED3')
append_pin_name(pins, 'PD14', 'LED5')
append_pin_name(pins, 'PD15', 'LED6')
append_pin_name(pins, 'PE0', 'MEMS_INT1')
append_pin_name(pins, 'PE1', 'MEMS_INT2')
append_pin_name(pins, 'PE3', 'MEMS_CS')

remove_pin(pins, 'PA11')
remove_pin(pins, 'PA12')

other_pins = (
  pin('NRST', 'in'),
  pin('PH0/OSC_IN', 'inout'),
  pin('PH1/OSC_PUT', 'inout'),
  pin('BOOT0', 'in'),
  pin('NC', 'nc'),
  pin('VDD', 'power_in'),
  pin('5V', 'power_in'),
  pin('3V', 'power_in'),
  pin('GND', 'power_in'),
)
pins.extend(other_pins)

dev.add_pins(pins)

#-----------------------------------------------------------------------------










#-----------------------------------------------------------------------------

class mb997(object):

  def __init__(self):
    global name
    self.name = name

  def __str__(self):
    """return the kicad_mod code for this footprint"""
    global descr, tags
    mod = kicad.mod_module(self.name, descr)
    mod.add_tags(tags)
    return str(mod)

footprint.db.add(mb997())

#-----------------------------------------------------------------------------


"""

# (connector, number, name, type)
pins = (
  ( # port a
    (1, 12, 'SW_PUSH/PA0', 'B'),
    (1, 11, 'system_reset/PA1', 'B'),
    (1, 14, 'PA2', 'B'),
    (1, 13, 'PA3', 'B'),
    (1, 16, 'I2S3_WS/PA4', 'B'),
    (1, 15, 'SPI1_SCK/PA5', 'B'),
    (1, 18, 'SPI1_MISO/PA6', 'B'),
    (1, 17, 'SPI1_MOSI/PA7', 'B'),
    (2, 43, 'PA8', 'B'),
    (2, 44, 'VBUS_FS/PA9', 'B'),
    (2, 41, 'OTG_FS_ID/PA10', 'B'),
    # PA11 - not on connector
    # PA12 - not on connector
    (2, 42, 'SWDIO/PA13', 'B'),
    (2, 39, 'SWCLK/PA14', 'B'),
    (2, 40, 'PA15', 'B'),
  ),
  ( # port b
    (1, 22, 'PB0', 'B'),
    (1, 21, 'PB1', 'B'),
    (1, 24, 'PB2', 'B'),
    (2, 28, 'SWO/PB3', 'B'),
    (2, 25, 'PB4', 'B'),
    (2, 26, 'PB5', 'B'),
    (2, 23, 'Audio_SCL/PB6', 'B'),
    (2, 24, 'PB7', 'B'),
    (2, 19, 'PB8', 'B'),
    (2, 20, 'Audio_SDA/PB9', 'B'),
    (1, 34, 'CLK_IN/PB10', 'B'),
    (1, 35, 'PB11', 'B'),
    (1, 36, 'PB12', 'B'),
    (1, 37, 'PB13', 'B'),
    (1, 38, 'PB14', 'B'),
    (1, 39, 'PB15', 'B'),
  ),
  ( # port c
    (1, 8, 'OTG_FS_PSON/PC0', 'B'),
    (1, 7, 'PC1', 'B'),
    (1, 10, 'PC2', 'B'),
    (1, 9, 'PDM_OUT/PC3', 'B'),
    (1, 20, 'PC4', 'B'),
    (1, 19, 'PC5', 'B'),
    (2, 47, 'PC6', 'B'),
    (2, 48, 'I2S3_MCK/PC7', 'B'),
    (2, 45, 'PC8', 'B'),
    (2, 46, 'PC9', 'B'),
    (2, 37, 'I2S3_SCK/PC10', 'B'),
    (2, 38, 'PC11', 'B'),
    (2, 35, 'I2S3_SD/PC12', 'B'),
    (2, 12, 'PC13', 'B'),
    (2, 9, 'osc_in/PC14', 'B'),
    (2, 10, 'osc_out/PC15', 'B'),
  ),
  ( # port d
    (2, 36, 'PD0', 'B'),
    (2, 33, 'PD1', 'B'),
    (2, 34, 'PD2', 'B'),
    (2, 31, 'PD3', 'B'),
    (2, 32, 'Audio_RST/PD4', 'B'),
    (2, 29, 'OTG_FS_OC/PD5', 'B'),
    (2, 30, 'PD6', 'B'),
    (2, 27, 'PD7', 'B'),
    (1, 40, 'PD8', 'B'),
    (1, 41, 'PD9', 'B'),
    (1, 42, 'PD10', 'B'),
    (1, 43, 'PD11', 'B'),
    (1, 44, 'LED4/PD12', 'B'),
    (1, 45, 'LED3/PD13', 'B'),
    (1, 46, 'LED5/PD14', 'B'),
    (1, 47, 'LED6/PD15', 'B'),
  ),
  ( # port e
    (2, 17, 'MEMS_INT1/PE0', 'B'),
    (2, 18, 'MEMS_INT2/PE1', 'B'),
    (2, 15, 'PE2', 'B'),
    (2, 16, 'MEMS_CS/PE3', 'B'),
    (2, 13, 'PE4', 'B'),
    (2, 14, 'PE5', 'B'),
    (2, 11, 'PE6', 'B'),
    (1, 25, 'PE7', 'B'),
    (1, 26, 'PE8', 'B'),
    (1, 27, 'PE9', 'B'),
    (1, 28, 'PE10', 'B'),
    (1, 29, 'PE11', 'B'),
    (1, 30, 'PE12', 'B'),
    (1, 31, 'PE13', 'B'),
    (1, 32, 'PE14', 'B'),
    (1, 33, 'PE15', 'B'),
  ),
  ( # misc
    (1, 6, 'NRST', 'I'),
    (2, 7, 'ph0_osc_in/PH0', 'B'),
    (2, 8, 'ph1_osc_out/PH1', 'B'),
    (2, 21, 'BOOT0', 'I'),
    (1, 48, 'NC', 'N'),
  ),
  ( # power
    (1, 3, 'VDD', 'w'), # power output
    (1, 4, 'VDD', 'W'),
    (2, 22, 'VDD', 'W'),
    (2, 3, '5V', 'w'), # power output
    (2, 4, '5V', 'W'),
    (2, 5, '3V', 'w'), # power output
    (2, 6, '3V', 'W'),
    (1, 1, 'GND', 'w'), # power output
    (1, 2, 'GND', 'W'),
    (1, 5, 'GND', 'W'),
    (1, 23, 'GND', 'W'),
    (1, 49, 'GND', 'W'),
    (1, 50, 'GND', 'W'),
    (2, 1, 'GND', 'W'),
    (2, 2, 'GND', 'W'),
    (2, 49, 'GND', 'W'),
    (2, 50, 'GND', 'W'),
  ),
)

def pad_name(prefix, pin_number):
  return '%s%d' % (('A', 'B')[prefix == 2], pin_number)

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
p_height = 17
rw = 800
rh = ((p_height - 1) * p_delta) + (2 * r_extra)

def lib_add_pins(unit, pins, w, h):

  i = 0
  for (prefix, pin_number, pin_name, pin_type) in pins:
    p = kicad.lib_pin(pad_name(prefix, pin_number), pin_name)
    x = w/2 + p_len
    y = h/2 - r_extra - (i * p_delta)
    p.ofs_xy(x, y)
    p.set_orientation('L')
    p.set_type(pin_type)
    p.set_length(p_len)
    unit.add_pin(p)
    i += 1

def lib_add_units(lib, pins):

  for unit_pins in pins:
    u = kicad.lib_unit()
    u.add_shape(kicad.lib_rect(rw, rh))
    lib_add_pins(u, unit_pins, rw, rh)
    lib.add_unit(u)

lib = kicad.lib_component(name, 'M')
lib.get_text(0).set_bl().ofs_xy(-rw/2, rh/2 + 50) # set the reference location
lib.get_text(1).set_tl().ofs_xy(-rw/2, -rh/2 - 50) # set the name location
lib.add_footprint('ggm', name)
lib_add_units(lib, pins)

#-----------------------------------------------------------------------------
# pcb footprint

def pad_xy(prefix, pin_number):

  pin_spacing = kicad.mil2mm(100)
  row_spacing = kicad.mil2mm(2000)
  x = (prefix - 1) * row_spacing + ((pin_number - 1) & 1) * pin_spacing
  y = ((pin_number - 1) >> 1) * pin_spacing
  return (x, y)

def mod_add_pads(mod, pins):
  pad_size = kicad.mil2mm(68)
  hole_size = kicad.mil2mm(40)
  for unit_pins in pins:
    for (prefix, pin_number, pin_name, pin_type) in unit_pins:
      pad_shape = ('circle', 'rect')[pin_number == 1 and prefix == 1]
      p = kicad.mod_pad(pad_name(prefix, pin_number), 'thru_hole', pad_shape, ('*.Cu', '*.Mask'))
      p.set_size(pad_size, pad_size).set_drill(hole_size)
      (x, y) = pad_xy(prefix, pin_number)
      p.set_xy(x, y)
      mod.add_pad(p)

def mod_add_connector_outline(mod):

  cw = kicad.mil2mm(200)
  ch = kicad.mil2mm(25 * 100)
  for cx, cy in (pad_xy(1, 1), pad_xy(2, 1)):
    cx -= kicad.mil2mm(50)
    cy -= kicad.mil2mm(50)
    mod.add_rect(cx, cy, cw, ch, 'F.SilkS', 0.12)

def mod_add_board_outline(mod):

  bw = 66.0
  bh = 97.0
  bx = (kicad.mil2mm(2100) - bw)/2.0
  by = kicad.mil2mm(-1350)
  mod.add_rect(bx, by, bw, bh, 'F.CrtYd', 0.05)
  mod.add_rect(bx, by, bw, bh, 'F.Fab', 0.1)

def mod_add_text(mod):
  # silk reference
  t = kicad.mod_text('REF**', 'reference', 'F.SilkS')
  t.set_xy(kicad.mil2mm(25), kicad.mil2mm(-100))
  mod.add_shape(t)
  # silk pin 1
  t = kicad.mod_text('A1', 'user', 'F.SilkS')
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
  mod_add_connector_outline(mod)
  mod_add_board_outline(mod)
  mod_add_text(mod)

mod = kicad.mod_module(name, descr)
mod_init(mod)

"""

#-----------------------------------------------------------------------------
