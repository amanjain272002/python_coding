from math import sqrt
n = int(input())
a = int(sqrt(5*n**2+4))
b = int(sqrt(5*n**2-4))

if (a*a == 5*n**2+4) or (b*b == 5*n**2-4 ):
    print("yes ")
else:
    print("no")

