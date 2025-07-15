#!/usr/bin/env python
# coding=utf-8
import sys
import inkex
import math




def generate_my_fract_part(depth, x0, y0, length, level=1, position=0):
    if position == 0:
        s = ('M ' + str(x0 - length / 2) + ', ' + str(y0 - length / 2) +
             ' L ' + str(x0 + length / 2) + ', ' + str(y0 - length / 2) +
             ' L ' + str(x0 + length / 2) + ', ' + str(y0 + length / 2) +
             ' L ' + str(x0 - length / 2) + ', ' + str(y0 + length / 2) +
             ' L ' + str(x0 - length / 2) + ', ' + str(y0 - length / 2))
    elif position == 1:
        s = ('M ' + str(x0 - length / 2) + ', ' + str(y0 - length / 2) +
             ' L ' + str(x0 + length / 2) + ', ' + str(y0 - length / 2) +
             ' L ' + str(x0 + length / 2) + ', ' + str(y0) +
             ' M ' + str(x0) + ', ' + str(y0 + length / 2) +
             ' L ' + str(x0 - length / 2) + ', ' + str(y0 + length / 2) +
             ' L ' + str(x0 - length / 2) + ', ' + str(y0 - length / 2))
    elif position == 2:
        s = ('M ' + str(x0 - length / 2) + ', ' + str(y0 - length / 2) +
             ' L ' + str(x0 + length / 2) + ', ' + str(y0 - length / 2) +
             ' L ' + str(x0 + length / 2) + ', ' + str(y0 + length / 2) +
             ' L ' + str(x0) + ', ' + str(y0 + length / 2) +
             ' M ' + str(x0 - length / 2) + ', ' + str(y0) +
             ' L ' + str(x0 - length / 2) + ', ' + str(y0 - length / 2))
    elif position == 3:
        s = ('M ' + str(x0) + ', ' + str(y0 - length / 2) +
             ' L ' + str(x0 + length / 2) + ', ' + str(y0 - length / 2) +
             ' L ' + str(x0 + length / 2) + ', ' + str(y0 + length / 2) +
             ' L ' + str(x0 - length / 2) + ', ' + str(y0 + length / 2) +
             ' L ' + str(x0 - length / 2) + ', ' + str(y0))
    elif position == 4:
        s = ('M ' + str(x0 - length /2) + ', ' + str(y0 - length / 2) +
             ' L ' + str(x0) + ', ' + str(y0 - length / 2) +
             ' M ' + str(x0 + length / 2) + ', ' + str(y0) +
             ' L ' + str(x0 + length / 2) + ', ' + str(y0 + length / 2) +
             ' L ' + str(x0 - length / 2) + ', ' + str(y0 + length / 2) +
             ' L ' + str(x0 - length / 2) + ', ' + str(y0 - length / 2))
    if level < depth:
        if position != 3:
            s += ' ' + generate_my_fract_part(depth, x0 - length / 2, y0 - length / 2, length // 2, level + 1, 1) + ' '
        if position != 4:
            s += ' ' + generate_my_fract_part(depth, x0 + length / 2, y0 - length / 2, length // 2, level + 1, 2) + ' '
        if position != 1:
            s += ' ' + generate_my_fract_part(depth, x0 + length / 2, y0 + length / 2, length // 2, level + 1, 3) + ' '
        if position != 2:
            s += ' ' + generate_my_fract_part(depth, x0 - length / 2, y0 + length / 2, length // 2, level + 1, 4)
    return s


def draw_SVG_fract(depth, length, x, y, cur):
    style = {'stroke': '#000000', 'stroke-width': '2', 'fill': 'none'}
    elem = cur.add(inkex.PathElement())
    elem.update(**{
    'style': style,
    'inkscape:label': 'Cantor',
    'd': generate_my_fract_part(depth, x, y, length)})
    return elem


class Mufract(inkex.EffectExtension):
    def add_arguments(self, pars):
        pars.add_argument("--depth", type=int, default=2, help="Depth")
        pars.add_argument("--length", type=float, default=100.0, help="Side Length")
        pars.add_argument("--x", type=float, default=0.0, help="X coord.")
        pars.add_argument("--y", type=float, default=0.0, help="Y coord.")

    def effect(self):
        cur = self.svg.get_current_layer()
        depth = self.options.depth
        length = self.options.length
        x = self.options.x
        y = self.options.y
        draw_SVG_fract(depth, length, x, y, cur)


if __name__ == '__main__':
    Mufract().run()
