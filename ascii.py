import numpy as np


def rect_action_input():
    """Prompts user for an action and returns their input."""
    prompt = """
    Choose what to do:
    a) Create a new rectangle
    b) Change a rectangle's fill
    c) Move a rectangle
    d) Clear the canvas
    """
    print(prompt)
    return input('Enter your selection:  ')


def choose_rectangle(rectangle_info):
    """Prompt for user to input which rectangle they will change."""

    rect_id = int(input("Input rectangle ID to edit:  "))

    return rect_id

def clear_rectangle_info():
    """creates empty dict to store rectangles."""
    rect_info = {}
    return rect_info

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

def store_rectangle(rectangle_info, fill_char, start_x, end_x, start_y, end_y):
    """stores the rectangle in a dictionary with ID."""
    # stores rectangle info
    rect_id = len(rectangle_info) + 1
    rectangle_info[rect_id] = [fill_char, start_x, end_x, start_y, end_y]

    return rectangle_info


def change_char(canvas, rectangle_info): 
    """Changes the rectangle's fill characters for selected."""
    # gets the rect id
    rect_id = choose_rectangle(rectangle_info)

    canvas_len = len(canvas[0])
    canvas_height = len(canvas)

    # gets the rect info from dict
    start_x = rectangle_info[rect_id][1]
    end_x = rectangle_info[rect_id][2]
    start_y = rectangle_info[rect_id][3]
    end_y = rectangle_info[rect_id][4]
    char = input('Input a new fill character:  ')

    rectangle_info[rect_id] = [char, start_x, end_x, start_y, end_y]
    return rectangle_info

def axis_shift_input():
    """prompts user for which axis they'd like to shift."""
    
    axis = input('Which axis would you like to shift? (x or y):  ')
    
    return axis


def shift_rectangles(rectangle_info, canvas, num=0):
    """shifts the selected rectangle."""


    rect_id = choose_rectangle(rectangle_info)
    axis = axis_shift_input()
    num = int(input('How many spaces would you like to shift it?  '))

    # gets the info of the selected rectangle
    fill_char = rectangle_info[rect_id][0] 
    start_x = rectangle_info[rect_id][1] 
    end_x = rectangle_info[rect_id][2] 
    start_y = rectangle_info[rect_id][3] 
    end_y = rectangle_info[rect_id][4]

    #updates the info depending on axis input
    if axis == 'x':
        start_x += num
        end_x += num
    if axis == 'y':
        start_y += num
        end_y += num

    ## update info in dictionary
    rectangle_info[rect_id] = [fill_char, start_x, end_x, start_y, end_y]
    return rectangle_info


def update_canvas(canvas, rectangle_info):
    """ updates the canvas based on the rectangle attributes."""
    canvas = create_blank_canvas()
    for rectangle in rectangle_info:
        fill_char = rectangle_info[rectangle][0]
        start_x = rectangle_info[rectangle][1]
        end_x = rectangle_info[rectangle][2]
        start_y = rectangle_info[rectangle][3]
        end_y = rectangle_info[rectangle][4]

        # updates the canvas with rectangle info
        j = 0
        while j < 10:
            if j >= start_y and j <= end_y:
                i = 0
                while i < 10:
                    if i >= start_x and i <= end_x:
                        canvas[j][i] = fill_char
                    i += 1
            j += 1

    return canvas


def validate_start_val(start_val):
    """validates start value."""
    if start_val >=0 and start_val <= 9:
        pass
    else:
        start_val = int(input("Invalid! Input start value (1-10):  "))


def validate_end_val(start_val, end_val):
    """validates end value."""
    if end_val <= 9 and end_val >= start_val:
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
    """prompts user to create and edit rectangle."""
    
    #intro message
    print('Welcome to Make a Rectangle!')
    print('------------------------')
   
    ## create blank canvas
    canvas = create_blank_canvas()
    rectangle_info = clear_rectangle_info()
    continue_playing = input('Would you like to play? (Yes/No)?  ')
    
    while continue_playing == 'Yes' or continue_playing == 'yes':
        user_choice = rect_action_input()
        
        ## options for different choices
        if user_choice == 'a':
            start_x = int(input("Start rectangle in column (0-9):  "))
            # form validation
            validate_start_val(start_x)
            end_x = int(input("End rectangle in column (0-9)):  "))
            validate_end_val(start_x, end_x)
            
            start_y = int(input("Start rectangle in row (0-9):  "))
            # form validation
            validate_start_val(start_x)
            end_y = int(input("End rectangle in row (0-9):  "))
            validate_end_val(start_y, end_y)
            fill_char = input("Choose a single character to fill rectangle:  ")
            if len(fill_char) > 1:
                fill_char = input("Error! Choose a single character:  ")
            # updates the canvas
            new_canvas = create_rectangle(start_x, start_y, 
            end_x, end_y, fill_char, canvas)
            rectangle_info = store_rectangle(rectangle_info, fill_char, start_x, end_x, start_y, end_y)
            # updates canvas to be the new canvas 
            canvas = update_canvas(canvas, rectangle_info)
            print_canvas(canvas)
            
        #option to change fill character
        if user_choice == 'b':
            rectangle_info = change_char(canvas, rectangle_info)
            canvas = update_canvas(canvas, rectangle_info)
            print_canvas(canvas)
        if user_choice == 'c':
            rectangle_info = shift_rectangles(rectangle_info, canvas)
            canvas = update_canvas(canvas, rectangle_info)
            print_canvas(canvas)

        if user_choice == 'd':
            rectangle_info = clear_rectangle_info()
            canvas = create_blank_canvas()

        continue_playing = input('Would you like to keep playing? (Yes/No)?  ')
    
    print('Thanks for playing!')

if __name__ == "__main__":
    prompt_user()