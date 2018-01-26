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

pins = []
# add all the io pins
for (j, port) in enumerate(('A', 'B', 'C', 'D', 'E',)):
  for k in range(16):
    pins.append(component.pin('P%s%d' % (port, k), 'inout', side=('L', 'R')[j & 1 == 0], group=j + 1))

# fixups
component.append_pin_name(pins, 'PA0', 'SW_PUSH')
component.append_pin_name(pins, 'PA1', 'system_reset')
component.append_pin_name(pins, 'PA4', 'I2S3_WS')
component.append_pin_name(pins, 'PA5', 'SPI1_SCK')
component.append_pin_name(pins, 'PA6', 'SPI1_MISO')
component.append_pin_name(pins, 'PA7', 'SPI1_MOSI')
component.append_pin_name(pins, 'PA9', 'VBUS_FS')
component.append_pin_name(pins, 'PA10', 'OTG_FS_ID')
component.append_pin_name(pins, 'PA13', 'SWDIO')
component.append_pin_name(pins, 'PA14', 'SWCLK')
component.append_pin_name(pins, 'PB3', 'SWO')
component.append_pin_name(pins, 'PB6', 'Audio_SCL')
component.append_pin_name(pins, 'PB9', 'Audio_SDA')
component.append_pin_name(pins, 'PB10', 'CLK_IN')
component.append_pin_name(pins, 'PC0', 'OTG_FS_PSON')
component.append_pin_name(pins, 'PC3', 'PDM_OUT')
component.append_pin_name(pins, 'PC7', 'I2S3_MCK')
component.append_pin_name(pins, 'PC10', 'I2S3_SCK')
component.append_pin_name(pins, 'PC12', 'I2S3_SD')
component.append_pin_name(pins, 'PC14', 'osc_in')
component.append_pin_name(pins, 'PC15', 'osc_out')
component.append_pin_name(pins, 'PD4', 'Audio_RST')
component.append_pin_name(pins, 'PD5', 'OTG_FS_OC')
component.append_pin_name(pins, 'PD12', 'LED4')
component.append_pin_name(pins, 'PD13', 'LED3')
component.append_pin_name(pins, 'PD14', 'LED5')
component.append_pin_name(pins, 'PD15', 'LED6')
component.append_pin_name(pins, 'PE0', 'MEMS_INT1')
component.append_pin_name(pins, 'PE1', 'MEMS_INT2')
component.append_pin_name(pins, 'PE3', 'MEMS_CS')

component.remove_pin(pins, 'PA11')
component.remove_pin(pins, 'PA12')

other_pins = (
  component.pin('NRST', 'in'),
  component.pin('PH0/OSC_IN', 'inout'),
  component.pin('PH1/OSC_OUT', 'inout'),
  component.pin('BOOT0', 'in'),
  component.pin('NC', 'nc'),
  component.pin('3V', 'power_in', group=0),
  component.pin('5V', 'power_in', group=1),
  component.pin('VDD', 'power_in', group=2),
  component.pin('GND', 'power_in'),
)
pins.extend(other_pins)

dev.add_pins(pins)
component.db.add(dev)

#-----------------------------------------------------------------------------

pin_map = {
  '5V': ('B3', 'B4',),
  'BOOT0': ('B21',),
  'PH0/OSC_IN': ('B7',),
  'PC12/I2S3_SD': ('B35',),
  'PE3/MEMS_CS': ('B16',),
  'PC14/osc_in': ('B9',),
  'PB9/Audio_SDA': ('B20',),
  'PD5/OTG_FS_OC': ('B29',),
  'PA6/SPI1_MISO': ('A18',),
  'PB10/CLK_IN': ('A34',),
  'PA14/SWCLK': ('B39',),
  'PA10/OTG_FS_ID': ('B41',),
  'PA2': ('A14',),
  'PA3': ('A13',),
  'PA0/SW_PUSH': ('A12',),
  'PD14/LED5': ('A46',),
  'PA8': ('B43',),
  'PD4/Audio_RST': ('B32',),
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
  'PH1/OSC_OUT': ('B8',),
  'NRST': ('A6',),
  'PC8': ('B45',),
  'PC9': ('B46',),
  'PC2': ('A10',),
  'PC1': ('A7',),
  'PC6': ('B47',),
  'PC15/osc_out': ('B10',),
  'PC5': ('A19',),
  'PD11': ('A43',),
  'PD10': ('A42',),
  'PA9/VBUS_FS': ('B44',),
  'PB3/SWO': ('B28',),
  'PC10/I2S3_SCK': ('B37',),
  'PB6/Audio_SCL': ('B23',),
  'PA4/I2S3_WS': ('A16',),
  'PE0/MEMS_INT1': ('B17',),
  'PD9': ('A41',),
  'PD8': ('A40',),
  'PD7': ('B27',),
  'PD6': ('B30',),
  'NC': ('A48',),
  'PD3': ('B31',),
  'PD2': ('B34',),
  'PD1': ('B33',),
  'PD0': ('B36',),
  'PC3/PDM_OUT': ('A9',),
  'PA1/system_reset': ('A11',),
  'PE1/MEMS_INT2': ('B18',),
  '3V': ('B5', 'B6',),
  'PA7/SPI1_MOSI': ('A17',),
  'PC0/OTG_FS_PSON': ('A8',),
  'PE8': ('A26',),
  'PE9': ('A27',),
  'PE4': ('B13',),
  'PE5': ('B14',),
  'PE6': ('B11',),
  'PE7': ('A25',),
  'PE2': ('B15',),
  'PD15/LED6': ('A47',),
  'PC7/I2S3_MCK': ('B48',),
  'PB11': ('A35',),
  'PB13': ('A37',),
  'PB12': ('A36',),
  'PB15': ('A39',),
  'PB14': ('A38',),
  'PA5/SPI1_SCK': ('A15',),
  'PC4': ('A20',),
  'GND': ('A1', 'A2', 'A5', 'A23', 'A49', 'A50', 'B1', 'B2', 'B49', 'B50',),
  'PA15': ('B40',),
  'PD13/LED3': ('A45',),
  'PD12/LED4': ('A44',),
  'PA13/SWDIO': ('B42',),
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
