#-----------------------------------------------------------------------------
"""

KiCAD Library Objects

"""
#-----------------------------------------------------------------------------

class sch_pin(object):
  """schematic pin"""

  def __init__(self, pin, name):
    self.pin = pin
    self.name = name
    self.length = 50
    self.orientation = None
    self.sizenum = 50
    self.sizename = 50
    self.part = 1
    self.dmg = 1
    self.type = 'P'
    self.shape = None

  def set_xy(self, x, y):
    """set the x,y coordinate"""
    self.x = x
    self.y = y

  def set_orientation(self, o):
    """set the pin orientation"""
    o_vals = (
      'L', # left
      'R', # right
      'U', # up
      'D' # down
      )
    assert o in o_vals, 'bad pin orientation %s' % t
    self.orientation = o

  def set_type(self, t):
    t_vals = (
      'I', # Input
      'O', # Output
      'B', # Bidirectional
      'T', # Tristate
      'P', # Passive
      'C', # Open Collector
      'E', # Open Emitter
      'N', # Non-connected
      'U', # Unspecified
      'W', # Power input
      'w', # Power output
      )
    assert t in t_vals, 'bad pin type %s' % t
    self.type = t

  def set_length(self, l):
    self.length = l

  def __str__(self):
    # X name pin X Y length orientation sizenum sizename part dmg type shape
    s = []
    s.append('X')
    s.append(self.name)
    s.append(self.pin)
    s.append('%d %d' % (self.x,self.y))
    s.append('%d' % self.length)
    s.append(self.orientation)
    s.append('%d' % self.sizenum)
    s.append('%d' % self.sizename)
    s.append('%d' % self.part)
    s.append('%d' % self.dmg)
    s.append(self.type)
    #self.shape
    return ' '.join(s)

#-----------------------------------------------------------------------------

class sch_rect(object):
  def __init__(self):
    self.x1
    self.y1
    self.x2
    self.y2
    self.part = 0
    self.dmg = 0
    self.pen = 0
    self.fill = 'N'

  def __str__(self):
    # S X1 Y1 X2 Y2 part dmg pen fill
    s = []
    s.append('S')
    s.append('%d %d %d %d' % (self.x1,self.y1, self.x2, self.y2))
    s.append('%d' % self.part)
    s.append('%d' % self.dmg)
    s.append('%d' % self.pen)
    s.append(self.fill)
    return ' '.join(s)

#-----------------------------------------------------------------------------

class sch_component(object):

  def __init__(self, name):
    self.name = name
    self.pins = []

  def add_pin(self, p):
    self.pins.append(p)

  def emit_head(self):
    s = []
    s.append('#\n# %s\n#' % self.name)
    s.append('DEF') # TODO
    s.append('F0') # TODO
    s.append('F1') # TODO
    s.append('F2') # TODO
    s.append('F3') # TODO
    return '\n'.join(s)

  def emit_tail(self):
    s = []
    s.append('ENDDEF')
    s.append('#')
    return '\n'.join(s)

  def emit_draw(self):
    s = []
    s.append('DRAW')
    s.extend([str(p) for p in self.pins])
    s.append('ENDDRAW')
    return '\n'.join(s)

  def __str__(self):
    s = []
    s.append(self.emit_head())
    s.append(self.emit_draw())
    s.append(self.emit_tail())
    return '\n'.join(s)

#-----------------------------------------------------------------------------

class sch_lib(object):
  """schematic library"""

  def __init__(self, name):
    self.name = name
    self.components = []

  def add_component(self, c):
    self.components.append(c)

  def emit_head(self):
    s = []
    s.append('EESchema-LIBRARY Version 2.3')
    s.append('#encoding utf-8')
    return '\n'.join(s)

  def emit_tail(self):
    s = []
    s.append('#End Library')
    return '\n'.join(s)

  def __str__(self):
    s = []
    s.append(self.emit_head())
    s.extend([str(c) for c in self.components])
    s.append(self.emit_tail())
    return '\n'.join(s)

#-----------------------------------------------------------------------------
