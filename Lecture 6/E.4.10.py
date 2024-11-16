"""Using lambda functions in a list since it is also classified as objects"""

flist = [lambda x: 1,
         lambda x: x,
         lambda x: x**2,
         lambda x: x**3,
]

"""Consider that we wish to call upon lambda functions enclosed in a list as above,
 we can use the test cases below"""

#Compute input value of 5 using the 3rd lambda function
print(flist[3](5))

#Compute input value of 4 using the 2nd lambda function
print(flist[2](4))