#-----------------------------------------------------------------------------
"""

Broadcom JTAG Connector - as seen on the BCM949408EAP

"""
#-----------------------------------------------------------------------------

import component

#-----------------------------------------------------------------------------

dev = component.component('BCMJTAG', 'U', 'Broadcom 16 pin JTAG Connector (BCM949408EAP)')
dev.add_tags(('JTAG',))
dev.set_url('https://www.broadcom.com/products/wireless/wireless-lan-infrastructure/bcm49408')

# jtag
dev.add_pin('TDI', 'out')
dev.add_pin('TDO', 'in')
dev.add_pin('TMS', 'out')
dev.add_pin('TCK', 'out')
dev.add_pin('TRST_L', 'out')
# spi ??
dev.add_pin('DBG_CLK', 'out').set_group(1)
dev.add_pin('DBG_EN_N', 'out').set_group(1)
dev.add_pin('DBG_SOUT', 'in').set_group(1)
dev.add_pin('DBG_SIN', 'out').set_group(1)
# serial port
dev.add_pin('UART0_RX', 'out').set_group(2)
dev.add_pin('UART0_TX', 'in').set_group(2)
# system
dev.add_pin('RESET_L', 'out').set_group(3)
# power
dev.add_pin('VDD', 'power_in') # 3.3V target voltage
dev.add_pin('GND', 'power_in')

component.db.add(dev)

#-----------------------------------------------------------------------------
# IDC16 footprint

pin_map = {
  'TDI': (1,),
  'TDO': (3,),
  'TMS': (5,),
  'TCK': (7,),
  'TRST_L': (9,),
  'DBG_CLK': (11,),
  'DBG_EN_N': (12,),
  'DBG_SOUT': (13,),
  'DBG_SIN': (14,),
  'UART0_RX': (15,),
  'UART0_TX': (16,),
  'VDD': (2,),
  'GND': (6,8,10,),
  'RESET_L': (4,),
}

dev.add_footprint('IDC16', pin_map)

#-----------------------------------------------------------------------------
