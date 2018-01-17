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
  'IREF': (1,),
  'DCPRG': (1,2,),
  'GSCLK': (1,),
  'SOUT': (1,),
  'XERR': (1,),
  'OUT0': (1,),
  'OUT1': (1,),
  'OUT2': (1,),
  'OUT3': (1,),
  'OUT4': (1,),
  'OUT5': (1,),
  'OUT6': (1,),
  'OUT7': (1,),
  'OUT8': (1,),
  'OUT9': (1,),
  'OUT10': (1,),
  'OUT11': (1,),
  'OUT12': (1,),
  'OUT13': (1,),
  'OUT14': (1,),
  'OUT15': (1,),
}

dip28.set_pin_map(pin_map)
tlc5940.add_footprint(dip28)

#-----------------------------------------------------------------------------

print tlc5940.dcm_str()

#-----------------------------------------------------------------------------
