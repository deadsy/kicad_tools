#-----------------------------------------------------------------------------
"""

STM32F407xx

"""
#-----------------------------------------------------------------------------

import component

#-----------------------------------------------------------------------------

name = 'STM32F407xx'
descr = '32-Bit Cortex M4 Microcontroller'
tags = (name, 'ST', 'STM32',)
url = 'http://www.st.com/resource/en/datasheet/stm32f405og.pdf'

#-----------------------------------------------------------------------------

dev = component.component(name, 'U', descr)
dev.add_tags = (tags)
dev.set_url(url)

pins = []
# add all the io pins
for port in ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I'):
  for i in range(16):
    pins.append(component.pin('P%s%d' % (port, i), 'inout'))

# fixups
component.append_pin_name(pins, 'PA0', 'WKUP')
component.append_pin_name(pins, 'PA13', 'JTMS-SWDIO')
component.append_pin_name(pins, 'PA14', 'JTCK/SWCLK')
component.append_pin_name(pins, 'PA15', 'JTDI')
component.append_pin_name(pins, 'PB2', 'BOOT1')
component.append_pin_name(pins, 'PB3', 'JTDO/TRACESWO')
component.append_pin_name(pins, 'PB4', 'NJTRST')
component.append_pin_name(pins, 'PC14', 'OSC32_IN')
component.append_pin_name(pins, 'PC15', 'OSC32_OUT')
component.append_pin_name(pins, 'PH0', 'OSC_IN')
component.append_pin_name(pins, 'PH1', 'OSC_OUT')

other_pins = (
  component.pin('VBAT', 'power_in'),
  component.pin('VSS', 'power_in'),
  component.pin('VDD', 'power_in'),
  component.pin('NRST', 'inout'),
  component.pin('VSSA', 'power_in'),
  component.pin('VREF-', 'power_in'),
  component.pin('VREF+', 'power_in'),
  component.pin('VDDA', 'power_in'),
  component.pin('BYPASS_REG', 'in'),
  component.pin('VCAP_1', 'power_in'),
  component.pin('VCAP_2', 'power_in'),
  component.pin('BOOT0', 'in'),
  component.pin('PDR_ON', 'in'),
)
pins.extend(other_pins)

dev.add_pins(pins)
component.db.add(dev)

#-----------------------------------------------------------------------------
# LQFP64

pin_map = {
  'VBAT': (1,),
  'PC13': (2,),
  'PC14/OSC32_IN': (3,),
  'PC15/OSC32_OUT': (4,),
  'PH0/OSC_IN': (5,),
  'PH1/OSC_OUT': (6,),
  'NRST': (7,),
  'PC0': (8,),
  'PC1': (9,),
  'PC2': (10,),
  'PC3': (11,),
  'VSSA': (12,),
  'VDDA': (13,),
  'PA0/WKUP': (14,),
  'PA1': (15,),
  'PA2': (16,),
  'PA3': (17,),
  'VSS': (18, 63,),
  'PA4': (20,),
  'PA5': (21,),
  'PA6': (22,),
  'PA7': (23,),
  'PC4': (24,),
  'PC5': (25,),
  'PB0': (26,),
  'PB1': (27,),
  'PB2/BOOT1': (28,),
  'PB10': (29,),
  'PB11': (30,),
  'VCAP_1': (31,),
  'VDD': (19, 32, 48, 64),
  'VCAP_2': (47,),
  'PA13/JTMS-SWDIO': (46,),
  'PA12': (45,),
  'PA11': (44,),
  'PA10': (43,),
  'PA9': (42,),
  'PA8': (41,),
  'PC9': (40,),
  'PC8': (39,),
  'PC7': (38,),
  'PC6': (37,),
  'PB15': (36,),
  'PB14': (35,),
  'PB13': (34,),
  'PB12': (33,),
  'PB9': (62,),
  'PB8': (61,),
  'BOOT0': (60,),
  'PB7': (59,),
  'PB6': (58,),
  'PB5': (57,),
  'PB4/NJTRST': (56,),
  'PB3/JTDO/TRACESWO': (55,),
  'PD2': (54,),
  'PC12': (53,),
  'PC11': (52,),
  'PC10': (51,),
  'PA15/JTDI': (50,),
  'PA14/JTCK/SWCLK': (49,),
}

dev.add_footprint('LQFP64', pin_map)

#-----------------------------------------------------------------------------
# UFBGA176

bga = (
  ('A', ('PE3', 'PE2', 'PE1', 'PE0', 'PB8', 'PB5', 'PG14', 'PG13', 'PB4', 'PB3', 'PD7', 'PC12', 'PA15', 'PA14', 'PA13')),
  ('B', ('PE4', 'PE5', 'PE6', 'PB9', 'PB7', 'PB6', 'PG15', 'PG12', 'PG11', 'PG10', 'PD6', 'PD0', 'PC11', 'PC10', 'PA12')),
  ('C', ('VBAT', 'PI7', 'PI6', 'PI5', 'VDD', 'PDR_ON', 'VDD', 'VDD', 'VDD', 'PG9', 'PD5', 'PD1', 'PI3', 'PI2', 'PA11')),
  ('D', ('PC13', 'PI8', 'PI9', 'PI4', 'VSS', 'BOOT0', 'VSS', 'VSS', 'VSS', 'PD4', 'PD3', 'PD2', 'PH15', 'PI1', 'PA10')),
  ('E', ('PC14', 'PF0', 'PI10', 'PI11', None, None, None, None, None, None, None, 'PH13', 'PH14', 'PI0', 'PA9')),
  ('F', ('PC15', 'VSS', 'VDD', 'PH2', None, 'VSS', 'VSS', 'VSS', 'VSS', 'VSS', None, 'VSS', 'VCAP_2', 'PC9', 'PA8')),
  ('G', ('PH0', 'VSS', 'VDD', 'PH3',  None, 'VSS', 'VSS', 'VSS', 'VSS', 'VSS', None, 'VSS', 'VDD', 'PC8', 'PC7')),
  ('H', ('PH1', 'PF2', 'PF1', 'PH4',  None, 'VSS', 'VSS', 'VSS', 'VSS', 'VSS', None, 'VSS', 'VDD', 'PG8', 'PC6')),
  ('J', ('NRST', 'PF3', 'PF4', 'PH5', None, 'VSS', 'VSS', 'VSS', 'VSS', 'VSS', None, 'VDD', 'VDD', 'PG7', 'PG6')),
  ('K', ('PF7', 'PF6', 'PF5', 'VDD',  None, 'VSS', 'VSS', 'VSS', 'VSS', 'VSS', None, 'PH12', 'PG5', 'PG4', 'PG3')),
  ('L', ('PF10', 'PF9', 'PF8', 'BYPASS_REG', None, None, None, None, None, None, None, 'PH11', 'PH10', 'PD15', 'PG2')),
  ('M', ('VSSA', 'PC0', 'PC1', 'PC2', 'PC3', 'PB2', 'PG1', 'VSS', 'VSS', 'VCAP_1', 'PH6', 'PH8', 'PH9', 'PD14', 'PD13')),
  ('N', ('VREF-', 'PA1', 'PA0', 'PA4', 'PC4', 'PF13', 'PG0', 'VDD', 'VDD', 'VDD', 'PE13', 'PH7', 'PD12', 'PD11', 'PD10')),
  ('P', ('VREF+', 'PA2', 'PA6', 'PA5', 'PC5', 'PF12', 'PF15', 'PE8', 'PE9', 'PE11', 'PE14', 'PB12', 'PB13', 'PD9', 'PD8')),
  ('R', ('VDDA', 'PA3', 'PA7', 'PB1', 'PB0', 'PF11', 'PF14', 'PE7', 'PE10', 'PE12', 'PE15', 'PB10', 'PB11', 'PB14', 'PB15')),
)

def bga_to_pin_map(bga):
  pin_map = {}
  for row in bga:
    letter = row[0]
    pins = row[1]
    assert len(pins) == 15
    for (i, name) in enumerate(pins):
      if name is not None:
        if pin_map.has_key(name):
          pin_map[name].append('%s%d' % (letter, i + 1))
        else:
          pin_map[name] = ['%s%d' % (letter, i + 1),]
  return pin_map

dev.add_footprint('UFBGA176', bga_to_pin_map(bga))

#-----------------------------------------------------------------------------
