#-----------------------------------------------------------------------------
"""
GooGooMuck Library Files
"""
#-----------------------------------------------------------------------------

import kicad
import footprint
import component

#-----------------------------------------------------------------------------
# components

import components.tlc5940
import components._7404
import components.bcmjtag
import components.ili9341
import components.mb997
import components.rotenc

#-----------------------------------------------------------------------------
# footprints

import footprints.dip
import footprints.qfn
import footprints.soic

#-----------------------------------------------------------------------------

lib_name = 'ggm'

lib = kicad.lib_file(lib_name)
lib.add_components(component.db.values())

dcm = kicad.dcm_file(lib_name)
dcm.add_components(component.db.values())

mod = footprint.db.values()

#-----------------------------------------------------------------------------
