import math


def print_matrix( matrix ):
	rows = len(matrix[0])
	for row in range( rows ):
		print '[ ',
		for col in matrix:
			p = str(col[row])
			if len(p) < 3:
				p = ' ' * (3 - len(p)) + p
			print p + ' ',
		print ']\n',

def ident( matrix ):
	l = len(matrix[0])
	m = new_matrix(rows=l,cols=l)
	for i in range( l ):
		m[i][i] = 1
	return m

#m1 * m2 -> m2
def matrix_mult( m1, m2 ):
    pass


def new_matrix(rows = 4, cols = 4):
    m = []
    for c in range( cols ):
        m.append( [] )
        for r in range( rows ):
            m[c].append( 0 )
    return m
