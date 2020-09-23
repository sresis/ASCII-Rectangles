
import numpy as np

def create_blank_canvas(canvas_len=10, canvas_height=10):
    """ Create a blank canvas."""
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
    return adj_matrix

def create_rectangle(start_x, start_y, end_x, end_y, fill_char):
    """ Creates a rectangle."""
    canvas = create_blank_canvas()
    canvas_len = len(canvas)
    canvas_height = len(canvas[0])

    j = 0
    while j < canvas_len:
        if j >= start_y and j <= end_y:
            i = 0
            while i < canvas_height:
                if i >= start_x and i <= end_x:
                    canvas[j][i] = fill_char
                i += 1
        j += 1
    return canvas

def change_char(char): 
    """Changes the rectangle's fill characters."""
    # get the rectangle

    # for each non-blank character, replace it with new char
    


print(create_rectangle(1, 1, 3, 8, 'x'))
print(create_rectangle(1, 1, 3, 4, 'o'))
