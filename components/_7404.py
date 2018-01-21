#-----------------------------------------------------------------------------
"""

74HC04

"""
#-----------------------------------------------------------------------------

from component import *

#-----------------------------------------------------------------------------

dev = component('74HC04', 'U', 'Hex Inverter')
dev.add_tags(('Inverter',))
dev.set_url('http://www.ti.com/lit/ds/symlink/sn74ahcu04-ep.pdf')

pins = (
  pin('1A', 'in', unit=1),
  pin('1Y', 'out', unit=1),
  pin('2A', 'in', unit=2),
  pin('2Y', 'out', unit=2),
  pin('3A', 'in', unit=3),
  pin('3Y', 'out', unit=3),
  pin('GND', 'power_in'),
  pin('VCC', 'power_in'),
  pin('6A', 'in', unit=6),
  pin('6Y', 'out', unit=6),
  pin('5A', 'in', unit=5),
  pin('5Y', 'out', unit=5),
  pin('4A', 'in', unit=4),
  pin('4Y', 'out', unit=4),
)

dev.add_pins(pins)

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
