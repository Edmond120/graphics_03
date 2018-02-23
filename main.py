from display import *
from draw import *
from matrix import *

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
print "\ndraw_lines( matrix, screen, color)"
draw_lines( matrix, screen, color )
display( screen )
save_extension( screen, 'img.png' )
