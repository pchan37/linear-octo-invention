from display import *
from draw import *

screen = new_screen()
color = [ 0, 255, 0 ]

draw_line1(screen, 0, 0, 20, 10, color)
draw_line2(screen, 0, 0, 10, 20, color)
draw_line7(screen, 10, 20, 0, 0, color)

display(screen)
save_extension(screen, 'img.png')
