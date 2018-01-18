#-----------------------------------------------------------------------------
"""

TLC 5940

"""
#-----------------------------------------------------------------------------

import util

#-----------------------------------------------------------------------------

tlc5940 = util.component('TLC5940', '16-Channel LED Driver')
tlc5940.add_tags(('LED', 'PWM'))
tlc5940.set_url('http://www.ti.com/product/TLC5940')

pins = (
  util.pin('VCC', 'power_in'),
  util.pin('GND', 'power_in'),
  util.pin('BLANK', 'in'),
  util.pin('XLAT', 'in'),
  util.pin('SCLK', 'in'),
  util.pin('SIN', 'in'),
  util.pin('VPRG', 'in'),
  util.pin('IREF', 'in'),
  util.pin('DCPRG', 'in'),
  util.pin('GSCLK', 'in'),
  util.pin('SOUT', 'out'),
  util.pin('XERR', 'out'),
  util.pin('OUT0', 'out'),
  util.pin('OUT1', 'out'),
  util.pin('OUT2', 'out'),
  util.pin('OUT3', 'out'),
  util.pin('OUT4', 'out'),
  util.pin('OUT5', 'out'),
  util.pin('OUT6', 'out'),
  util.pin('OUT7', 'out'),
  util.pin('OUT8', 'out'),
  util.pin('OUT9', 'out'),
  util.pin('OUT10', 'out'),
  util.pin('OUT11', 'out'),
  util.pin('OUT12', 'out'),
  util.pin('OUT13', 'out'),
  util.pin('OUT14', 'out'),
  util.pin('OUT15', 'out'),
)

tlc5940.add_pins(pins)

#-----------------------------------------------------------------------------
# PDIP-28 footprint

fp = util.footprint('PDIP-28')

pin_map = {
  'OUT1': (1,),
  'OUT2': (2,),
  'OUT3': (3,),
  'OUT4': (4,),
  'OUT5': (5,),
  'OUT6': (6,),
  'OUT7': (7,),
  'OUT8': (8,),
  'OUT9': (9,),
  'OUT10': (10,),
  'OUT11': (11,),
  'OUT12': (12,),
  'OUT13': (13,),
  'OUT14': (14,),
  'OUT0': (28,),
  'VPRG': (27,),
  'SIN': (26,),
  'SCLK': (25,),
  'XLAT': (24,),
  'BLANK': (23,),
  'GND': (22,),
  'VCC': (21,),
  'IREF': (20,),
  'DCPRG': (19,),
  'GSCLK': (18,),
  'SOUT': (17,),
  'XERR': (16,),
  'OUT15': (15,),
}

fp.set_pin_map(pin_map)
tlc5940.add_footprint(fp)

#-----------------------------------------------------------------------------
# VQFN-32 footprint

fp = util.footprint('VQFN-32')

pin_map = {
  'SCLK': (1,),
  'SIN': (2,),
  'VPRG': (3,),
  'OUT0': (4,),
  'OUT1': (5,),
  'OUT2': (6,),
  'OUT3': (7,),
  'OUT4': (8,),
  'OUT5': (9,),
  'OUT6': (10,),
  'OUT7': (11,),
  'OUT8': (14,),
  'OUT9': (15,),
  'OUT10': (16,),
  'OUT11': (17,),
  'OUT12': (18,),
  'OUT13': (19,),
  'OUT14': (20,),
  'OUT15': (21,),
  'XERR': (22,),
  'SOUT': (23,),
  'GSCLK': (24,),
  'DCPRG': (25,),
  'IREF': (26,),
  'VCC': (27,),
  'GND': (30,),
  'BLANK': (31,),
  'XLAT': (32,),
}

fp.set_pin_map(pin_map)
tlc5940.add_footprint(fp)

#-----------------------------------------------------------------------------
# HTSSOP-28 footprint

fp = util.footprint('HTSSOP-28')

pin_map = {
  'GND': (1,),
  'BLANK': (2,),
  'XLAT': (3,),
  'SCLK': (4,),
  'SIN': (5,),
  'VPRG': (6,),
  'OUT0': (7,),
  'OUT1': (8,),
  'OUT2': (9,),
  'OUT3': (10,),
  'OUT4': (11,),
  'OUT5': (12,),
  'OUT6': (13,),
  'OUT7': (14,),
  'VCC': (28,),
  'IREF': (27,),
  'DCPRG': (26,),
  'GSCLK': (25,),
  'SOUT': (24,),
  'XERR': (23,),
  'OUT15': (22,),
  'OUT14': (21,),
  'OUT13': (20,),
  'OUT12': (19,),
  'OUT11': (18,),
  'OUT10': (17,),
  'OUT9': (16,),
  'OUT8': (15,),
}

fp.set_pin_map(pin_map)
tlc5940.add_footprint(fp)

#-----------------------------------------------------------------------------

print tlc5940.dcm_str()
print tlc5940.lib_str('HTSSOP-28')

#-----------------------------------------------------------------------------
