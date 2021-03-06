#-----------------------------------------------------------------------------
"""

TLC 5940

"""
#-----------------------------------------------------------------------------

import component

#-----------------------------------------------------------------------------

dev = component.component('TLC5940', 'U', '16-Channel LED Driver')
dev.add_tags(('LED', 'PWM'))
dev.set_url('http://www.ti.com/product/TLC5940')

dev.add_pin('VCC', 'power_in')
dev.add_pin('GND', 'power_in')
dev.add_pin('BLANK', 'in')
dev.add_pin('XLAT', 'in')
dev.add_pin('SCLK', 'in')
dev.add_pin('SIN', 'in')
dev.add_pin('VPRG', 'in')
dev.add_pin('IREF', 'in')
dev.add_pin('DCPRG', 'in')
dev.add_pin('GSCLK', 'in')
dev.add_pin('OUT0', 'out')
dev.add_pin('OUT1', 'out')
dev.add_pin('OUT2', 'out')
dev.add_pin('OUT3', 'out')
dev.add_pin('OUT4', 'out')
dev.add_pin('OUT5', 'out')
dev.add_pin('OUT6', 'out')
dev.add_pin('OUT7', 'out')
dev.add_pin('OUT8', 'out')
dev.add_pin('OUT9', 'out')
dev.add_pin('OUT10', 'out')
dev.add_pin('OUT11', 'out')
dev.add_pin('OUT12', 'out')
dev.add_pin('OUT13', 'out')
dev.add_pin('OUT14', 'out')
dev.add_pin('OUT15', 'out')
dev.add_pin('SOUT', 'out').set_group(1)
dev.add_pin('XERR', 'out').set_group(1)

component.db.add(dev)

#-----------------------------------------------------------------------------
# DIP28 footprint

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

dev.add_footprint('DIP28', pin_map)

#-----------------------------------------------------------------------------
# VQFN32 footprint

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

dev.add_footprint('VQFN32', pin_map)

#-----------------------------------------------------------------------------
# HTSSOP28 footprint

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

dev.add_footprint('HTSSOP28', pin_map)

#-----------------------------------------------------------------------------
