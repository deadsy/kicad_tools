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

pins = (
  component.pin('1A', 'in', unit=1),
  component.pin('1Y', 'out', unit=1),
  component.pin('2A', 'in', unit=2),
  component.pin('2Y', 'out', unit=2),
  component.pin('3A', 'in', unit=3),
  component.pin('3Y', 'out', unit=3),
  component.pin('GND', 'power_in'),
  component.pin('VCC', 'power_in'),
  component.pin('6A', 'in', unit=6),
  component.pin('6Y', 'out', unit=6),
  component.pin('5A', 'in', unit=5),
  component.pin('5Y', 'out', unit=5),
  component.pin('4A', 'in', unit=4),
  component.pin('4Y', 'out', unit=4),
)

dev.add_pins(pins)
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
