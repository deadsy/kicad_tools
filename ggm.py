#-----------------------------------------------------------------------------
"""
GooGooMuck Library Files
"""
#-----------------------------------------------------------------------------

import kicad

#-----------------------------------------------------------------------------
# components

import components.tlc5940
import components._7404

components = (
  components.tlc5940.dev,
  components._7404.dev,
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


#mod = kicad.mod_files(lib_name)
#dcm.add_components(components)


#-----------------------------------------------------------------------------
