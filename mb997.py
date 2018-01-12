#-----------------------------------------------------------------------------
"""

MB997 - STM32F4 Discovery Board

"""
#-----------------------------------------------------------------------------

import kicad

#-----------------------------------------------------------------------------

name = 'MB997'
descr = 'STM32F4 Discovery Board'
tags = (name, 'STM32', 'STM32F4', 'STM32F407', 'Discovery',)
url = 'http://www.st.com/en/evaluation-tools/stm32f4discovery.html'

# (connector, number, name, type)
all_pins = (
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
    (1, 48, 'NC', 'N'),
    (2, 7, 'ph0_osc_in/PH0', 'B'),
    (2, 8, 'ph1_osc_out/PH1', 'B'),
    (2, 21, 'BOOT0', 'I'),
  ),
  ( # power
    (1, 3, 'VDD', 'w'),
    (1, 4, 'VDD', 'w'),
    (2, 22, 'VDD', 'w'),
    (2, 3, '5V', 'w'),
    (2, 4, '5V', 'w'),
    (2, 5, '3V', 'w'),
    (2, 6, '3V', 'w'),
    (1, 1, 'GND', 'W'),
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

def set_pins(unit, pins, prefix, w, h):
  """add the pins to the component unit"""
  for (pin_number, pin_name, pin_type) in pins:
    p = kicad.lib_pin('%d.%d' % (prefix, pin_number), pin_name)
    x = (-w/2 - p_len, w/2 + p_len)[pin_number & 1 == 0]
    y = h/2 - r_extra + ((pin_number - 1) >> 1) * -p_delta
    p.ofs_xy(x, y)
    p.set_orientation(('R', 'L')[pin_number % 2 == 0])
    p.set_type(pin_type)
    p.set_length(p_len)
    unit.add_pin(p)

def add_pins(unit, pins, w, h):
  # add the pins to the unit"""
  i = 0
  for (prefix, pin_number, pin_name, pin_type) in pins:
    p = kicad.lib_pin('%d.%d' % (prefix, pin_number), pin_name)
    x = w/2 + p_len
    y = h/2 - r_extra - (i * p_delta)
    p.ofs_xy(x, y)
    p.set_orientation('L')
    p.set_type(pin_type)
    p.set_length(p_len)
    unit.add_pin(p)
    i += 1

def add_units(lib, all_pins):
  # add the units to the component"""
  for unit_pins in all_pins:
    u = kicad.lib_unit()
    u.add_shape(kicad.lib_rect(rw, rh))
    add_pins(u, unit_pins, rw, rh)
    lib.add_unit(u)

lib = kicad.lib_component(name, 'M')
lib.get_text(0).set_bl().ofs_xy(-rw/2, rh/2 + 50) # set the reference location
lib.get_text(1).set_tl().ofs_xy(-rw/2, -rh/2 - 50) # set the name location
lib.add_footprint('ggm', name)
add_units(lib, all_pins)

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

mod.add_rect(66, 97, 'F.CrtYd', 0.05)

mod.add_pad(kicad.mod_pad('10', ptype='smd', shape='rect'))

#-----------------------------------------------------------------------------
