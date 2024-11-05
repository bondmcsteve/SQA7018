# This problem is based on Problem 2.5.4 in the textbook. Refer to it for problem statement

# This problem concerns about straight line alkanes CnH(2n+2)
# We are to write a program to output the structural formula of such alkane given in stoichiometry

#Ex: Butane (n=4) shall be H3C-CH2-CH2-CH3
#Ex2: For stoich = 'C8H18' should be H3C-CH2-CH2-CH2-CH2-CH2-CH2-CH3

#The start and end points are of CH3 with inversion at the start. We can use function associated with reverse?

#We begin with function definition
def alkane_structure(n):
    if n < 2:
        return "n must be greater than 1"

    #Begin with the "head"
    structure = "H3C"

    #For the chain and repetitive part
    for i in range(n-2):
        structure += "-CH2"

    #For the end point
    structure += "-CH3"

    return structure

#n = 8 # Original code
n = int(input("Please enter the amount of carbon within the desired linear  alkane : "))
print(alkane_structure(n))
