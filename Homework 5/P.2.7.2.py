# This example is based on Problem 2.7.2 from the textbook.

# The question asks us to find the smallest factorial of n, or n! such that its value not divisible
# with the sum of its own digits.
# (Eg. Consider 6! where 6! = 720, and 720 cannot be divided by [7+2+0])

# We know we can split the program into two functions, one evaluating for the sum of digit,
# while another evaluates for the divisibility.

# Since we are finding the smallest n, we expect some kind of looping in divisibility evaluation

#Begin with fetching appropriate packages
import math

#Define the function for evaluating the sum of digit
def sum_of_digits(number):
    #Convert 'number' into iterable list, use for statement to iterate the list, and
    #then use sum() command to sum the iteration values
    return sum(int(digit) for digit in str(number))

#Define function for divisibility check
def find_smallest_n():
    n = 1 #Set the counter to 1
    while True: #Infinite loop until return condition is met
        factorial_n = math.factorial(n) #Evaluate the factorial of n
        digit_sum = sum_of_digits(factorial_n) #Evaluate the sum of digits of the factorial

        #Checking for divisibility
        if factorial_n % digit_sum != 0:
            return n
        n += 1 #Moving on to next value of n

# Main script
smallest_n = find_smallest_n()
print("The smallest positive integer n whose factorial is not divisible by the sum of its digits is: ", smallest_n)