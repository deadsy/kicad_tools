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
  return MM_PER_INCH * (float(mil) / 1000.0)

def mm2mil(mm):
  return 1000.0 * float(mm) / MM_PER_INCH

def tedit_secs():
  """return number of seconds since 1970/1/1"""
  return int(time.time())

def mm(d):
  s = '%.3f' % d
  # strip trailing 0's
  s = s.rstrip('0')
  # strip trailing .
  s = s.rstrip('.')
  return s

#-----------------------------------------------------------------------------

class point(object):
  """2d point"""

  def __init__(self, x, y):
    self.x = float(x)
    self.y = float(y)

#-----------------------------------------------------------------------------

class mod_at(object):
  """footprint at element"""

  def __init__(self, x, y, a=0):
    self.x = float(x)
    self.y = float(y)
    self.a = float(a)

  def ofs_xy(self, xofs, yofs):
    """offset the xy position"""
    self.x += float(xofs)
    self.y += float(yofs)

  def __str__(self):
    if self.a == 0:
      return '(at %s %s)' % (mm(self.x), mm(self.y))
    else:
      return '(at %s %s %s)' % (mm(self.x), mm(self.y), mm(self.a))

#-----------------------------------------------------------------------------

class mod_size(object):
  """footprint size element"""

  def __init__(self, w, h):
    self.w = float(w)
    self.h = float(h)

  def __str__(self):
    return '(size %s %s)' % (mm(self.w), mm(self.h))

#-----------------------------------------------------------------------------

class mod_width(object):
  """footprint width element"""

  def __init__(self, w):
    self.w = float(w)

  def __str__(self):
    return '(width %s)' % mm(self.w)

#-----------------------------------------------------------------------------

class mod_xy(object):
  """footprint xy element"""

  def __init__(self, x, y):
    self.x = float(x)
    self.y = float(y)

  def __str__(self):
    return '(xy %s %s)' % (mm(self.x), mm(self.y))

#-----------------------------------------------------------------------------

class mod_start(object):
  """footprint start element"""

  def __init__(self, p):
    self.p = p

  def __str__(self):
    return '(start %s %s)' % (mm(self.p.x), mm(self.p.y))

#-----------------------------------------------------------------------------

class mod_end(object):
  """footprint end element"""

  def __init__(self, p):
    self.p = p

  def __str__(self):
    return '(end %s %s)' % (mm(self.p.x), mm(self.p.y))

#-----------------------------------------------------------------------------

class mod_angle(object):
  """footprint angle element"""

  def __init__(self, a):
    self.a = float(a)

  def __str__(self):
    return '(angle %s)' % mm(self.a)

#-----------------------------------------------------------------------------

class mod_pts(object):
  """footprint pts (points) element"""

  def __init__(self, points=None):
    self.points = points

  def __str__(self):
    assert self.points is not None and len(self.points) != 0, 'no points in points list'
    return '(pts %s)' % ' '.join([str(x) for x in self.points])

#-----------------------------------------------------------------------------

class mod_rect_delta(object):
  """footprint rect_delta"""

  def __init__(self, dx=0.0, dy=0.0):
    self.dx = dx
    self.dy = dy

  def __str__(self):
    return '(rect_delta %s %s)' % (mm(self.dy), mm(self.dx))

#-----------------------------------------------------------------------------

class mod_drill(object):
  """footprint drill"""

  def __init__(self, size, xofs=0, yofs=0):
    self.size = float(size)
    self.xofs = float(xofs)
    self.yofs = float(yofs)

  def __str__(self):
    if (self.xofs != 0.0) or (self.yofs != 0.0):
      return '(drill %s (offset %s %s))' % (mm(self.size), mm(self.xofs), mm(self.yofs))
    else:
      return '(drill %s)' % mm(self.size)

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

def valid_layer(l):
  """is this a valid layer?"""
  x = l.split('.')
  if len(x) != 2:
    return False
  if x[0] not in layer_names:
    return False
  if x[1] not in layer_types:
    return False
  return True

class mod_layer(object):
  """single footprint layer"""

  def __init__(self, l):
    assert valid_layer(l), 'invalid layer %s' % l
    self.layer = l

  def __str__(self):
    return '(layer %s)' % self.layer

class mod_layers(object):
  """list of footprint layers"""

  def __init__(self, layers):
    for l in layers:
      assert valid_layer(l), 'invalid layer %s' % l
    self.layers = layers

  def __str__(self):
    return '(layers %s)' % ' '.join([x for x in self.layers])

#-----------------------------------------------------------------------------

pad_types = ('thru_hole', 'smd', 'connect', 'np_thru_hole')
pad_shapes = ('circle', 'rect', 'oval', 'trapezoid')

class mod_pad(object):
  """footprint pad"""

  def __init__(self, name, pad_type, pad_shape, layers):
    assert pad_type in pad_types, 'bad pad type %s' % pad_type
    assert pad_shape in pad_shapes, 'bad pad shape %s' % pad_shape
    self.name = (name, '""')[len(name) == 0]
    self.pad_type = pad_type # pad type
    self.pad_shape = pad_shape
    self.layers = mod_layers(layers)
    self.rect_delta = None
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

  def set_xy(self, v):
    """set the xy position"""
    self.at = mod_at(v[0], v[1])
    return self

  def set_size(self, w, h):
    """set the pad size"""
    self.size = mod_size(w, h)
    return self

  def set_drill(self, s):
    """set the drill size"""
    self.drill = mod_drill(s)
    return self

  def __str__(self):
    s = []
    s.append('%s' % self.name)
    s.append('%s' % self.pad_type)
    s.append('%s' % self.pad_shape)
    assert self.at is not None, 'pad does not have at location'
    s.append(str(self.at))
    assert self.size is not None, 'no pad size defined'
    s.append(str(self.size))
    if self.pad_shape == 'trapezoid':
      assert self.rect_delta is not None, 'no pad rect_delta defined'
      s.append(str(self.rect_delta))
    if self.pad_type in ('thru_hole', 'np_thru_hole'):
      assert self.drill is not None, 'no pad drill defined'
      s.append(str(self.drill))
    s.append(str(self.layers))
    return '(pad %s)' % ' '.join(s)

#-----------------------------------------------------------------------------

class mod_font(object):

  def __init__(self):
    self.size = mod_size(1, 1)
    self.thickness = 0.15

  def __str__(self):
    return '(font %s (thickness %s))' % (self.size, mm(self.thickness))

#-----------------------------------------------------------------------------

class mod_effects(object):

  def __init__(self):
    self.font = mod_font()

  def __str__(self):
    s = []
    s.append(str(self.font))
    return '(effects %s)' % ' '.join(s)

#-----------------------------------------------------------------------------

text_types = ('reference', 'value', 'user')

class mod_text(object):
  """footprint fp_text element"""

  def __init__(self, text, text_type, layer):
    assert text_type in text_types, 'bad text type %s' % text_type
    self.text = text
    self.text_type = text_type
    self.layer = mod_layer(layer)
    self.effects = mod_effects()
    self.at = None

  def set_xy(self, v):
    """set the xy position"""
    self.at = mod_at(v[0], v[1])
    return self

  def __str__(self):
    s = []
    assert self.at is not None, 'need to set the text position'
    s.append('(fp_text %s %s %s %s' % (self.text_type, self.text, self.at, self.layer))
    s.append(indent(str(self.effects)))
    s.append(')')
    return '\n'.join(s)

#-----------------------------------------------------------------------------

class mod_poly(object):
  """footprint fp_poly element"""

  def __init__(self, pts, layer, width):
    self.pts = pts
    self.layer = mod_layer(layer)
    self.width = mod_width(width)

  def __str__(self):
    s = []
    s.append('(fp_poly')
    s.append(indent(str(self.pts)))
    s.append(indent(str(self.layer)))
    s.append(indent(str(self.width)))
    s.append(')')
    return '\n'.join(s)

#-----------------------------------------------------------------------------

class mod_line(object):
  """footprint fp_line element"""

  def __init__(self, start, end, layer, width):
    self.start = mod_start(start)
    self.end = mod_end(end)
    self.layer = mod_layer(layer)
    self.width = mod_width(width)

  def __str__(self):
    s = []
    s.append('(fp_line')
    s.append(indent(str(self.start)))
    s.append(indent(str(self.end)))
    s.append(indent(str(self.layer)))
    s.append(indent(str(self.width)))
    s.append(')')
    return '\n'.join(s)

#-----------------------------------------------------------------------------

class mod_arc(object):
  """footprint fp_arc element"""

  def __init__(self, start, end, angle, layer, width):
    self.start = mod_start(start)
    self.end = mod_end(end)
    self.angle = mod_angle(angle)
    self.layer = mod_layer(layer)
    self.width = mod_width(width)

  def __str__(self):
    s = []
    s.append('(fp_arc')
    s.append(indent(str(self.start)))
    s.append(indent(str(self.end)))
    s.append(indent(str(self.angle)))
    s.append(indent(str(self.layer)))
    s.append(indent(str(self.width)))
    s.append(')')
    return '\n'.join(s)

#-----------------------------------------------------------------------------

class mod_module(object):
  """footprint module"""

  def __init__(self, name, descr, layer='F.Cu'):
    self.name = name
    self.descr = descr
    self.pads = []
    self.tags = []
    self.shapes = []
    self.layer = mod_layer(layer)
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
    if p.pad_type == 'smd':
      self.attr = 'smd'
    self.pads.append(p)

  def add_shape(self, s):
    self.shapes.append(s)

  def add_block(self, w, h, layer, pwidth):
    """add a w x h block (filled) centered on the origin"""
    tl = mod_xy(-w/2.0, h/2.0)
    tr = mod_xy(w/2.0, h/2.0)
    bl = mod_xy(-w/2.0, -h/2.0)
    br = mod_xy(w/2.0, -h/2.0)
    pts = mod_pts((tl, tr, br, bl))
    poly = mod_poly(pts, layer, pwidth)
    self.add_shape(poly)

  def add_rect(self, x, y, w, h, layer, pwidth, render=('T', 'B', 'L', 'R')):
    """add a w x h rectangle with top left corner at x,y"""
    x = float(x)
    y = float(y)
    w = float(w)
    h = float(h)
    tl = point(x, y)
    tr = point(x + w, y)
    bl = point(x, y + h)
    br = point(x + w, y + h)
    if 'T' in render:
      self.add_shape(mod_line(tl, tr, layer, pwidth))
    if 'R' in render:
      self.add_shape(mod_line(tr, br, layer, pwidth))
    if 'B' in render:
      self.add_shape(mod_line(br, bl, layer, pwidth))
    if 'L' in render:
      self.add_shape(mod_line(bl, tl, layer, pwidth))
    if 'd0' in render:
      self.add_shape(mod_line(bl, tr, layer, pwidth))
    if 'd1' in render:
      self.add_shape(mod_line(tl, br, layer, pwidth))

  def add_arc(self, x, y, radius, layer, pwidth):
    start = point(x, y)
    end = point(x + radius, y)
    self.add_shape(mod_arc(start, end, 180, layer, pwidth))


  def tags_str(self):
    return '"%s"' % ' '.join([str(x) for x in self.tags])

  def __str__(self):
    s = []
    s.append('(module %s %s (tedit %X)' % (self.name, self.layer, tedit_secs()))
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
    # map a user friendly string onto the kicad pin type
    pin_types = {
      'in': 'I', # Input
      'out': 'O', # Output
      'inout': 'B', # Bidirectional
      'tristate': 'T', # Tristate
      'passive': 'P', # Passive
      'open_collector': 'C', # Open Collector
      'open_emitter': 'E', # Open Emitter
      'nc': 'N', # Non-connected
      'unspecified': 'U', # Unspecified
      'power_in': 'W', # Power input
      'power_out': 'w', # Power output
    }
    self.type = pin_types[t]
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
    x = '%s%s' % (self.visible, self.shape)
    if len(x):
      s.append(x)
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

  def add_components(self, c):
    self.components.extend(c)

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
    s.extend([c.lib_str(self.name) for c in self.components])
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

  def add_components(self, c):
    self.components.extend(c)

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
    s.extend([x.dcm_str() for x in self.components])
    s.append(self.emit_tail())
    return '\n'.join(s)

#-----------------------------------------------------------------------------
