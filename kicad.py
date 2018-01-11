#-----------------------------------------------------------------------------
"""

KiCAD Objects

lib - schematic symbols
dcm - part information
mod - part pcb footprint

"""
#-----------------------------------------------------------------------------

import time

#-----------------------------------------------------------------------------

def indent(s):
  items = s.split('\n')
  for i, _ in enumerate(items):
    items[i] = '  %s' % items[i]
  return '\n'.join(items)

MM_PER_INCH = 25.4

def mil2mm(mil):
  return MM_PER_INCH * (mil / 1000.0)

def tedit_secs():
  """return number of seconds since 1970/1/1"""
  return int(time.time())

#-----------------------------------------------------------------------------

class mod_at(object):
  """footprint at element"""

  def __init__(self, x=0.0, y=0.0, a=0.0):
    self.x = x
    self.y = y
    self.a = a

  def ofs_xy(self, xofs, yofs):
    """offset the xy position"""
    self.x += float(xofs)
    self.y += float(yofs)

  def __str__(self):
    if self.a == 0:
      return '(at %.2f %.2f)' % (self.x, self.y)
    else:
      return '(at %.2f %.2f %.2f)' % (self.x, self.y, self.a)

#-----------------------------------------------------------------------------

class mod_size(object):
  """footprint size element"""

  def __init__(self, w=0.0, h=0.0):
    self.w = w
    self.h = h

  def __str__(self):
    return '(size %.2f %.2f)' % (self.w, self.h)

#-----------------------------------------------------------------------------

class mod_width(object):
  """footprint width element"""

  def __init__(self, w=0.0):
    self.w = w

  def __str__(self):
    return '(width %.2f)' % self.w

#-----------------------------------------------------------------------------

class mod_xy(object):
  """footprint xy element"""

  def __init__(self, x=0.0, y=0.0):
    self.x = x
    self.y = y

  def __str__(self):
    return '(xy %.2f %.2f)' % (self.x, self.y)

#-----------------------------------------------------------------------------

class mod_pts(object):
  """footprint pts (points) element"""

  def __init__(self, points=None):
    self.points = points

  def __str__(self):
    assert self.points is not None and len(self.points) != 0, 'no points in points list'
    return '(pts %s)' % ''.join([str(x) for x in self.points])

#-----------------------------------------------------------------------------

class mod_rect_delta(object):
  """footprint rect_delta"""

  def __init__(self, dx=0.0, dy=0.0):
    self.dx = dx
    self.dy = dy

  def __str__(self):
    return '(rect_delta %.2f %.2f)' % (self.dy, self.dx)

#-----------------------------------------------------------------------------

class mod_drill(object):
  """footprint drill"""

  def __init__(self, size=0.0, xofs=0.0, yofs=0.0):
    self.size = size
    self.xofs = xofs
    self.yofs = yofs

  def __str__(self):
    if (self.xofs != 0.0) or (self.yofs != 0.0):
      return '(drill %.2f (offset %.2f %.2f))' % (self.size, self.xofs, self.yofs)
    else:
      return '(drill %.2f)' % self.size

#-----------------------------------------------------------------------------

layer_types = (
  'Cu', # copper
  'Paste', # solder paste
  'Adhes', # adhesive
  'SilkS', # silkscreen
  'Mask', # solder mask
  'CrtYd', # courtyard
  'Fab', # fabrication
)

layer_names = (
  '*', # all
  'F', # front
  'B', # back
)

class mod_layer(object):
  """single footprint layer"""

  def __init__(self, layer=None):
    self.layer = layer

  def __str__(self):
    assert self.layer is not None, 'no layer defined'
    return '(layer %s)' % self.layer

class mod_layers(object):
  """list of footprint layers"""

  def __init__(self, layers=None):
    self.layers = layers

  def __str__(self):
    assert self.layers is not None, 'no layers defined'
    return '(layers %s)' % ' '.join([x for x in self.layers])

#-----------------------------------------------------------------------------

ptypes = ('thru_hole', 'smd', 'connect', 'np_thru_hole')
pshapes = ('circle', 'rect', 'oval', 'trapezoid')

class mod_pad(object):
  """footprint pad"""

  def __init__(self, name, ptype='smd', shape='rect'):
    assert ptype in ptypes, 'bad pad type %s' % ptype
    assert shape in pshapes, 'bad pad shape %s' % shape
    self.name = name # pin number or name (string)
    self.ptype = ptype # pad type
    self.shape = shape
    self.at = mod_at()
    self.size = mod_size()
    self.rect_delta = mod_rect_delta()
    self.drill = mod_drill()
    if self.ptype in ('thru_hole', 'np_thru_hole'):
      self.layers = mod_layers(('*.Cu', '*.Mask', 'F.SilkS'))
    else:
      self.layers = mod_layers(('F.Cu', 'F.Paste', 'F.Mask'))
    # TODO
    # drill oval
    # die_length
    # solder_mask
    # clearance
    # solder_paste
    # solder_paste_margin_ratio
    # zone_connect
    # thermal_width
    # thermal_gap

  def __str__(self):
    s = []
    s.append('%s' % self.name)
    s.append('%s' % self.ptype)
    s.append('%s' % self.shape)
    s.append(str(self.at))
    s.append(str(self.size))
    if self.shape == 'trapezoid':
      s.append(str(self.rect_delta))
    if self.ptype in ('thru_hole', 'np_thru_hole'):
      s.append(str(self.drill))
    s.append(str(self.layers))
    return '(pad %s)' % ' '.join(s)

#-----------------------------------------------------------------------------

class mod_font(object):

  def __init__(self):
    self.size = mod_size(1.0, 1.0)
    self.thickness = 0.15

  def __str__(self):
    return '(font %s (thickness %.2f))' % (self.size, self.thickness)

#-----------------------------------------------------------------------------

class mod_effects(object):

  def __init__(self):
    self.font = mod_font()

  def __str__(self):
    s = []
    s.append(str(self.font))
    return '(effects %s)' % ' '.join(s)

#-----------------------------------------------------------------------------

ttypes = ('reference', 'value', 'user')

class mod_text(object):
  """footprint fp_text element"""

  def __init__(self, text, ttype):
    assert ttype in ttypes, 'bad ttype %s' % ttype
    self.text = text
    self.ttype = ttype
    self.at = mod_at()
    self.layer = 'F.SilkS'
    self.effects = mod_effects()

  def ofs_xy(self, xofs, yofs):
    """offset the xy position"""
    self.at.ofs_xy(xofs, yofs)
    return self

  def set_layer(self, l):
    assert l in ('F.SilkS', 'F.Fab'), 'bad layer type %s' % l
    self.layer = l
    return self

  def __str__(self):
    s = []
    s.append('(fp_text %s %s %s (layer %s)' % (self.ttype, self.text, self.at, self.layer))
    s.append(indent(str(self.effects)))
    s.append(')')
    return '\n'.join(s)

#-----------------------------------------------------------------------------

class mod_poly(object):
  """footprint fp_poly element"""

  def __init__(self):
    self.pts = mod_pts()
    self.layer = mod_layer()
    self.width = mod_width()

  def __str__(self):
    s = []
    s.append('(fp_poly')
    s.append(str(self.pts))
    s.append(str(self.layer))
    s.append(str(self.width))
    s.append(')')
    return '\n'.join(s)

#-----------------------------------------------------------------------------

class mod_module(object):
  """footprint module"""

  def __init__(self, name, descr):
    self.name = name
    self.descr = descr
    self.pads = []
    self.tags = []
    self.shapes = []
    self.layer = 'F.Cu'
    self.attr = None
    # TODO
    # locked
    # autoplace_cost90
    # autoplace_cost180
    # solder_mask_margin
    # solder_paste_margin
    # solder_paste_margin_ratio
    # clearance
    # zone_connect
    # thermal_width
    # thermal_gap
    # fp_line
    # fp_circle
    # fp_arc
    # fp_poly
    # fp_curve
    # model

  def add_tags(self, t):
    self.tags.extend(t)

  def add_pad(self, p):
    if p.ptype == 'smd':
      self.attr = 'smd'
    self.pads.append(p)

  def add_shape(self, s):
    self.shapes.append(s)

  def tags_str(self):
    return '"%s"' % ' '.join([str(x) for x in self.tags])

  def __str__(self):
    s = []
    s.append('(module %s (layer %s) (tedit %X)' % (self.name, self.layer, tedit_secs()))
    s.append(indent('(descr "%s")' % self.descr))
    s.append(indent('(tags %s)' % self.tags_str()))
    if self.attr:
      s.append(indent('(attr %s)' % self.attr))
    s.extend([indent(str(x)) for x in self.shapes])
    s.extend([indent(str(x)) for x in self.pads])
    s.append(')\n')
    return '\n'.join(s)

#-----------------------------------------------------------------------------

class mod_files(object):

  def __init__(self, name):
    self.name = name
    self.modules = []

  def add_module(self, m):
    self.modules.append(m)

#-----------------------------------------------------------------------------

class lib_pin(object):
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
    self.shape = ''
    self.visible = ''
    self.x = 0
    self.y = 0

  def set_part(self, p):
    """set the part number"""
    self.part = p

  def ofs_xy(self, xofs, yofs):
    """offset the xy position"""
    self.x += xofs
    self.y += yofs
    return self

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
    """set the pin type"""
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
    if self.type == 'N':
      self.set_visible(False)
      self.set_shape('')

  def set_shape(self, s):
    """set the pin shape"""
    s_vals = (
      '', # line
      'I', # inverted
      'C', # clock
      'L', # input low
      'V', # output low
    )
    assert s in s_vals, 'bad pin shape %s' % s
    self.shape = s

  def set_visible(self, v):
    """set the pin as visible/invisible"""
    self.visible = ('N', '')[v]

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
    s.append('%s%s' % (self.visible, self.shape))
    return ' '.join(s)

#-----------------------------------------------------------------------------

class lib_rect(object):
  """schematic rectangle"""

  def __init__(self, w, h):
    self.x1 = -w/2
    self.y1 = -h/2
    self.x2 = w/2
    self.y2 = h/2
    self.part = 0
    self.dmg = 0
    self.pen = 10
    self.fill = 'f'

  def set_part(self, p):
    """set the part number"""
    self.part = p

  def set_fill(self, f):
    f_vals = (
      'f', # background
      'F', # pen color
      'N', # transparent
    )
    assert f in f_vals, 'bad fill value %s' % f
    self.fill = f

  def ofs_xy(self, xofs, yofs):
    """offset the xy position"""
    self.x1 += xofs
    self.y1 += yofs
    self.x2 += xofs
    self.y2 += yofs
    return self

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

class lib_text(object):
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

  def set_text(self, t):
    """set the text field"""
    self.text = t
    return self

  def set_halign(self, a):
    """set horizontal alignment"""
    assert a in ('C', 'L', 'R'), 'bad horizontal alignment %s' % a
    self.halign = a
    return self

  def set_valign(self, a):
    """set vertical alignment"""
    assert a in ('C', 'T', 'B'), 'bad vertical alignment %s' % a
    self.valign = a
    return self

  def set_tl(self):
    """set the text origin to the top left point"""
    self.valign = 'T'
    self.halign = 'L'
    return self

  def set_bl(self):
    """set the text origin to the bottom left point"""
    self.valign = 'B'
    self.halign = 'L'
    return self

  def ofs_xy(self, xofs, yofs):
    """offset the xy position"""
    self.x += xofs
    self.y += yofs
    return self

  def set_orientation(self, o):
    """set the text orientation"""
    o_vals = (
      'H', # horizontal
      'V', # vertical
      )
    assert o in o_vals, 'bad text orientation %s' % o
    self.orientation = o
    return self

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

class lib_unit(object):
  """schematic unit"""

  def __init__(self):
    self.pins = []
    self.shapes = []

  def set_part(self, p):
    for x in self.shapes:
      x.set_part(p)
    for x in self.pins:
      x.set_part(p)

  def add_pin(self, p):
    self.pins.append(p)

  def add_shape(self, s):
    self.shapes.append(s)

  def ofs_xy(self, xofs, yofs):
    """offset all the pins and shapes"""
    for x in self.shapes:
      x.ofs_xy(xofs, yofs)
    for x in self.pins:
      x.ofs_xy(xofs, yofs)

  def __str__(self):
    s = []
    s.extend([str(x) for x in self.shapes])
    s.extend([str(x) for x in self.pins])
    return '\n'.join(s)

#-----------------------------------------------------------------------------

class lib_component(object):
  """schematic component"""

  def __init__(self, name, ref):
    self.name = name
    self.ref = ref
    self.ofs = 50
    self.pin_names = True
    self.pin_numbers = True
    self.nparts = 0
    self.locked = True
    self.power = False
    self.units = []
    self.footprints = []
    self.text = (
      lib_text(self.ref), # F0 reference
      lib_text(self.name), # F1 component name
      lib_text(""), # F2 footprint name
      lib_text(""), # F3 relative path to datasheet
    )

  def get_text(self, i):
    return self.text[i]

  def add_unit(self, u):
    """add a sub-unit to the component"""
    self.units.append(u)
    self.nparts += 1

  def add_footprint(self, library, name):
    """add a footprint library and name to the component"""
    self.footprints.append((library, name))

  def ofs_xy(self, xofs, yofs):
    """offset the component"""
    for x in self.units:
      x.ofs_xy(xofs, yofs)
    for x in self.text:
      x.ofs_xy(xofs, yofs)

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
    if len(self.footprints) == 1:
      # single footprint, set F2
      (library, name) = self.footprints[0]
      self.text[2].set_text('%s:%s' % (library, name))
    s.extend(['F%d %s' % (i, self.text[i]) for i in range(len(self.text))])
    return '\n'.join(s)

  def emit_tail(self):
    s = []
    s.append('ENDDEF')
    return '\n'.join(s)

  def emit_draw(self):
    s = []
    s.append('DRAW')
    s.extend([str(x) for x in self.units])
    s.append('ENDDRAW')
    return '\n'.join(s)

  def emit_footprints(self):
    s = []
    s.append('$FPLIST')
    # add footprint name patterns
    s.extend([' %s*' % x[1] for x in self.footprints])
    s.append('$ENDFPLIST')
    return '\n'.join(s)

  def __str__(self):
    for i, x in enumerate(self.units):
      x.set_part(i + 1)
    s = []
    s.append(self.emit_head())
    s.append(self.emit_footprints())
    s.append(self.emit_draw())
    s.append(self.emit_tail())
    return '\n'.join(s)

#-----------------------------------------------------------------------------

class lib_file(object):
  """schematic library file"""

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
    s.append('#\n#End Library')
    return '\n'.join(s)

  def __str__(self):
    s = []
    s.append(self.emit_head())
    s.extend([str(c) for c in self.components])
    s.append(self.emit_tail())
    return '\n'.join(s)

#-----------------------------------------------------------------------------

class dcm_component(object):
  """documentation component"""

  def __init__(self, name, descr):
    self.name = name
    self.description = descr
    self.keywords = []
    self.url = None

  def add_keywords(self, k):
    self.keywords.extend(k)

  def add_url(self, url):
    self.url = url

  def __str__(self):
    s = []
    s.append('#\n$CMP %s' % self.name)
    s.append('D %s' % self.description)
    s.append('K %s' % ' '.join([x for x in self.keywords]))
    if self.url:
      s.append('F %s' % self.url)
    s.append('$ENDCMP')
    return '\n'.join(s)

#-----------------------------------------------------------------------------

class dcm_file(object):
  """parts documentation file"""

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
