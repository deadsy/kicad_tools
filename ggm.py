#-----------------------------------------------------------------------------
"""
GooGooMuck Component Library
"""
#-----------------------------------------------------------------------------

import kicad
import mb997
import ili9341

lib = kicad.sch_lib('ggm')
lib.add_component(mb997.lib)
lib.add_component(ili9341.lib)

dcm = kicad.doc_lib('ggm')
dcm.add_component(mb997.dcm)
dcm.add_component(ili9341.dcm)

#-----------------------------------------------------------------------------
