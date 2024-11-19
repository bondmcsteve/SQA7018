""""This problem is based on Problem 4.3.1 in the textbook"""

def calculate_trace(matrix):
    """Calculate the trace of a square matrix using a list comprehension."""
    return sum(matrix[i][i] for i in range(len(matrix)))

# Example usage
M = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

N = [
    [10, 20],
    [30, 40, 50],
    [60, 70, 80]
]

trace = calculate_trace(N)
print("Trace of the matrix:", trace)  # Expected output: 15 (1 + 5 + 9)
