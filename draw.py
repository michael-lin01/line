from display import *

def draw_line(x0, y0, x1, y1, screen, color):
    x0,y0,x1,y1 = int(x0),int(y0),int(x1),int(y1)
    #vertical line
    if x0 == x1:
        if y1 < y0:
            y0,y1 = y1,y0
        while y0 <= y1:
            plot(screen, color, x0, y0)
            y0 += 1
    # horizontal line
    elif y0 == y1:
        if x1 < x0:
            x0,x1 = x1,x0
        while x0 <= x1:
            plot(screen, color, x0, y0)
            x0 += 1
    else:
        if x1 < x0:
            x0,y0,x1,y1 = x1,y1,x0,y0
        A = y1-y0
        B = x0-x1
        slope = (y1-y0)/(x1-x0)
        # octants 1 and 5
        if slope >= 0 and slope <= 1:
            d = 2*A + B
            A,B = 2*A, 2*B
            while x0 <= x1:
                plot(screen, color, x0, y0)
                if d > 0:
                    y0 += 1
                    d += B
                x0 += 1
                d += A
        # octants 2 and 6
        elif slope > 1:
            d = A + 2*B
            A,B = 2*A, 2*B
            while y0 <= y1:
                plot(screen, color, x0, y0)
                if d < 0:
                    x0 += 1
                    d += A
                y0 += 1
                d += B
        # octants 4 and 8
        elif slope >= -1 and slope < 0:
            d = 2*A + B
            A,B = 2*A, 2*B
            while x0 <= x1:
                plot(screen, color, x0, y0)
                if d < 0:
                    y0 -= 1
                    d -= B
                x0 += 1
                d += A
        # octants 3 and 7
        elif slope < -1:
            d = A - 2*B
            A,B = 2*A, 2*B
            while y0 >= y1:
                plot(screen, color, x0, y0)
                if d > 0:
                    x0 += 1
                    d += A
                y0 -= 1
                d -= B
