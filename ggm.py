#-----------------------------------------------------------------------------
"""
GooGooMuck Library Files
"""
#-----------------------------------------------------------------------------

import kicad
import footprint

#-----------------------------------------------------------------------------
# components

import components.tlc5940
import components._7404
import components.bcmjtag
import components.ili9341
import components.mb997
import components.rotenc

components = (
  components.tlc5940.dev,
  components._7404.dev,
  components.bcmjtag.dev,
  components.ili9341.dev,
  components.mb997.dev,
  components.rotenc.dev,
)

#-----------------------------------------------------------------------------
# footprints

import footprints.dip
import footprints.qfn
import footprints.soic

#-----------------------------------------------------------------------------

lib_name = 'ggm'

lib = kicad.lib_file(lib_name)
lib.add_components(components)

dcm = kicad.dcm_file(lib_name)
dcm.add_components(components)

mod = footprint.db.values()

#-----------------------------------------------------------------------------
