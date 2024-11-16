"""Self coding session for Problem 4.3.1"""

#Define a function for trace calculation
def trace_calculate(matrix):
    """Do note we need to return the length of matrix in form of int and make it iterable"""
    return sum(matrix[i][i] for i in range(len(matrix)))

#Test case
matrix = [[1,2,3],
          [4,5,6],
          [7,8,9]]

trace_val = trace_calculate(matrix)
print("The calculated trace for the matrix is :" + str(trace_val))

print(type(len(matrix)))