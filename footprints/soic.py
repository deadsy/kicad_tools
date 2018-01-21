#-----------------------------------------------------------------------------
"""

Generate Small Outline Integrated Cicuit footprints

"""
#-----------------------------------------------------------------------------

import kicad
import footprint

#-----------------------------------------------------------------------------

class soic():

  def __init__(self, name, n, width):
    self.name = name # footprint name
    self.n = n # number of pins
    self.width = width # width between pin rows (mm)

#-----------------------------------------------------------------------------

footprint.db.add(soic('HTSSOP28', 28, kicad.mil2mm(300)))

#-----------------------------------------------------------------------------
