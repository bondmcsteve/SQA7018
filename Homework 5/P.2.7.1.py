# This homework problem is based on Problem 2.7.1 from the textbook

# We want to create a program that checks, for a game of Scrabble, whether
# an input word of either horizontal or downward character order
# can fit within 15x15 Scrabble grid.

# Expected inputs: (1) word, (2) direction or orientation, (3) starting cell or position

# We begin with defining a function that checks for the condition
def can_fit_in_grid(start_pos, direction, word):
    #Grid dimension initialization
    grid_size = 15

    #Parsing row and column from start_pos
    row_letter = start_pos[0].upper() #Conversion to uppercase for standardization
    col_number = int(start_pos[1:]) #Conversion of column number input to int type

    # Calculation for the row index by mapping the letters to numerical equivalent as such
    # 'A' = 1, 'B' = 2, 'C' = 3, ...
    row_index = ord(row_letter) - ord('A') # ord() converts char to its unicode equivalent
    col_index = col_number - 1 # Index-1 remapped to Index-0 for looping

    # Bound-check based on direction
    if direction == 'across':
        # Checking if word fits horizontally
        if col_index + len(word) <= grid_size:
            return True

    elif direction == 'down':
        if row_index + len(word) <= grid_size:
            return True

    return False #If the word does not fit, and direction-check fails (Wrong input)

# Test cases
print(can_fit_in_grid("G7", "across", "HELLO"))
print(can_fit_in_grid("M12", "down", "SCRABBLE"))
