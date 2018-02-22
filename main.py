from display import *
from draw import *
from matrix import *

screen = new_screen()
color = [ 255, 0, 0 ]
matrix = new_matrix()
print_matrix( matrix )
print "----"
print_matrix( ident( matrix ) )
#draw_lines( matrix, screen, color )
#display( screen )
#save_extension( screen, 'img.png' )
