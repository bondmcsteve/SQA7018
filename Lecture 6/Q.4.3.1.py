"""This problem is based on Question 4.3.1 from the textbook"""

"""Rewrite the list of lambda functions created in Example E4.10 using a single
list comprehension."""

flist = [lambda x: 1,
         lambda x: x,
         lambda x: x**2,
         lambda x: x**3]

"""This function uses if-else function for lambda"""
flist2 = [lambda x, poly=p: x**poly if p>0 else 1 for p in range(4)]

"""This line does not use if-statement for lambda function"""
flist3 = [lambda x, poly2 = p2: x**p2 for p2 in range(0,4)]

print(flist[3](5))
print(flist2[3](5))
print(flist3[3](5))

