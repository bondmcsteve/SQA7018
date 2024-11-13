"""This problem is based on Question 4.3.1 from the textbook"""

"""Rewrite the list of lambda functions created in Example E4.10 using a single
list comprehension."""

flist = [lambda x:1,
         lambda x:x,
         lambda x: x**2,
         lambda x:x**3]

flist2 = [lambda x, square=s: x**square for s in range(4)]
print(flist[3][5])
print(flist2[3][5])