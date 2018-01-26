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

pins = (
  # jtag
  component.pin('TDI', 'out'),
  component.pin('TDO', 'in'),
  component.pin('TMS', 'out'),
  component.pin('TCK', 'out'),
  component.pin('TRST_L', 'out'),

  component.pin('DBG_CLK', 'out', group=1),
  component.pin('DBG_EN_N', 'out', group=1),
  component.pin('DBG_SOUT', 'in', group=1),
  component.pin('DBG_SIN', 'out', group=1),
  # serial port
  component.pin('UART0_RX', 'out', group=2),
  component.pin('UART0_TX', 'in', group=2),
  # system
  component.pin('RESET_L', 'out', group=3),
  # power
  component.pin('VDD', 'power_in'), # 3.3V target voltage
  component.pin('GND', 'power_in'),
)

dev.add_pins(pins)
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
