"""This problem is based on Problem 4.2.1 in the textbook"""
# 1st and 2nd color = Significant value
# 3rd color = Decimal multiplier
# 4th color = Tolerance

def get_resistor_value(bands):
    """Translate color bands into a resistance value and tolerance."""
    # Define color code dictionaries with full names
    significant_figures = {
        'black': 0, 'brown': 1, 'red': 2, 'orange': 3, 'yellow': 4,
        'green': 5, 'blue': 6, 'violet': 7, 'gray': 8, 'white': 9
    }
    multipliers = {
        'black': 1, 'brown': 10, 'red': 100, 'orange': 1000, 'yellow': 10000,
        'green': 100000, 'blue': 1000000, 'violet': 10000000, 'gray': 100000000, 'white': 1000000000
    }
    tolerances = {
        'brown': 1, 'red': 2, 'green': 0.5, 'blue': 0.25, 'violet': 0.1,
        'gray': 0.05, 'gold': 5, 'silver': 10
    }

    # Extract the colors from the bands
    color1, color2, multiplier_color, tolerance_color = bands

    # Calculate significant digits
    digit1 = significant_figures[color1]
    digit2 = significant_figures[color2]
    multiplier = multipliers[multiplier_color]
    tolerance = tolerances[tolerance_color]

    # Calculate resistance value
    resistance = (digit1 * 10 + digit2) * multiplier

    return resistance, tolerance


print(get_resistor_value(['violet', 'yellow', 'red', 'green']))  # Expected output: (7400, 0.5)

"""Standard Resistor Color Code (for reference):
Significant Figures and Multipliers:

Black: 0, multiplier 
1
0
0
10 
0

Brown: 1, multiplier 
1
0
1
10 
1

Red: 2, multiplier 
1
0
2
10 
2

Orange: 3, multiplier 
1
0
3
10 
3

Yellow: 4, multiplier 
1
0
4
10 
4

Green: 5, multiplier 
1
0
5
10 
5

Blue: 6, multiplier 
1
0
6
10 
6

Violet: 7, multiplier 
1
0
7
10 
7

Gray: 8, multiplier 
1
0
8
10 
8

White: 9, multiplier 
1
0
9
10 
9

Tolerance:

Brown: ±1%
Red: ±2%
Green: ±0.5%
Blue: ±0.25%
Violet: ±0.1%
Gray: ±0.05%
Gold: ±5%
Silver: ±10%"""