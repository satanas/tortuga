#!/usr/bin/env python

import cairo

surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, 256, 256)
ctx = cairo.Context(surface)
ctx.scale(256, 256)
ctx.show_page()


