"""Playground with generator"""
import sys

# Declaring the generator function
def generate_evens_with_yield(limit):
    num = 0
    while num <= limit:
        if num % 2 == 0:
            yield num
        num += 1
"""Apparently, the generator looks very much similar to that of typical loop 
but only uses yield for return value"""

""""Generator returns value on the fly, good when handling big data 
so that the data does not have to be stored on memory"""

# Create the generator
gen_evens = generate_evens_with_yield(1000000)

# Check the memory used by the generator
print("Memory used by the generator: ", sys.getsizeof(gen_evens), "bytes")

# Use the generator to print first 10 even numbers (mechanism illustration)
for i, even in enumerate(gen_evens):
    if i < 10:
        print(even)

def generate_evens_without_yield(limit):
    evens = []
    num = 0
    while num <= limit:
        if num % 2 == 0:
            evens.append(num)
        num += 1
    return evens

"""Generate the even numbers with limit being 1 million"""
evens_list = generate_evens_without_yield(1000000)

""""Ascertain the memory used to operate the loop function without using generator"""
print("Memory used by the list: ", sys.getsizeof(evens_list), "bytes")

# Use the loop to print first 10 even numbers (mechanism illustration)
for i, even in enumerate(evens_list):
    if i < 10:
        print(even)