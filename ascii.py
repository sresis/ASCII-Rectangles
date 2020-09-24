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

def change_char(char, canvas, start_x, end_x, start_y, end_y): 
    """Changes the rectangle's fill characters."""

    # for each non-blank character, replace it with new char
    canvas_len = 10
    canvas_height = 10

    j = 0
    while j < canvas_len:
        if j >= start_y and j <= end_y:
            i = 0
            while i < canvas_height:
                if i >= start_x and i <= end_x:
                    canvas[j][i] = char
                i += 1
        j += 1
    return canvas

def validate_start_val(start_val):
    """validates start value."""
    if start_val >=1 and start_val <= 10:
        pass
    else:
        start_val = int(input("Invalid! Input start value (1-10):  "))


def validate_end_val(start_val, end_val):
    """validates end value."""
    if end_val <= 10 and end_val >= start_val:
        pass
    else:
        end_val = int(input("Invalid! Input end value (1-10):  "))


def clear_all_shapes():
    """clears the canvas."""
    
    canvas = create_blank_canvas()
    return canvas
def print_canvas(canvas):
    """prints the canvas."""
    for item in canvas:
        new_row = ('').join(item)
        print(new_row)
    return canvas



def prompt_user():
    """prompts user to create rectangle."""
    
    #intro message
    print('Welcome to Make a Rectangle!')
    print('------------------------')
   
    ## create blank canvas
    canvas = create_blank_canvas()

    continue_playing = input('Would you like to play? (Yes/No)?  ')
    
    while continue_playing == 'Yes' or continue_playing == 'yes':

        ## prompt for inputs
        start_x = int(input("Start rectangle in column (1-10):  "))
        # form validation
        validate_start_val(start_x)
        end_x = int(input("End rectangle in column (1-10):  "))
        validate_end_val(start_x, end_x)
        
        start_y = int(input("Start rectangle in row (1-10):  "))
        # form validation
        validate_start_val(start_x)
        end_y = int(input("End rectangle in row (1-10):  "))
        validate_end_val(start_y, end_y)
        fill_char = input("Choose a single character to fill rectangle:  ")
        if len(fill_char) > 1:
            fill_char = input("Error! Choose a single character:  ")
        # updates the canvas
        new_canvas = create_rectangle(start_x, start_y, 
        end_x, end_y, fill_char, canvas)
        print_canvas(new_canvas)
        # updates canvas to be the new canvas 
        canvas = new_canvas
        
        #option to change fill character
        #need to only apply to current rectangle (use start and end values)
        make_new_char = input('Would you like to change the fill character?(Yes/No)  ')
        if make_new_char == 'yes' or make_new_char == 'Yes':
            new_char = input('Input a new fill character:  ')
            new_canvas = change_char(new_char, canvas, start_x, end_x, start_y, end_y)
            canvas = new_canvas
            print_canvas(new_canvas)

        print_canvas(canvas)



        continue_playing = input('Would you like to play? (Yes/No)?  ')

if __name__ == "__main__":
    prompt_user()