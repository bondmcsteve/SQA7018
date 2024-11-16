""""We will be exploring the bitwise left shift operator"""

"""Begin Example 1: Simple Left Shift"""
""""Consider initial value below"""
num = 5 #Translates to 0000 0101 in binary

"""We can shift the the bits to left by one position as follows"""
result = num << 1 #0000 1010 = 8+2
print(result)

"""Question: What about to right shift?"""
result2 = num >> 1 #0000 0010 = 2
print(result2)

"""Example 2: Left Shift by Multiple Position"""
num3 = 3 #0000 0011
result3 = num3 << 2 #0000 1100 = 8 + 4 = 12
print(result3)

"""Example 3: Left shifting negative number"""
num4 = -4 #If 1s bit complement: 0000 0100 -> 1111 1011, 2's complement is 1111 1100
result4 = num << 1 #1111 1000 in 2's -> 0000 0111 -> 0000 1000 (Invert then plus 1)
print(result4)