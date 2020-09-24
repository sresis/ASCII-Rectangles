
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
## need to store existing canvas somewhere
def create_rectangle(start_x, start_y, end_x, end_y, fill_char, canvas):
    """ Creates a rectangle."""
    
    canvas_len = 10
    canvas_height = 10

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

def validate_start_val(start_val):
    """validates start value."""
    if start_val >=1 and start_val <= 10:
        pass
    else:
        start_val = int(input("Invalid! Input start value (1-10):  "))

def prompt_user():
    """prompts user to create rectangle."""
    
    #intro message
    print('Welcome to Make a Rectangle!')
    print('------------------------')
   
    ## create blank canvas
    canvas = create_blank_canvas()

    continue_playing = input('Would you like to play? (Yes/No)?  ')
    
    while continue_playing == 'Yes':

        ## prompt for inputs
        start_x = int(input("Start rectangle in column (1-10):  "))
        # form validation
        validate_start_val(start_x)
        end_x = int(input("End rectangle in column (1-10):  "))
        start_y = int(input("Start rectangle in row (1-10):  "))
        # form validation
        validate_start_val(start_x)
        end_y = int(input("End rectangle in row (1-10):  "))
        fill_char = input("Choose a single character to fill rectangle:  ")
        new_canvas = create_rectangle(start_x, start_y, 
        end_x, end_y, fill_char, canvas)
        print(new_canvas)
        #resets canvas to be the new canvas 
        canvas = new_canvas



        continue_playing = input('Would you like to play? (Yes/No)?  ')

if __name__ == "__main__":
    prompt_user()