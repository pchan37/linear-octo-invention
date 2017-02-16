from __future__ import division
from display import *
from draw import *

from math import floor, pi, cos, sin

screen = new_screen()
color = [ 120, 255, 120 ]

interval = pi / 16
def dy(theta):
    return sin(interval * theta)

def dx(theta):
    return cos(interval * theta)

for i in xrange(32):
    draw_line(screen, 250, 250, 250 + int(250 * dx(i)), 250 + int(250 * dy(i)), color)

display(screen)
save_extension(screen, 'img.png')
