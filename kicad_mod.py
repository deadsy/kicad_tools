#-----------------------------------------------------------------------------
"""

KiCAD MOD Objects

Generate the *.kicad_mod files defining the PCB footprint

"""
#-----------------------------------------------------------------------------

"""

(module R_Array_Convex_8x0602 (layer F.Cu) (tedit 54539007)
  (descr "Chip Resistor Network, ROHM MNR18 (see mnr_g.pdf)")
  (tags "resistor array")
  (attr smd)
  (fp_text reference REF** (at 0 -3) (layer F.SilkS)
    (effects (font (size 1 1) (thickness 0.15)))
  )
  (fp_text value R_Array_Convex_8x0602 (at 0 3) (layer F.Fab)
    (effects (font (size 1 1) (thickness 0.15)))
  )
  (fp_line (start -1.55 -2.25) (end 1.55 -2.25) (layer F.CrtYd) (width 0.05))
  (fp_line (start -1.55 2.25) (end 1.55 2.25) (layer F.CrtYd) (width 0.05))
  (fp_line (start -1.55 -2.25) (end -1.55 2.25) (layer F.CrtYd) (width 0.05))
  (fp_line (start 1.55 -2.25) (end 1.55 2.25) (layer F.CrtYd) (width 0.05))
  (fp_line (start 0.5 2.125) (end -0.5 2.125) (layer F.SilkS) (width 0.15))
  (fp_line (start 0.5 -2.125) (end -0.5 -2.125) (layer F.SilkS) (width 0.15))
  (pad 1 smd rect (at -0.9 -1.75) (size 0.8 0.3) (layers F.Cu F.Paste F.Mask))
  (pad 16 smd rect (at 0.9 -1.75) (size 0.8 0.3) (layers F.Cu F.Paste F.Mask))
  (pad 8 smd rect (at -0.9 1.75) (size 0.8 0.3) (layers F.Cu F.Paste F.Mask))
  (pad 9 smd rect (at 0.9 1.75) (size 0.8 0.3) (layers F.Cu F.Paste F.Mask))
  (pad 2 smd rect (at -0.9 -1.25) (size 0.8 0.3) (layers F.Cu F.Paste F.Mask))
  (pad 3 smd rect (at -0.9 -0.75) (size 0.8 0.3) (layers F.Cu F.Paste F.Mask))
  (pad 4 smd rect (at -0.9 -0.25) (size 0.8 0.3) (layers F.Cu F.Paste F.Mask))
  (pad 5 smd rect (at -0.9 0.25) (size 0.8 0.3) (layers F.Cu F.Paste F.Mask))
  (pad 6 smd rect (at -0.9 0.75) (size 0.8 0.3) (layers F.Cu F.Paste F.Mask))
  (pad 7 smd rect (at -0.9 1.25) (size 0.8 0.3) (layers F.Cu F.Paste F.Mask))
  (pad 15 smd rect (at 0.9 -1.25) (size 0.8 0.3) (layers F.Cu F.Paste F.Mask))
  (pad 14 smd rect (at 0.9 -0.75) (size 0.8 0.3) (layers F.Cu F.Paste F.Mask))
  (pad 13 smd rect (at 0.9 -0.25) (size 0.8 0.3) (layers F.Cu F.Paste F.Mask))
  (pad 11 smd rect (at 0.9 0.75) (size 0.8 0.3) (layers F.Cu F.Paste F.Mask))
  (pad 12 smd rect (at 0.9 0.25) (size 0.8 0.3) (layers F.Cu F.Paste F.Mask))
  (pad 10 smd rect (at 0.9 1.25) (size 0.8 0.3) (layers F.Cu F.Paste F.Mask))
  (model Resistors_SMD.3dshapes/R_Array_Convex_8x0602.wrl
    (at (xyz 0 0 0))
    (scale (xyz 1 1 1))
    (rotate (xyz 0 0 0))
  )
)

"""

#-----------------------------------------------------------------------------

class at(object):

  def __init__(self, x=0.0, y=0.0, a=0.0):
    self.x = x
    self.y = y
    self.a = a

  def __str__(self):
    if self.a == 0:
      return '(at %.2f %.2f)' % (self.x, self.y)
    else:
      return '(at %.2f %.2f %.2f)' % (self.x, self.y, self.a)

#-----------------------------------------------------------------------------

class size(object):

  def __init__(self, w=0.0, h=0.0):
    self.w = w
    self.h = h

  def __str__(self):
    return '(size %.2f %.2f)' % (self.w, self.h)

#-----------------------------------------------------------------------------

ptypes = ('thru_hole', 'smd', 'connect', 'np_thru_hole')
pshapes = ('circle', 'rect', 'oval', 'trapezoid')

class pad(object):

  def __init__(self, name, ptype='smd', shape='rect'):
    self.name = name # pin number or name (string)
    self.ptype = ptype # pad type
    self.shape = shape
    self.at = at()
    self.size = size()

  def set_type(self, t):
    assert t in ptypes, 'bad pad type %s' % t
    self.ptype = t

  def set_shape(self, s):
    assert s in pshapes, 'bad pad shape %s' % s
    self.shape = s

  def __str__(self):
    s = []
    s.append('%s' % self.name)
    s.append('%s' % self.ptype)
    s.append('%s' % self.shape)
    s.append(str(self.at))
    s.append(str(self.size))
    return '(pad %s)' % ' '.join(s)

#-----------------------------------------------------------------------------

def main():
  x = pad('1')
  print x

main()
