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
    self.x = 0
    self.y = 0

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
    assert o in o_vals, 'bad pin orientation %s' % o
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
    s.append('%d %d' % (self.x, self.y))
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
  def __init__(self, w, h):
    self.x1 = -w/2
    self.y1 = -h/2
    self.x2 = w/2
    self.y2 = h/2
    self.part = 0
    self.dmg = 0
    self.pen = 0
    self.fill = 'N'

  def set_xy(self, x, y):
    self.x1 = x
    self.y1 = y

  def offset(self, x, y):
    self.x1 += x
    self.y1 += y
    self.x2 += x
    self.y2 += y

  def set_size(self, w, h):
    self.x2 = self.x1 + w
    self.y2 = self.y1 + h

  def __str__(self):
    # S X1 Y1 X2 Y2 part dmg pen fill
    s = []
    s.append('S')
    s.append('%d %d %d %d' % (self.x1, self.y1, self.x2, self.y2))
    s.append('%d' % self.part)
    s.append('%d' % self.dmg)
    s.append('%d' % self.pen)
    s.append(self.fill)
    return ' '.join(s)

#-----------------------------------------------------------------------------

class sch_text(object):
  """schematic text"""

  def __init__(self, text):
    self.text = text
    self.size = 50
    self.orientation = 'H'
    self.visible = len(self.text) != 0
    self.halign = 'C'
    self.valign = 'C'
    self.italic = False
    self.bold = False
    self.x = 0
    self.y = 0

  def set_xy(self, x, y):
    self.x = x
    self.y = y

  def set_orientation(self, o):
    """set the text orientation"""
    o_vals = (
      'H', # horizontal
      'V', # vertical
      )
    assert o in o_vals, 'bad text orientation %s' % o
    self.orientation = o

  def __str__(self):
    s = []
    s.append('"%s"' % self.text)
    s.append('%d %d' % (self.x, self.y))
    s.append('%d' % self.size)
    s.append(self.orientation)
    s.append(('I', 'V')[self.visible])
    s.append(self.halign)
    s.append('%s%s%s' % (self.valign, ('N', 'I')[self.italic], ('N', 'B')[self.bold]))
    return ' '.join(s)

#-----------------------------------------------------------------------------

class sch_unit(object):
  """schematic unit"""

  def __init__(self):
    self.pins = []
    self.shapes = []

  def add_pin(self, p):
    self.pins.append(p)

  def add_shape(self, s):
    self.shapes.append(s)

#-----------------------------------------------------------------------------

class sch_component(object):

  def __init__(self, name, ref):
    self.name = name
    self.ref = ref
    self.ofs = 50
    self.pin_names = True
    self.pin_numbers = True
    self.nparts = 1
    self.locked = False
    self.power = False
    self.pins = []
    self.shapes = []
    self.text = (
      sch_text(self.ref), # F0 reference
      sch_text(self.name), # F1 component name
      sch_text(""), # F2 footprint name
      sch_text(""), # F3 relative path to datasheet
    )

  def add_pin(self, p):
    self.pins.append(p)

  def add_shape(self, s):
    self.shapes.append(s)

  def emit_def(self):
    s = []
    s.append('DEF')
    s.append(self.name)
    s.append(self.ref)
    s.append('0') # always 0
    s.append('%d' % self.ofs)
    s.append(('N', 'Y')[self.pin_numbers])
    s.append(('N', 'Y')[self.pin_names])
    s.append('%d' % self.nparts)
    s.append(('F', 'L')[self.locked])
    s.append(('N', 'P')[self.power])
    return ' '.join(s)

  def emit_head(self):
    s = []
    s.append('#\n# %s\n#' % self.name)
    s.append(self.emit_def())
    s.extend(['F%d %s' % (i, self.text[i]) for i in range(len(self.text))])
    return '\n'.join(s)

  def emit_tail(self):
    s = []
    s.append('ENDDEF')
    s.append('#')
    return '\n'.join(s)

  def emit_draw(self):
    s = []
    s.append('DRAW')
    s.extend([str(x) for x in self.shapes])
    s.extend([str(x) for x in self.pins])
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

class doc_component(object):
  """documentation component"""

  def __init__(self, name, descr):
    self.name = name
    self.description = descr
    self.keywords = []

  def add_keywords(self, k):
    self.keywords.extend(k)

  def __str__(self):
    s = []
    s.append('#\n$CMP %s' % self.name)
    s.append('D %s' % self.description)
    s.append('K %s' % ' '.join([x for x in self.keywords]))
    s.append('$ENDCMP')
    return '\n'.join(s)

#-----------------------------------------------------------------------------

class doc_lib(object):
  """documentation library"""

  def __init__(self, name):
    self.name = name
    self.components = []

  def add_component(self, c):
    self.components.append(c)

  def emit_head(self):
    s = []
    s.append('EESchema-DOCLIB  Version 2.0')
    return '\n'.join(s)

  def emit_tail(self):
    s = []
    s.append('#\n#End Doc Library')
    return '\n'.join(s)

  def __str__(self):
    s = []
    s.append(self.emit_head())
    s.extend([str(x) for x in self.components])
    s.append(self.emit_tail())
    return '\n'.join(s)

#-----------------------------------------------------------------------------
