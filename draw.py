from display import *

def draw_line( x0, y0, x1, y1, screen, color ):
    # octant I
    if x1 < x0:
        x0,y0 = x1,y1
    A = y1-y0
    B = x0-x1
    d = 2*A + B
    while x0 <= x1:
        plot(screen, color, x0, y0)
        if d > 0:
            y0 += 1
            d += B
        x0 += 1
        d += A
