#-----------------------------------------------------------------------------
"""

MB997 - STM32F4 Discovery Board

"""
#-----------------------------------------------------------------------------

import kicad
import footprint
import component

#-----------------------------------------------------------------------------

name = 'MB997'
descr = 'STM32F4 Discovery Board'
tags = (name, 'STM32', 'STM32F4', 'STM32F407', 'Discovery',)
url = 'http://www.st.com/en/evaluation-tools/stm32f4discovery.html'

#-----------------------------------------------------------------------------

dev = component.component(name, 'M', descr)
dev.add_tags = (tags)
dev.set_url(url)

# add all the io pins
for (j, port) in enumerate(('A', 'B', 'C', 'D', 'E',)):
  for k in range(16):
    dev.add_pin('P%s%d' % (port, k), 'inout').set_side(('L', 'R')[j & 1 == 0]).set_group(j + 1)

# fixups
dev.get_pin('PA0').add_names(('SW_PUSH',))
dev.get_pin('PA1').add_names(('system_reset',))
dev.get_pin('PA4').add_names(('I2S3_WS',))
dev.get_pin('PA5').add_names(('SPI1_SCK',))
dev.get_pin('PA6').add_names(('SPI1_MISO',))
dev.get_pin('PA7').add_names(('SPI1_MOSI',))
dev.get_pin('PA9').add_names(('VBUS_FS',))
dev.get_pin('PA10').add_names(('OTG_FS_ID',))
dev.get_pin('PA13').add_names(('SWDIO',))
dev.get_pin('PA14').add_names(('SWCLK',))
dev.get_pin('PB3').add_names(('SWO',))
dev.get_pin('PB6').add_names(('Audio_SCL',))
dev.get_pin('PB9').add_names(('Audio_SDA',))
dev.get_pin('PB10').add_names(('CLK_IN',))
dev.get_pin('PC0').add_names(('OTG_FS_PSON',))
dev.get_pin('PC3').add_names(('PDM_OUT',))
dev.get_pin('PC7').add_names(('I2S3_MCK',))
dev.get_pin('PC10').add_names(('I2S3_SCK',))
dev.get_pin('PC12').add_names(('I2S3_SD',))
dev.get_pin('PC14').add_names(('osc_in',))
dev.get_pin('PC15').add_names(('osc_out',))
dev.get_pin('PD4').add_names(('Audio_RST',))
dev.get_pin('PD5').add_names(('OTG_FS_OC',))
dev.get_pin('PD12').add_names(('LED4',))
dev.get_pin('PD13').add_names(('LED3',))
dev.get_pin('PD14').add_names(('LED5',))
dev.get_pin('PD15').add_names(('LED6',))
dev.get_pin('PE0').add_names(('MEMS_INT1',))
dev.get_pin('PE1').add_names(('MEMS_INT2',))
dev.get_pin('PE3').add_names(('MEMS_CS',))

dev.del_pin('PA11')
dev.del_pin('PA12')

dev.add_pin('NRST', 'in')
dev.add_pin('PH0', 'inout').add_names(('OSC_IN',))
dev.add_pin('PH1', 'inout').add_names(('OSC_OUT',))
dev.add_pin('BOOT0', 'in')
dev.add_pin('NC', 'nc')
dev.add_pin('3V', 'power_in').set_group(0)
dev.add_pin('5V', 'power_in').set_group(1)
dev.add_pin('VDD', 'power_in').set_group(2)
dev.add_pin('GND', 'power_in')

component.db.add(dev)

#-----------------------------------------------------------------------------

pin_map = {
  '5V': ('B3', 'B4',),
  'BOOT0': ('B21',),
  'PH0': ('B7',),
  'PC12': ('B35',),
  'PE3': ('B16',),
  'PC14': ('B9',),
  'PB9': ('B20',),
  'PD5': ('B29',),
  'PA6': ('A18',),
  'PB10': ('A34',),
  'PA14': ('B39',),
  'PA10': ('B41',),
  'PA2': ('A14',),
  'PA3': ('A13',),
  'PA0': ('A12',),
  'PD14': ('A46',),
  'PA8': ('B43',),
  'PD4': ('B32',),
  'PC11': ('B38',),
  'PC13': ('B12',),
  'VDD': ('A3', 'A4', 'B22',),
  'PB5': ('B26',),
  'PB4': ('B25',),
  'PB7': ('B24',),
  'PB1': ('A21',),
  'PB0': ('A22',),
  'PB2': ('A24',),
  'PB8': ('B19',),
  'PH1': ('B8',),
  'NRST': ('A6',),
  'PC8': ('B45',),
  'PC9': ('B46',),
  'PC2': ('A10',),
  'PC1': ('A7',),
  'PC6': ('B47',),
  'PC15': ('B10',),
  'PC5': ('A19',),
  'PD11': ('A43',),
  'PD10': ('A42',),
  'PA9': ('B44',),
  'PB3': ('B28',),
  'PC10': ('B37',),
  'PB6': ('B23',),
  'PA4': ('A16',),
  'PE0': ('B17',),
  'PD9': ('A41',),
  'PD8': ('A40',),
  'PD7': ('B27',),
  'PD6': ('B30',),
  'NC': ('A48',),
  'PD3': ('B31',),
  'PD2': ('B34',),
  'PD1': ('B33',),
  'PD0': ('B36',),
  'PC3': ('A9',),
  'PA1': ('A11',),
  'PE1': ('B18',),
  '3V': ('B5', 'B6',),
  'PA7': ('A17',),
  'PC0': ('A8',),
  'PE8': ('A26',),
  'PE9': ('A27',),
  'PE4': ('B13',),
  'PE5': ('B14',),
  'PE6': ('B11',),
  'PE7': ('A25',),
  'PE2': ('B15',),
  'PD15': ('A47',),
  'PC7': ('B48',),
  'PB11': ('A35',),
  'PB13': ('A37',),
  'PB12': ('A36',),
  'PB15': ('A39',),
  'PB14': ('A38',),
  'PA5': ('A15',),
  'PC4': ('A20',),
  'GND': ('A1', 'A2', 'A5', 'A23', 'A49', 'A50', 'B1', 'B2', 'B49', 'B50',),
  'PA15': ('B40',),
  'PD13': ('A45',),
  'PD12': ('A44',),
  'PA13': ('B42',),
  'PE14': ('A32',),
  'PE15': ('A33',),
  'PE12': ('A30',),
  'PE13': ('A31',),
  'PE10': ('A28',),
  'PE11': ('A29',),
}

dev.add_footprint(name, pin_map)

#-----------------------------------------------------------------------------

class mb997(object):

  def __init__(self):
    global name
    self.name = name
    self.w = 66.0 # board width
    self.h = 97.0 # board height

  def pad_xy(self, row, n):
    pin_spacing = kicad.mil2mm(100)
    row_spacing = kicad.mil2mm(2000)
    x = row * row_spacing + (n & 1) * pin_spacing
    y = (n >> 1) * pin_spacing
    return (x, y)

  def add_pads(self, mod):
    """add the pads"""
    pad_size = kicad.mil2mm(68)
    hole_size = kicad.mil2mm(40)
    for row in range(2):
      for n in range(50):
        pad_shape = ('circle', 'rect')[row == 0 and n == 0]
        pad_name = '%s%d' % (('A', 'B')[row == 1], n + 1)
        p = kicad.mod_pad(pad_name, 'thru_hole', pad_shape, ('*.Cu', '*.Mask'))
        p.set_size(pad_size, pad_size).set_drill(hole_size)
        p.set_xy(self.pad_xy(row, n))
        mod.add_pad(p)

  def add_courtyard(self, mod):
    """add a courtyard"""
    x = (kicad.mil2mm(2100) - self.w)/2.0
    y = kicad.mil2mm(-1350)
    mod.add_rect(x, y, self.w, self.h, 'F.CrtYd', 0.05)

  def add_fab(self, mod):
    """add a fab layer"""
    # board outline
    x = (kicad.mil2mm(2100) - self.w)/2.0
    y = kicad.mil2mm(-1350)
    mod.add_rect(x, y, self.w, self.h, 'F.Fab', 0.1)
    # fab name at top left
    t = kicad.mod_text(name, 'value', 'F.Fab')
    t.set_xy((kicad.mil2mm(-125), kicad.mil2mm(-1300)))
    mod.add_shape(t)
    # fab reference at top left
    t = kicad.mod_text('%R', 'user', 'F.Fab')
    t.set_xy((kicad.mil2mm(-125), kicad.mil2mm(-1200)))
    mod.add_shape(t)

  def add_silk(self, mod):
    """add a silk layer"""
    # add connector outlines
    cw = kicad.mil2mm(200)
    ch = kicad.mil2mm(25 * 100)
    for cx, cy in (self.pad_xy(0, 0), self.pad_xy(1, 0)):
      cx -= kicad.mil2mm(50)
      cy -= kicad.mil2mm(50)
      mod.add_rect(cx, cy, cw, ch, 'F.SilkS', 0.12)
    # silk reference
    t = kicad.mod_text('REF**', 'reference', 'F.SilkS')
    t.set_xy((kicad.mil2mm(25), kicad.mil2mm(-100)))
    mod.add_shape(t)
    # silk pin 1
    t = kicad.mod_text('A1', 'user', 'F.SilkS')
    t.set_xy((kicad.mil2mm(-100), 0))
    mod.add_shape(t)

  def __str__(self):
    """return the kicad_mod code for this footprint"""
    global descr, tags
    mod = kicad.mod_module(self.name, descr)
    mod.add_tags(tags)
    self.add_pads(mod)
    self.add_courtyard(mod)
    self.add_fab(mod)
    self.add_silk(mod)
    return str(mod)

footprint.db.add(mb997())

#-----------------------------------------------------------------------------
