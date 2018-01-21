#-----------------------------------------------------------------------------
"""

Footprint Functions

"""
#-----------------------------------------------------------------------------

class footprint_database():

  def __init__(self):
    self.footprints = {}

  def lookup(self, name):
    """lookup a footprint by name"""
    return self.footprints[name]

  def add(self, fp):
    """add a footprint to the database"""
    assert self.footprints.has_key(fp.name) is False, 'footprint database already has this name'
    self.footprints[fp.name] = fp

db = footprint_database()

#-----------------------------------------------------------------------------


