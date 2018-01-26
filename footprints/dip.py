#-----------------------------------------------------------------------------
"""

Generate Dual In Place footprints

"""
#-----------------------------------------------------------------------------

import kicad
import footprint

#-----------------------------------------------------------------------------

class dip(object):
  """dual in place package generator"""

  def __init__(self, n, width):
    self.name = 'DIP%d_%d' % (n, kicad.mm2mil(width))
    self.descr = '%d pin DIP package, row spacing %d mils' % (n, kicad.mm2mil(width))
    self.n = n # number of pins
    self.pitch = kicad.mil2mm(100)
    self.w = float(width) # width between pin rows (mm)
    self.h = ((self.n / 2) - 1) * self.pitch

  def pad_xy(self, i):
    """return the x, y position of pad i"""
    half = self.n / 2
    rhs = (i >= half)
    x = (0.0, self.w)[rhs]
    y = (i * self.pitch, (self.n - i - 1) * self.pitch)[rhs]
    return (x, y)

  def centered_rect(self, mod, w, h, layer, pwidth, render=('T', 'B', 'L', 'R')):
    """add a centered rectangle"""
    x = (self.w - w) / 2.0
    y = (self.h - h) / 2.0
    mod.add_rect(x, y, w, h, layer, pwidth, render)

  def courtyard(self, mod):
    """add a courtyard"""
    w = self.w + 3.0
    h = self.h + 3.0
    self.centered_rect(mod, w, h, 'F.CrtYd', 0.05)

  def fab(self, mod):
    """add a fab layer"""
    d = kicad.mil2mm(100)
    w = self.w + d
    h = self.h + d
    self.centered_rect(mod, w, h, 'F.Fab', 0.1)
    w = self.w - d
    self.centered_rect(mod, w, h, 'F.Fab', 0.1, render=('L', 'R'))
    # add the notch
    x = (self.w - w) / 2.0
    y = (self.h - h) / 2.0
    w = self.pitch / 2.0
    h = w
    mod.add_rect(x, y, w, h, 'F.Fab', 0.1, render=('d0',))

  def silk(self, mod):
    """add a silk layer"""
    d = kicad.mil2mm(110)
    w = self.w + d
    h = self.h + d
    self.centered_rect(mod, w, h, 'F.SilkS', 0.12)
    w = self.w - d
    self.centered_rect(mod, w, h, 'F.SilkS', 0.12, render=('L', 'R'))
    mod.add_arc(self.w/2.0, -d / 2.0, self.pitch / 2.0, 'F.SilkS', 0.12)

  def __str__(self):
    """return the kicad_mod code for this footprint"""
    mod = kicad.mod_module(self.name, self.descr)
    mod.add_tags(('DIL', 'DIP', 'PDIP', '%dmil' % kicad.mm2mil(self.w)))
    # add text: silk reference (center top)
    t = kicad.mod_text('REF**', 'reference', 'F.SilkS')
    t.set_xy((self.w / 2.0, -self.pitch))
    mod.add_shape(t)
    # add text: fab name (center bottom)
    t = kicad.mod_text(self.name, 'value', 'F.Fab')
    t.set_xy((self.w / 2.0, self.h + self.pitch))
    mod.add_shape(t)
    # add text: fab reference (center)
    t = kicad.mod_text('%R', 'user', 'F.Fab')
    t.set_xy((self.w / 2.0, self.h / 2.0))
    mod.add_shape(t)
    # add the pads
    pad_size = 1.6
    hole_size = 0.8
    for i in range(self.n):
      pad_shape = ('oval', 'rect')[i == 0]
      p = kicad.mod_pad('%d' % (i + 1), 'thru_hole', pad_shape, ('*.Cu', '*.Mask'))
      p.set_size(pad_size, pad_size).set_drill(hole_size)
      p.set_xy(self.pad_xy(i))
      mod.add_pad(p)

    self.courtyard(mod)
    self.fab(mod)
    self.silk(mod)
    return str(mod)

#-----------------------------------------------------------------------------

footprint.db.add(dip(8, kicad.mil2mm(300)))
footprint.db.add(dip(28, kicad.mil2mm(300)))
footprint.db.add(dip(14, kicad.mil2mm(300)))
footprint.db.add(dip(40, kicad.mil2mm(600)))

#-----------------------------------------------------------------------------
