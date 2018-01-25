#-----------------------------------------------------------------------------
"""

STM32F407xx

"""
#-----------------------------------------------------------------------------

import util

#-----------------------------------------------------------------------------

dev = util.component('STM32F407xx', 'U', '32-Bit Cortex M4 Microcontroller')
dev.add_tags(('ST', 'STM32'))
dev.set_url('www.st.com/resource/en/datasheet/stm32f405og.pdf')

pins = []
# add all the io pins
for port in ('A','B','C','D','E','F','G','H','I'):
  for i in range(16):
    pins.append(util.pin('P%s%d' % (port, i), 'inout'))

# fixups
util.append_pin_name(pins, 'PA0', 'WKUP')
util.append_pin_name(pins, 'PA13', 'JTMS-SWDIO')
util.append_pin_name(pins, 'PA14', 'JTCK/SWCLK')
util.append_pin_name(pins, 'PA15', 'JTDI')
util.append_pin_name(pins, 'PB2', 'BOOT1')
util.append_pin_name(pins, 'PB3', 'JTDO/TRACESWO')
util.append_pin_name(pins, 'PB4', 'NJTRST')
util.append_pin_name(pins, 'PC14', 'OSC32_IN')
util.append_pin_name(pins, 'PC15', 'OSC32_OUT')
util.append_pin_name(pins, 'PH0', 'OSC_IN')
util.append_pin_name(pins, 'PH1', 'OSC_OUT')

other_pins = (
  util.pin('VBAT', 'power_in'),
  util.pin('VSS', 'power_in'),
  util.pin('VDD', 'power_in'),
  util.pin('NRST', 'inout'),
  util.pin('VSSA', 'power_in'),
  util.pin('VREF-', 'power_in'),
  util.pin('VREF+', 'power_in'),
  util.pin('VDDA', 'power_in'),
  util.pin('BYPASS_REG', 'in'),
  util.pin('VCAP_1', 'power_in'),
  util.pin('VCAP_2', 'power_in'),
  util.pin('BOOT0', 'in'),
  util.pin('PDR_ON', 'in'),
)
pins.extend(other_pins)

dev.add_pins(pins)

#-----------------------------------------------------------------------------





