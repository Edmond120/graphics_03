from display import *
from matrix import *


def draw_lines( matrix, screen, color ):
    pass

def add_edge( matrix, x0, y0, z0, x1, y1, z1 ):
    pass

def add_point( matrix, x, y, z=0 ):
    pass

def draw_line( x0, y0, x1, y1, screen, color ):
	if(x0 > x1): #swap points so that x0 is the smaller one
		tmp = x0
		x0 = x1
		x1 = tmp
		tmp = y0
		y0 = y1
		y1 = tmp
	A = y1 - y0
	B = -1 * (x1 - x0)
	if(B == 0):
		if(y0 < y1):
			for y in xrange(y0,y1):
				plot(screen,color,x0,y)
		else:
			for y in xrange(y1,y0):
				plot(screen,color,x0,y)
		return
	slope = A / (B * -1.0) #todo check for divide by 0
	C = y1 - x1 * slope
	if(slope >= 0 and slope <= 1): #octant 1
		d = 2 * A + B
		while x0 <= x1:
			plot(screen,color,x0,y0)
			if(d > 0):
				y0 += 1
				d += 2 * B
			x0 += 1
			d += 2 * A
		return
	elif(slope > 1): #octant 2
		d = A + 2 * B
		while y0 <= y1:
			plot(screen,color,x0,y0)
			if(d > 0):
				x0 += 1
				d -= 2 * A
			y0 += 1
			d -= 2 * B
		return
	elif(slope < 0 and slope >= -1):
		d = 2 * A + B
		while x0 <= x1:
			plot(screen,color,x0,y0)
			if(d > 0):
				y0 -= 1
				d -= 2 * B
			x0 += 1
			d -= 2 * A
		return
	elif(slope < -1):
		d = A + 2 * B
		while abs(y0) >= abs(y1):
			plot(screen,color,x0,y0)
			if(d > 0):
				x0 += 1
				d += 2 * A
			y0 -= 1
			d -= 2 * B
	return
