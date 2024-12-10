import random as random

random.seed(123) #Rerunning the program produces same random number sequence due to it running on same seed value

print(random.randint(0, 100))

for i in range(10):
    print(random.randint(0,100))

""""If we do not use seed, we will detach from seed, making it truly random"""

random.seed() # or if we omit this
print(random.randint(0, 100))

for i in range(10):
    print(random.randint(0,100))