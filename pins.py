#-----------------------------------------------------------------------------
"""

Component Pins

"""
#-----------------------------------------------------------------------------

class pinset(object):

  def __init__(self):
    self.units = []

  def add_unit(self, u):
    self.units.append(u)

class unit(object):

  def __init__(self):
    self.groups = []

  def add_group(self, g):
    self.groups.append(g)

class group(object):

  def __init__(self, align):
    assert align in ('L','R','T','B'), 'bad alignment %s' % align
    self.align = align
    self.pins = []

  def add_pin(self, p)
    self.pins.append(p)

class pin(object):

  def __init__(self, number, name, ptype):
    self.number = number
    self.name = name
    self.ptype = ptype


#-----------------------------------------------------------------------------

