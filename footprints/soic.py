#-----------------------------------------------------------------------------
"""

Generate Small Outline Integrated Cicuit footprints

"""
#-----------------------------------------------------------------------------

import kicad
import footprint

#-----------------------------------------------------------------------------

class soic(object):

  def __init__(self, n, w, pitch, pad_w, pad_h):
    self.name = ''
    self.descr = ''
    self.n = n # number of pads
    self.pitch = float(pitch) # vertical pad pitch
    self.w = float(w) # horizontal width pad to pad center
    self.h = ((self.n / 2) - 1) * self.pitch
    self.pad_w = pad_w # width of pad
    self.pad_h = pad_h # height of pad

  def pad_xy(self, i):
    """return the x, y position of pad i"""
    half = self.n / 2
    rhs = (i >= half)
    x = (0.0, self.w)[rhs]
    y = (i * self.pitch, (self.n - i - 1) * self.pitch)[rhs]
    return (x, y)

  def add_pads(self, mod):
    """add the pads"""
    for i in range(self.n):
      p = kicad.mod_pad('%d' % i, 'smd', 'rect', ('F.Cu', 'F.Mask', 'F.Paste'))
      p.set_size(self.pad_w, self.pad_h)
      p.set_xy(self.pad_xy(i))
      mod.add_pad(p)

  def add_courtyard(self, mod):
    """add a courtyard"""
    pass

  def add_fab(self, mod):
    """add a fab layer"""
    pass

  def add_silk(self, mod):
    """add a silk layer"""
    pass

  def __str__(self):
    """return the kicad_mod code for this footprint"""
    mod = kicad.mod_module(self.name, self.descr)
    mod.add_tags(self.tags)
    self.add_pads(mod)
    self.add_courtyard(mod)
    self.add_fab(mod)
    self.add_silk(mod)
    return str(mod)

#-----------------------------------------------------------------------------

x = soic(28, 9.4, 1.27, 2, 0.6)
x.name = 'SOIC-28W_7.5x17.9mm_Pitch1.27mm'
x.descr = '28-Lead Plastic Small Outline (SO) - Wide, 7.50 mm Body [SOIC] (see Microchip Packaging Specification 00000049BS.pdf)'
x.tags = ('SOIC',)
footprint.db.add(x)

#-----------------------------------------------------------------------------

x = soic(28, 9.4, 0.65, 1.75, 0.45)
x.name = 'TI-HTSSOP28-PWP'
x.descr = 'TI-HTSSOP28-PWP http://www.ti.com/lit/ml/mpds373/mpds373.pdf'
x.tags = ('TI', 'PWP', 'HTSSOP', 'SOIC')
footprint.db.add(x)

#-----------------------------------------------------------------------------
