from display import *
from draw import *
import math

s = new_screen()
c = [ 102, 61, 20]
# c = [0,255,0]

# #octants 1 and 5
# draw_line(0, 0, XRES-1, YRES-1, s, c)
# draw_line(0, 0, XRES-1, YRES / 2, s, c) 
# draw_line(XRES-1, YRES-1, 0, YRES / 2, s, c)

# #octants 8 and 4
# c[BLUE] = 255;
# draw_line(0, YRES-1, XRES-1, 0, s, c);  
# draw_line(0, YRES-1, XRES-1, YRES/2, s, c);
# draw_line(XRES-1, 0, 0, YRES/2, s, c);

# #octants 2 and 6
# c[RED] = 255;
# c[GREEN] = 0;
# c[BLUE] = 0;
# draw_line(0, 0, XRES/2, YRES-1, s, c);
# draw_line(XRES-1, YRES-1, XRES/2, 0, s, c);

# #octants 7 and 3
# c[BLUE] = 255;
# draw_line(0, YRES-1, XRES/2, 0, s, c);
# draw_line(XRES-1, 0, XRES/2, YRES-1, s, c);

# #horizontal and vertical
# c[BLUE] = 0;
# c[GREEN] = 255;
# draw_line(0, YRES/2, XRES-1, YRES/2, s, c);
# draw_line(XRES/2, 0, XRES/2, YRES-1, s, c);

# for i in range(250,501):
#     c = [255,0,0]
#     draw_line(0,i,i,YRES,s,c)
#     c = [0,255,0]
#     draw_line(0,YRES-i,i,0,s,c)
#     c = [0,0,255]
#     draw_line(XRES,i,YRES-i,YRES,s,c)
#     c = [255,255,0]
#     draw_line(XRES,YRES-i,YRES-i,0,s,c)

def draw_tree(x0,y0,color,angle,length,depth):
    if depth:
        x1 = x0 + int(math.cos(math.radians(angle)) * length * 12)
        y1 = y0 + int(math.sin(math.radians(angle)) * length * 12)
        draw_line(x0,y0,x1,y1,s,color)
        next_c = [ color[0]-3, color[1]+10, color[2]]
        draw_tree(x1, y1, next_c, angle + 32, length*3/4, depth-1)
        draw_tree(x1, y1, next_c, angle - 32, length*3/4, depth-1)
draw_tree(250, 1, c, 90, 8, 12)

display(s)
save_ppm(s, 'binary.ppm')
save_ppm_ascii(s, 'ascii.ppm')
save_extension(s, 'img.png')