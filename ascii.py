
import numpy as np
def create_rectangle(start_x, start_y, end_x, end_y, fill_char):
    """ Creates a rectangle."""
    
    # dimensions of canvas is 10x10
    canvas_len = 10
    canvas_height = 10
    
    # makes the row of the canvas length
    row = []
    i = 0
    while i < canvas_height:
        row.append(' ')
        i += 1
    
    # makes canvas_len number of rows
    matrix = []
    i = 0
    while i < canvas_len:
        matrix.append(row)
        i += 1
    
    # make rows on top of each other
    adj_matrix = np.array(matrix)

    j = 0
    while j < canvas_len:
        if j >= start_y and j <= end_y:
            i = 0
            while i < canvas_height:
                if i >= start_x and i <= end_x:
                    adj_matrix[j][i] = fill_char
                i += 1
        j += 1
    print(adj_matrix)


create_rectangle(1, 1, 3, 1, 'x')

