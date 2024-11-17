def power_set(S):
    """Generate all subsets of set S (the power set) using a generator."""
    # Convert the set to a tuple to work with ordered elements
    elements = tuple(S)
    n = len(elements)

    # There are 2^n possible subsets for a set with n elements
    for i in range(1 << n):  # 1 << n is 2^n, this is left bitwise shift
        subset = {elements[j] for j in range(n) if (i & (1 << j))}
        yield subset


S = {1, 2, 3}
for subset in power_set(S):
    print(subset)

"""
How this program works:
1. Declare the set
2. Initiate for loop, which iterates through function power_set() to print the outputs
of the function
3. Within power_set(), take input (parent set) and then convert it into tuple within
variable elements 
4. The tuple length is calculated using len(), and is stored in variable n 
5. A for-loop, which iterates in such n is the amount of  left bitwise shifting, is initialised. 
(Example: If n = 3, then 1 << n means the output is 0001 -> 1000 = 8)
As such 1<<n becomes i's max value in looping.
6. Left bitwise shifting is used to compute the possible amount of subset in superset function,
which exactly 2^n.
7. Consequently, the for-loop iterates in an amount such that it is equal to that of total
possible subset in the superset.
8. Within the for-loop, the variable subset runs a list comprehension that iterates for the
amount of possible subsets by using bitwise left shift and AND logic comparison.
9. i-th iteration rotates j counter, till  i = 8. As long the convolution between i and j gives out
non-zero answer, it should spew out bit value corresponding to position of elements in the list.
10. As such, for j-bit, we can think of (001) to be element 1, (010) to be element 2, and (100) to be
element 3.
"""