from display import *

def draw_line(screen, x0, y0, x1, y1, color):
    dx = x1 - x0
    dy = y1 - y0

    
    
    if dx >= 0 and dy >=0:
        if dx >= dy:
            return draw_line1(screen, x0, y0, x1, y1, color)
        return draw_line2(screen, x0, y0, x1, y1, color)
            
    elif dx >= 0 and dy <= 0:
        if dx >= -dy:
            return draw_line8(screen, x0, y0, x1, y1, color)
        return draw_line7(screen, x0, y0, x1, y1, color)

    elif dx <= 0 and dy >=0:
        if -dx >= dy:
            return draw_line8(screen, x1, y1, x0, y0, color)
        return draw_line7(screen, x1, y1, x0, y0, color)
    else:
        if -dx >= -dy:
            return draw_line1(screen, x1, y1, x0, y0, color)
        return draw_line2(screen, x1, y1, x0, y0, color)
            
        
def draw_line1(screen, x0, y0, x1, y1, color):
    delta_x = x1 - x0
    delta_y = y1 - y0

    A = delta_y
    B = -delta_x

    d = 2 * A + B
    while x0 < x1:
        plot(screen, color, x0, y0)
        if d > 0:
            y0 += 1
            d += 2 * B
        x0 += 1
        d += 2 * A
    plot(screen, color, x1, y1)

def draw_line2(screen, x0, y0, x1, y1, color):
    delta_x = x1 - x0
    delta_y = y1 - y0

    A = delta_y
    B = -delta_x

    d = A + 2 * B
    while y0 < y1:
        plot(screen, color, x0, y0)
        if d < 0:
            x0 += 1
            d += 2 * A
        y0 += 1
        d += 2 * B
    plot(screen, color, x1, y1)

def draw_line7(screen, x0, y0, x1, y1, color):
    delta_x = x1 - x0
    delta_y = y1 - y0

    A = delta_y
    B = -delta_x

    d = A - 2 * B
    while y0 > y1:
        plot(screen, color, x0, y0)
        if d > 0:
            x0 += 1
            d += 2 * A
        y0 -= 1
        d -= 2 * B
    plot(screen, color, x1, y1)

def draw_line8(screen, x0, y0, x1, y1, color):
    delta_x = x1 - x0
    delta_y = y1 - y0

    A = delta_y
    B = -delta_x

    d = -2 * A + B
    while x0 < x1:
        plot(screen, color, x0, y0)
        if d < 0:
            y0 -= 1
            d -= 2 * B
        x0 += 1
        d += 2 * A
    plot(screen, color, x1, y1)
