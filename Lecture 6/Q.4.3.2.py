nmax = 5
x = [1]
for n in range(1,nmax+2):
    print(x)
    x = [([0]+x)[i] + (x+[0])[i] for i in range(n+1)]