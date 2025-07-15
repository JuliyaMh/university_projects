#!/usr/bin/env python
# coding=utf-8
import sys
import inkex
import math

s = ''

def generate_my_fract_part(depth, length, angle=0):
    global s
    if depth == 0:
        s += ' l ' + str(math.cos(angle) * length) + ', ' + str(-1 * math.sin(angle) * length)
    else:
        generate_my_fract_part(depth - 1, length / 3, angle)
        generate_my_fract_part(depth - 1, length / 3, angle + math.pi / 3)
        generate_my_fract_part(depth - 1, length / 3, angle - math.pi / 3)
        generate_my_fract_part(depth - 1, length / 3, angle)


def generate_my_fract(depth, length):
    angle = 0
    for i in range(3):
        generate_my_fract_part(depth, length, angle)
        angle -= math.pi / 3 * 2


def draw_SVG_fract(depth, length, x, y, cur):
    global s
    s = 'M ' + str(x) + ', ' + str(y)
    generate_my_fract(depth, length)
    style = {'stroke': '#000000', 'stroke-width': '2', 'fill': 'none'}
    elem = cur.add(inkex.PathElement())
    elem.update(**{
    'style': style,
    'inkscape:label': 'Koch',
    'd': s})
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
