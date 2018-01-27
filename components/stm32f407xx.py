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

# add all the io pins
for (j, port) in enumerate(('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I')):
  for k in range(16):
    dev.add_pin('P%s%d' % (port, k), 'inout').set_group(j + 1)

dev.add_pin('VBAT', 'power_in')
dev.add_pin('VSS', 'power_in')
dev.add_pin('VDD', 'power_in')
dev.add_pin('NRST', 'inout')
dev.add_pin('VSSA', 'power_in')
dev.add_pin('VREF-', 'power_in')
dev.add_pin('VREF+', 'power_in')
dev.add_pin('VDDA', 'power_in')
dev.add_pin('BYPASS_REG', 'in')
dev.add_pin('VCAP_1', 'power_in')
dev.add_pin('VCAP_2', 'power_in')
dev.add_pin('BOOT0', 'in')
dev.add_pin('PDR_ON', 'in')

# fixups
dev.get_pin('PA0').add_names(('WKUP',))
dev.get_pin('PA13').add_names(('JTMS' 'SWDIO',))
dev.get_pin('PA14').add_names(('JTCK', 'SWCLK',))
dev.get_pin('PA15').add_names(('JTDI',))
dev.get_pin('PB2').add_names(('BOOT1',))
dev.get_pin('PB3').add_names(('JTDO', 'TRACESWO',))
dev.get_pin('PB4').add_names(('NJTRST',))
dev.get_pin('PC14').add_names(('OSC32_IN',))
dev.get_pin('PC15').add_names(('OSC32_OUT',))
dev.get_pin('PH0').add_names(('OSC_IN',))
dev.get_pin('PH1').add_names(('OSC_OUT',))

component.db.add(dev)

#-----------------------------------------------------------------------------
# LQFP64

pin_map = {
  'VBAT': (1,),
  'PC13': (2,),
  'PC14': (3,),
  'PC15': (4,),
  'PH0': (5,),
  'PH1': (6,),
  'NRST': (7,),
  'PC0': (8,),
  'PC1': (9,),
  'PC2': (10,),
  'PC3': (11,),
  'VSSA': (12,),
  'VDDA': (13,),
  'PA0': (14,),
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
  'PB2': (28,),
  'PB10': (29,),
  'PB11': (30,),
  'VCAP_1': (31,),
  'VDD': (19, 32, 48, 64),
  'VCAP_2': (47,),
  'PA13': (46,),
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
  'PB4': (56,),
  'PB3': (55,),
  'PD2': (54,),
  'PC12': (53,),
  'PC11': (52,),
  'PC10': (51,),
  'PA15': (50,),
  'PA14': (49,),
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
