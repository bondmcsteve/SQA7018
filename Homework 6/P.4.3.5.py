def power_set(S):
    """Generate all subsets of set S (the power set) using a generator."""
    # Convert the set to a tuple to work with ordered elements
    elements = tuple(S)
    n = len(elements)

    # There are 2^n possible subsets for a set with n elements
    for i in range(1 << n):  # 1 << n is 2^n
        subset = {elements[j] for j in range(n) if (i & (1 << j))}
        yield subset


S = {1, 2, 3}
for subset in power_set(S):
    print(subset)
