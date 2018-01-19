#-----------------------------------------------------------------------------
"""

STM32F407xx

"""
#-----------------------------------------------------------------------------

import util

#-----------------------------------------------------------------------------

dev = util.component('STM32F407xx', '32-Bit Cortex M4 Microcontroller')
dev.add_tags(('ST', 'STM32'))
dev.set_url('www.st.com/resource/en/datasheet/stm32f405og.pdf')

pins = []
# add all the io pins
for port in ('A','B','C','D','E','F','G','H','I'):
  for i in range(16):
    pins.append(util.pin('P%s%d' % (port, i), 'inout'))

# fixups
util.rename_pin(pins, 'PA0', 'PA0/WKUP')
util.rename_pin(pins, 'PA13', 'PA13/JTMS-SWDIO')
util.rename_pin(pins, 'PA14', 'PA14/JTCK/SWCLK')
util.rename_pin(pins, 'PA15', 'PA15/JTDI')
util.rename_pin(pins, 'PB2', 'PB2/BOOT1')
util.rename_pin(pins, 'PB3', 'PB3/JTDO/TRACESWO')
util.rename_pin(pins, 'PB4', 'PB4/NJTRST')
util.rename_pin(pins, 'PC14', 'PC14/OSC32_IN')
util.rename_pin(pins, 'PC15', 'PC15/OSC32_OUT')
util.rename_pin(pins, 'PH0', 'PH0/OSC_IN')
util.rename_pin(pins, 'PH1', 'PH1/OSC_OUT')

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





