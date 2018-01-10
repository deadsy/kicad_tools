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

# P1 Side (number, name, type)
pinset1 = (
  (1, 'GND', 'W'),
  (3, 'VDD', 'w'),
  (5, 'GND', 'W'),
  (7, 'PC1', 'B'),
  (9, 'PC3', 'B'),
  (11, 'PA1', 'B'),
  (13, 'PA3', 'B'),
  (15, 'PA5', 'B'),
  (17, 'PA7', 'B'),
  (19, 'PC5', 'B'),
  (21, 'PB1', 'B'),
  (23, 'GND', 'W'),
  (25, 'PE7', 'B'),
  (27, 'PE9', 'B'),
  (29, 'PE11', 'B'),
  (31, 'PE13', 'B'),
  (33, 'PE15', 'B'),
  (35, 'PB11', 'B'),
  (37, 'PB13', 'B'),
  (39, 'PB15', 'B'),
  (41, 'PD9', 'B'),
  (43, 'PD11', 'B'),
  (45, 'PD13', 'B'),
  (47, 'PD15', 'B'),
  (49, 'GND', 'W'),
  (2, 'GND', 'W'),
  (4, 'VDD', 'w'),
  (6, 'NRST', 'I'),
  (8, 'PC0', 'B'),
  (10, 'PC2', 'B'),
  (12, 'PA0', 'B'),
  (14, 'PA2', 'B'),
  (16, 'PA4', 'B'),
  (18, 'PA6', 'B'),
  (20, 'PC4', 'B'),
  (22, 'PB0', 'B'),
  (24, 'PB2', 'B'),
  (26, 'PE8', 'B'),
  (28, 'PE10', 'B'),
  (30, 'PE12', 'B'),
  (32, 'PE14', 'B'),
  (34, 'PB10', 'B'),
  (36, 'PB12', 'B'),
  (38, 'PB14', 'B'),
  (40, 'PD8', 'B'),
  (42, 'PD10', 'B'),
  (44, 'PD12', 'B'),
  (46, 'PD14', 'B'),
  (48, 'NC', 'N'),
  (50, 'GND', 'W'),
)

# P2 Side (number, name, type)
pinset2 = (
  (1, 'GND', 'W'),
  (3, '5V', 'w'),
  (5, '3V', 'w'),
  (7, 'PH0', 'B'),
  (9, 'PC14', 'B'),
  (11, 'PE6', 'B'),
  (13, 'PE4', 'B'),
  (15, 'PE2', 'B'),
  (17, 'PE0', 'B'),
  (19, 'PB8', 'B'),
  (21, 'BOOT0', 'I'),
  (23, 'PB6', 'B'),
  (25, 'PB4', 'B'),
  (27, 'PD7', 'B'),
  (29, 'PD5', 'B'),
  (31, 'PD3', 'B'),
  (33, 'PD1', 'B'),
  (35, 'PC12', 'B'),
  (37, 'PC10', 'B'),
  (39, 'PA14', 'B'),
  (41, 'PA10', 'B'),
  (43, 'PA8', 'B'),
  (45, 'PC8', 'B'),
  (47, 'PC6', 'B'),
  (49, 'GND', 'W'),
  (2, 'GND', 'W'),
  (4, '5V', 'w'),
  (6, '3V', 'w'),
  (8, 'PH1', 'B'),
  (10, 'PC15', 'B'),
  (12, 'PC13', 'B'),
  (14, 'PE5', 'B'),
  (16, 'PE3', 'B'),
  (18, 'PE1', 'B'),
  (20, 'PB9', 'B'),
  (22, 'VDD', 'w'),
  (24, 'PB7', 'B'),
  (26, 'PB5', 'B'),
  (28, 'PB3', 'B'),
  (30, 'PD6', 'B'),
  (32, 'PD4', 'B'),
  (34, 'PD2', 'B'),
  (36, 'PD0', 'B'),
  (38, 'PC11', 'B'),
  (40, 'PA15', 'B'),
  (42, 'PA13', 'B'),
  (44, 'PA9', 'B'),
  (46, 'PC9', 'B'),
  (48, 'PC7', 'B'),
  (50, 'GND', 'W'),
)

#-----------------------------------------------------------------------------
# part documentation

dcm = kicad.dcm_component(name, descr)
dcm.add_keywords(tags)

#-----------------------------------------------------------------------------
# schematic symbol

p_len = 200
p_delta = 150
r_extra = 100
p_height = len(pinset1) / 2
rh = (p_height - 1) * p_delta + (2 * r_extra)
rw = 800

def set_pins(unit, pinset, prefix, w, h):
  for (pin_number, pin_name, pin_type) in pinset:
    p = kicad.lib_pin('%d.%d' % (prefix, pin_number), pin_name)
    x = (-w/2 - p_len, w/2 + p_len)[pin_number & 1 == 0]
    y = h/2 - r_extra + ((pin_number - 1) >> 1) * -p_delta
    p.ofs_xy(x, y)
    p.set_orientation(('R', 'L')[pin_number % 2 == 0])
    p.set_type(pin_type)
    p.set_length(p_len)
    unit.add_pin(p)

lib = kicad.lib_component(name, 'M')
lib.get_text(0).set_bl().ofs_xy(-rw/2, rh/2 + 50)
lib.get_text(1).set_tl().ofs_xy(-rw/2, -rh/2 - 50)

u = kicad.lib_unit()
u.add_shape(kicad.lib_rect(rw, rh))
set_pins(u, pinset1, 1, rw, rh)
lib.add_unit(u)

u = kicad.lib_unit()
u.add_shape(kicad.lib_rect(rw, rh))
set_pins(u, pinset2, 2, rw, rh)
lib.add_unit(u)

#-----------------------------------------------------------------------------
# pcb footprint

mod = kicad.mod_module(name, descr)
mod.add_tags(tags)

t = kicad.mod_text('REF**', 'reference')
t.set_layer('F.SilkS')
mod.add_text(t)

t = kicad.mod_text(name, 'value')
t.set_layer('F.Fab')
mod.add_text(t)

mod.add_pad(kicad.mod_pad('10', ptype='smd', shape='rect'))

#-----------------------------------------------------------------------------
