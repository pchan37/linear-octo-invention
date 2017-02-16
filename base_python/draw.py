from display import *

def draw_line(screen, x0, y0, x1, y1, color):
    # draw_line1(screen, x0, y0, x1, y1, color)
    draw_line2(screen, x0, y0, x1, y1, color)

def draw_line1( screen, x0, y0, x1, y1, color ):
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
    plot(screen, color, x0, y0)
    
def main():
    screen = new_screen()
    draw_line(screen, 0, 0, 20, 10, [255, 0, 255])
    
if __name__ == '__main__':
    main()
