from display import *
from draw import *
from matrix import *
from random import random

screen = new_screen()
color = [ 255, 0, 0 ]
matrix = [[1,2,3],[4,5,6]]
print "\nmatrix"
print_matrix( matrix )
print "\nident( matrix )"
print_matrix( ident( matrix ) )
print "\nother_matrix"
other_matrix = [[7,8],[9,10],[11,12]]
print_matrix( other_matrix )
print "\nmatrix_mult(matrix,other_matrix)"
print_matrix( matrix_mult( matrix, other_matrix ) )
print "\nmatrix"
matrix = [[0,250],[0,100],[0,0],[1,1]]
print_matrix( matrix )
print "\ntranslate 50,10"
matrix = matrix_mult(translate(matrix,50,10,0),matrix)
print_matrix( matrix )

#make picture

matrix = new_matrix(4,0)
lines = 500
px = 0
py = 0
for l in range(lines):
	x = l
	y = py + 1
	if(random() < 0.5):
		x-=2
	if(random() < 0.5):
		y-=2
	add_edge(matrix, px, py, 0, x, y, 0)
	px = x
	py = y

	draw_lines(matrix,screen,color)
for i in range(500):
	matrix = matrix_mult(translate(matrix,0,1,0),matrix)
	color = [0,int(random() * 250),int(random() * 250)]
	draw_lines(matrix,screen,color)

display( screen )
save_extension( screen, 'img.png' )
