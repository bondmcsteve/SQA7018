def generate_rule30(num_generations=20, row_width=80):
    # Create initial row with a single ‘on’ cell in the center
    current_row = [' ' for _ in range(row_width)]
    current_row[row_width // 2] = '*'  # Middle cell ‘on’

    # Rule 30 mapping based on 3-cell parent states (left, center, right)
    rule30 = {
        '***': ' ',  # 111 → 0
        '** ': ' ',  # 110 → 0
        '* *': ' ',  # 101 → 0
        '*  ': '*',  # 100 → 1
        ' **': '*',  # 011 → 1
        ' * ': '*',  # 010 → 1
        '  *': '*',  # 001 → 1
        '   ': ' '   # 000 → 0
    }

    # Display initial row
    print(''.join(current_row))

    # Generate subsequent generations
    for _ in range(num_generations - 1):
        new_row = [' ' for _ in range(row_width)]
        for i in range(1, row_width - 1):
            # Get states of left, center, and right cells
            parent_state = ''.join(current_row[i - 1:i + 2])
            # Determine new state using Rule 30
            new_row[i] = rule30[parent_state]
        # Update current row and print it
        current_row = new_row
        print(''.join(current_row))

# Call the function to display rows generated by Rule 30
generate_rule30()


"""Understand Rule 30:

Rule 30 specifies that the state of each cell in the next generation depends on its current state and the states of its two neighbors.
The rule can be expressed in binary as 00011110, where each combination of parent states corresponds to an "on" or "off" state in the child.
Define the Transition Rules:

Map each combination of three cells (current cell and two neighbors) to its next state. For Rule 30:
111 → 0 (off)
110 → 0 (off)
101 → 0 (off)
100 → 1 (on)
011 → 1 (on)
010 → 1 (on)
001 → 1 (on)
000 → 0 (off)
Implement the Automaton:

Initialize the row with a single "on" cell in the center and the rest "off".
For each generation, determine the new state of each cell by applying Rule 30.
Display each generation using '*' for "on" and ' ' for "off".
"""