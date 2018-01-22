#-----------------------------------------------------------------------------
"""

Generate Quad Flat No Lead footprints

"""
#-----------------------------------------------------------------------------

import kicad
import footprint

#-----------------------------------------------------------------------------

class qfn(object):

  def __init__(self, name, descr, n):
    self.name = name # footprint name
    self.descr = descr # description
    self.n = n # number of pins

  def __str__(self):
    """return the kicad_mod code for this footprint"""
    mod = kicad.mod_module(self.name, self.descr)
    return str(mod)

#-----------------------------------------------------------------------------

footprint.db.add(qfn('VQFN32', '', 32))

#-----------------------------------------------------------------------------
