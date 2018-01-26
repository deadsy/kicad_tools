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
  'VSS': (18,),
  'VDD': (19,),
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
  'VDD': (32,),
  'VDD': (48,),
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
  'VDD': (64,),
  'VSS': (63,),
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
