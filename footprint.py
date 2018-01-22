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
    assert self.footprints.has_key(name), 'footprint %s not found' % name
    return self.footprints[name]

  def values(self):
    return self.footprints.values()

  def add(self, fp):
    """add a footprint to the database"""
    assert self.footprints.has_key(fp.name) is False, 'footprint database already has %s' % fp.name
    self.footprints[fp.name] = fp

db = footprint_database()

#-----------------------------------------------------------------------------


