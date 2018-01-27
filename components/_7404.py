#-----------------------------------------------------------------------------
"""

74HC04

"""
#-----------------------------------------------------------------------------

import component

#-----------------------------------------------------------------------------

dev = component.component('74HC04', 'U', 'Hex Inverter')
dev.add_tags(('Inverter',))
dev.set_url('http://www.ti.com/lit/ds/symlink/sn74ahcu04-ep.pdf')

dev.add_pin('1A', 'in').set_unit(1)
dev.add_pin('1Y', 'out').set_unit(1)
dev.add_pin('2A', 'in').set_unit(2)
dev.add_pin('2Y', 'out').set_unit(2)
dev.add_pin('3A', 'in').set_unit(3)
dev.add_pin('3Y', 'out').set_unit(3)
dev.add_pin('GND', 'power_in')
dev.add_pin('VCC', 'power_in')
dev.add_pin('6A', 'in').set_unit(6)
dev.add_pin('6Y', 'out').set_unit(6)
dev.add_pin('5A', 'in').set_unit(5)
dev.add_pin('5Y', 'out').set_unit(5)
dev.add_pin('4A', 'in').set_unit(4)
dev.add_pin('4Y', 'out').set_unit(4)

component.db.add(dev)

#-----------------------------------------------------------------------------
# DIP-14 footprint

pin_map = {
  '1A': (1,),
  '1Y': (2,),
  '2A': (3,),
  '2Y': (4,),
  '3A': (5,),
  '3Y': (6,),
  'GND': (7,),
  'VCC': (14,),
  '6A': (13,),
  '6Y': (12,),
  '5A': (11,),
  '5Y': (10,),
  '4A': (9,),
  '4Y': (8,),
}

dev.add_footprint('DIP14', pin_map)

#-----------------------------------------------------------------------------
