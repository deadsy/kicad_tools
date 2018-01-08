#-----------------------------------------------------------------------------
"""
GooGooMuck Component Library
"""
#-----------------------------------------------------------------------------

import kicad
import mb997

lib = kicad.sch_lib('ggm')
lib.add_component(mb997.lib)

dcm = kicad.doc_lib('ggm')
dcm.add_component(mb997.dcm)

#-----------------------------------------------------------------------------
