#-----------------------------------------------------------------------------
"""

TLC 5940

"""
#-----------------------------------------------------------------------------

from util import *

#-----------------------------------------------------------------------------

tlc5940 = component('TLC5940', '16-Channel LED Driver')
tlc5940.add_tags(('LED', 'PWM'))
tlc5940.set_url('http://www.ti.com/product/TLC5940')

#-----------------------------------------------------------------------------

pins = (
  pin('VCC', 'power_in'),
  pin('GND', 'power_in'),
  pin('BLANK', 'in'),
  pin('XLAT', 'in'),
  pin('SCLK', 'in'),
  pin('SIN', 'in'),
  pin('VPRG', 'in'),
  pin('IREF', 'in'),
  pin('DCPRG', 'in'),
  pin('GSCLK', 'in'),
  pin('SOUT', 'out'),
  pin('XERR', 'out'),
  pin('OUT0', 'out'),
  pin('OUT1', 'out'),
  pin('OUT2', 'out'),
  pin('OUT3', 'out'),
  pin('OUT4', 'out'),
  pin('OUT5', 'out'),
  pin('OUT6', 'out'),
  pin('OUT7', 'out'),
  pin('OUT8', 'out'),
  pin('OUT9', 'out'),
  pin('OUT10', 'out'),
  pin('OUT11', 'out'),
  pin('OUT12', 'out'),
  pin('OUT13', 'out'),
  pin('OUT14', 'out'),
  pin('OUT15', 'out'),
)

tlc5940.add_pins(pins)

#-----------------------------------------------------------------------------
# dip28 footprint

dip28 = footprint('DIP28')

pin_map = {
  'VCC': (1,),
  'GND': (2,),
  'BLANK': (3,),
  'XLAT': (4,),
  'SCLK': (5,),
  'SIN': (6,),
  'VPRG': (7,),
  'IREF': (8,),
  'DCPRG': (9,),
  'GSCLK': (10,),
  'SOUT': (11,),
  'XERR': (12,),
  'OUT0': (13,),
  'OUT1': (14,),
  'OUT2': (15,),
  'OUT3': (16,),
  'OUT4': (17,),
  'OUT5': (18,),
  'OUT6': (19,),
  'OUT7': (20,),
  'OUT8': (21,),
  'OUT9': (22,),
  'OUT10': (23,),
  'OUT11': (24,),
  'OUT12': (25,),
  'OUT13': (26,),
  'OUT14': (27,),
  'OUT15': (28,),
}

dip28.set_pin_map(pin_map)
tlc5940.add_footprint(dip28)

#-----------------------------------------------------------------------------

print tlc5940.dcm_str()

#-----------------------------------------------------------------------------
