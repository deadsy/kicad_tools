#-----------------------------------------------------------------------------
"""

Generate Small Outline Integrated Cicuit footprints

"""
#-----------------------------------------------------------------------------

import kicad
import footprint

#-----------------------------------------------------------------------------

class soic(object):

  def __init__(self, name, descr, n, width):
    self.name = name # footprint name
    self.descr = descr # description
    self.n = n # number of pins
    self.width = width # width between pin rows (mm)

  def __str__(self):
    """return the kicad_mod code for this footprint"""
    mod = kicad.mod_module(self.name, self.descr)
    return str(mod)

#-----------------------------------------------------------------------------

footprint.db.add(soic('HTSSOP28', '', 28, kicad.mil2mm(300)))

#-----------------------------------------------------------------------------
