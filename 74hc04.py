#-----------------------------------------------------------------------------
"""

74HC04

"""
#-----------------------------------------------------------------------------

import util

#-----------------------------------------------------------------------------

dev = util.component('74HC04', 'Hex Inverter')
dev.add_tags(('Inverter',))
dev.set_url('http://www.ti.com/lit/ds/symlink/sn74ahcu04-ep.pdf')

pins = (
  util.pin('1A', 'in', unit=1),
  util.pin('1Y', 'out', unit=1),
  util.pin('2A', 'in', unit=2),
  util.pin('2Y', 'out', unit=2),
  util.pin('3A', 'in', unit=3),
  util.pin('3Y', 'out', unit=3),
  util.pin('GND', 'power_in'),
  util.pin('VCC', 'power_in'),
  util.pin('6A', 'in', unit=6),
  util.pin('6Y', 'out', unit=6),
  util.pin('5A', 'in', unit=5),
  util.pin('5Y', 'out', unit=5),
  util.pin('4A', 'in', unit=4),
  util.pin('4Y', 'out', unit=4),
)

dev.add_pins(pins)

#-----------------------------------------------------------------------------
# DIP-14 footprint

fp = util.footprint('DIP-14')

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

fp.set_pin_map(pin_map)
dev.add_footprint(fp)

#-----------------------------------------------------------------------------

print dev.dcm_str()
print dev.lib_str('DIP-14')

#-----------------------------------------------------------------------------
