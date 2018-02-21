from display import *
from draw import *
from matrix import *

screen = new_screen()
color = [ 255, 0, 0 ]
matrix = new_matrix()

draw_lines( matrix, screen, color )
display(screen)
save_extension(screen, 'img.png')
