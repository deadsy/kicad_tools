#-----------------------------------------------------------------------------
"""

Generate Dual In Place footprints

"""
#-----------------------------------------------------------------------------

import kicad
import footprint

#-----------------------------------------------------------------------------

class dip():

  def __init__(self, name, n, width):
    self.name = name # footprint name
    self.n = n # number of pins
    self.width = width # width between pin rows (mm)

#-----------------------------------------------------------------------------

footprint.db.add(dip('DIP28', 28, kicad.mil2mm(300)))
footprint.db.add(dip('DIP14', 14, kicad.mil2mm(300)))

#-----------------------------------------------------------------------------
