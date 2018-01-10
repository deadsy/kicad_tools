#-----------------------------------------------------------------------------
"""
GooGooMuck Library Files
"""
#-----------------------------------------------------------------------------

import kicad
import mb997
import ili9341

lib = kicad.lib_file('ggm')
lib.add_component(mb997.lib)
lib.add_component(ili9341.lib)

dcm = kicad.dcm_file('ggm')
dcm.add_component(mb997.dcm)
dcm.add_component(ili9341.dcm)

mod = kicad.mod_files('ggm')
mod.add_module(mb997.mod)
mod.add_module(ili9341.mod)

#-----------------------------------------------------------------------------
