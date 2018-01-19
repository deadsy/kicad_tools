#-----------------------------------------------------------------------------
"""
GooGooMuck Library Files
"""
#-----------------------------------------------------------------------------

import kicad

#-----------------------------------------------------------------------------

import components.tlc5940
import components._7404

components = (
  components.tlc5940.dev,
  components._7404.dev,
)

#-----------------------------------------------------------------------------

lib = kicad.lib_file('ggm')
lib.add_components(components)

dcm = kicad.dcm_file('ggm')
dcm.add_components(components)

mod = kicad.mod_files('ggm')

#-----------------------------------------------------------------------------
