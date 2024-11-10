def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    return x / y


def power(x, y):
    return x ** y


def evaluate_rpn(expression):
    """Evaluate a Reverse Polish Notation (RPN) expression."""
    # Define a stack to store numbers
    stack = []

    # Define the operations as functions in a dictionary
    operations = {
        '+': add,
        '-': subtract,
        '*': multiply,
        '/': divide,
        '**': power
    }

    # Split the expression into tokens
    tokens = expression.split()

    for token in tokens:
        if token in operations:
            # Pop two operands from the stack
            operand2 = stack.pop()  # Right operand
            operand1 = stack.pop()  # Left operand

            # Perform the operation and push the result back onto the stack
            result = operations[token](operand1, operand2)
            stack.append(result)
        else:
            # Convert the token to a float and push it onto the stack
            stack.append(float(token))

    # The final result should be the only item left in the stack
    return stack.pop()


expression = "3 7 + 2 /"  # Equivalent to (3 + 7) / 2
result = evaluate_rpn(expression)
print("Result:", result)  # Expected output: 5.0

# Test with an expression using exponentiation
expression = "4 2 **"  # Equivalent to 4^2
result = evaluate_rpn(expression)
print("Result:", result)  # Expected output: 16.0
