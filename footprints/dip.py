#-----------------------------------------------------------------------------
"""

Generate Dual In Place footprints

"""
#-----------------------------------------------------------------------------

import kicad
import footprint

#-----------------------------------------------------------------------------

class dip(object):

  def __init__(self, name, descr, n, width):
    self.name = name # footprint name
    self.descr = descr # description
    self.n = n # number of pins
    self.pitch = kicad.mil2mm(100)
    self.w = float(width) # width between pin rows (mm)
    self.h = (self.n / 2) * self.pitch

  def pad_xy(self, i):
    half = self.n / 2
    rhs = (i >= half)
    x = (0.0, self.w)[rhs]
    y = (i * self.pitch, (self.n - i - 1) * self.pitch)[rhs]
    return (x, y)

  def __str__(self):
    """return the kicad_mod code for this footprint"""
    mod = kicad.mod_module(self.name, self.descr)
    mod.add_tags(('DIL', 'DIP', 'PDIP', '%dmil' % kicad.mm2mil(self.w)))
    # add the pads
    pad_size = 1.6
    hole_size = 0.8
    for i in range(self.n):
      pad_shape = ('oval', 'rect')[i == 0]
      p = kicad.mod_pad('%d' % (i + 1), 'thru_hole', pad_shape, ('*.Cu', '*.Mask'))
      p.set_size(pad_size, pad_size).set_drill(hole_size)
      (x, y) = self.pad_xy(i)
      p.set_xy(x, y)
      mod.add_pad(p)


    # add text: silk reference (center top)
    t = kicad.mod_text('REF**', 'reference', 'F.SilkS')
    t.set_xy(self.w / 2.0, -self.pitch)
    mod.add_shape(t)
    # add text: fab name (center bottom)
    t = kicad.mod_text(self.name, 'value', 'F.Fab')
    t.set_xy(self.w / 2.0, self.h)
    mod.add_shape(t)
    # add text: fab reference (center)
    t = kicad.mod_text('%R', 'user', 'F.Fab')
    t.set_xy(self.w / 2.0, (self.h - self.pitch) / 2.0)
    mod.add_shape(t)

    return str(mod)


#-----------------------------------------------------------------------------

footprint.db.add(dip('DIP28_300', '28 pin DIP package, row spacing 300 mils)', 28, kicad.mil2mm(300)))
footprint.db.add(dip('DIP14_300', '14 pin DIP package, row spacing 300 mils)', 14, kicad.mil2mm(300)))
footprint.db.add(dip('DIP40_600', '40 pin DIP package, row spacing 600 mils)', 40, kicad.mil2mm(600)))

#-----------------------------------------------------------------------------
