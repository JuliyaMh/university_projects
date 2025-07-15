#!/usr/bin/env python
# coding=utf-8

import inkex

def draw_SVG_square(amount, width, height, cur):
    x = 0
    d = ''
    for i in range(int(amount)):
        d += ('M ' + str(x + width / 7 * 3) + ', 0 ' +
              'L ' + str(x + width / 7 * 3) + ', ' + str(height / 5 * 2) +
              ' L ' + str(x) + ', ' + str(height / 5 * 2) +
              ' L ' + str(x + width / 7 * 3) + ', 0 ' +
              'L ' + str(x + width / 7 * 3.8) + ', ' + str(height / 5 * 0.5) +
              ' L ' + str(x + width / 7 * 3) + ', ' + str(height / 5) +
              ' L ' + str(x + width / 7 * 3.8) + ', ' + str(height / 5 * 1.5) +
              ' L ' + str(x + width / 7 * 3) + ', ' + str(height / 5 * 2) +
              ' M ' + str(x + width / 7 * 4) + ', ' + str(height / 5 * 2) +
              ' L ' + str(x + width / 7 * 4) + ', 0' +
              ' L' + str(x + width) + ', ' + str(height / 5 * 2) +
              ' L ' + str(x + width / 7 * 4) + ', ' + str(height / 5 * 2) +
              ' L ' + str(x + width / 7 * 4.5) + ', ' + str(height / 5 * 2.8) +
              ' L ' + str(x + width / 7 * 5) + ', ' + str(height / 5 * 2) +
              ' L ' + str(x + width / 7 * 5.5) + ', ' + str(height / 5 * 2.8) +
              ' L ' + str(x + width / 7 * 6) + ', ' + str(height / 5 * 2) +
              ' L ' + str(x + width / 7 * 6.5) + ', ' + str(height / 5 * 2.8) +
              ' L ' + str(x + width) + ', ' + str(height / 5 * 2) +
              ' M ' + str(x) + ', ' + str(height / 5 * 3) +
              ' L ' + str(x + width / 7 * 3) + ', ' + str(height) +
              ' L ' + str(x + width / 7 * 3) + ', ' + str(height / 5 * 3) +
              ' L ' + str(x) + ', ' + str(height / 5 * 3) +
              ' L ' + str(x + width / 7 * 0.5) + ', ' + str(height / 5 * 2.2) +
              ' L ' + str(x + width / 7) + ', ' + str(height / 5 * 3) +
              ' L ' + str(x + width / 7 * 1.5) + ', ' + str(height / 5 * 2.2) +
              ' L ' + str(x + width / 7 * 2) + ', ' + str(height / 5 * 3) +
              ' L ' + str(x + width / 7 * 2.5) + ', ' + str(height / 5 * 2.2) +
              ' L ' + str(x + width / 7 * 3) + ', ' + str(height / 5 * 3) +
              ' M ' + str(x + width / 7 * 4) + ', ' + str(height / 5 * 3) +
              ' L ' + str(x + width) + ', ' + str(height / 5 * 3) +
              ' L ' + str(x + width / 7 * 4) + ', ' + str(height) +
              ' L ' + str(x + width / 7 * 4) + ', ' + str(height / 5 * 3) +
              ' L ' + str(x + width / 7 * 3.2) + ', ' + str(height / 5 * 3.5) +
              ' L ' + str(x + width / 7 * 4) + ', ' + str(height / 5 * 4) +
              ' L ' + str(x + width / 7 * 3.2) + ', ' + str(height / 5 * 4.5) +
              ' L ' + str(x + width / 7 * 4) + ', ' + str(height))
        x += width
    style = {'stroke': '#000000', 'stroke-width': '0.3', 'fill': 'none'}
    elem = cur.add(inkex.PathElement())
    elem.update(**{
        'style': style,
        'inkscape:label': 'MySquare',
         'd': d
    })
    return elem

class MyOrnament(inkex.EffectExtension):

    def add_arguments(self, pars):
        pars.add_argument("--amount", type=int, default=5, help="Amount of rapports")
        pars.add_argument("--height", type=float, default=50.0, help="Height of a rapport")
        pars.add_argument("--width", type=float, default=70.0, help="Width of a rapport")

    def effect(self):
        cur = self.svg.get_current_layer()
        amount = self.options.amount  # ????????????????????
        height = self.options.height
        width = self.options.width
        draw_SVG_square(amount, width, height, cur)

if __name__ == '__main__':
    MyOrnament().run()
