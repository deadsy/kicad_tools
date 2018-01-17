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

#-----------------------------------------------------------------------------


g0 = util.pin_group('T')
g0.add_pin('VCC', 'power_in')

g1 = util.pin_group('B')
g1.add_pin('GND', 'power_in')

g2 = util.pin_group('L')
g2.add_pin('BLANK', 'in')
g2.add_pin('XLAT', 'in')
g2.add_pin('SCLK', 'in')
g2.add_pin('SIN', 'in')
g2.add_pin('VPRG', 'in')
g2.add_pin('IREF', 'in')
g2.add_pin('DCPRG', 'in')
g2.add_pin('GSCLK', 'in')

g3 = util.pin_group('R')

 util.pin('SOUT', 'out')
 util.pin('XERR', 'out')

 util.pin('OUT0', 'out')
 util.pin('OUT1', 'out')
 util.pin('OUT2', 'out')
 util.pin('OUT3', 'out')
 util.pin('OUT4', 'out')
 util.pin('OUT5', 'out')
 util.pin('OUT6', 'out')
 util.pin('OUT7', 'out')
 util.pin('OUT8', 'out')
 util.pin('OUT9', 'out')
 util.pin('OUT10', 'out')
 util.pin('OUT11', 'out')
 util.pin('OUT12', 'out')
 util.pin('OUT13', 'out')
 util.pin('OUT14', 'out')
 util.pin('OUT15', 'out')

#-----------------------------------------------------------------------------

print tlc5940.dcm_str()

#-----------------------------------------------------------------------------
