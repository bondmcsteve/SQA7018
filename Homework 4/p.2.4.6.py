# This homework is based on problem P.2.4.6 from the main textbook

# Refer to the question for more info on problem statement

# From the question, we understand that:
# 1. If n (input param.) is odd, counter is (n+1)/2
# 2. If n is even, counter is n/2
# 3. We need to discriminate between odd and even functions
# 4. And then run it in the loop as it multiplies with itself


# We begin with function definition,
def double_factorial(n):
    result = 1
    if n%2 == 0: #Check for condition which n is even
        for i in range(2, n+1, 2): # range(l-bound, u-bound, delta)
            result *= i #Multiply with previous self-multiplication
    else:
        for i in range(1, n+1, 2):
            result *= i
    return result #Return the result of self-multiplication to main script

def console_input(n): # Just a function to make this automated for user input
    print(n)
    double_factorial(n)
    print(double_factorial(n))

n = int(input("Enter n number:"))
console_input(n)

# Test cases
# n_odd = 7
# n_even = 8
# print(double_factorial(n_odd), double_factorial(n_even))
