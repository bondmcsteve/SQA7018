a = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
b = [4, 2, 6, 1, 5, 0, 3]

res_a = [a[x] for x in b] #Takes elements in b, and maps it to a
res_b = [a[x] for x in sorted(b)] #Sorts element in b, then map to a
res_c = [a[b[x]] for x in b] #b map to b, then map to a. Follow index
res_d = [x for (y,x) in sorted(zip(b,a))]
"""zip produces tuples of a,b. Sorted using b as enumerating val.
Later on, the loop extracts the x value from the tuples based on current arrangement"""

#print(res_a)
#print(res_b)
#print(res_c)
print(res_d)