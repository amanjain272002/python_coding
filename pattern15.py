import math 
k = 8
for outer in range(0,8):
    for star in range(0,k):
        print("*",end='')
    for line in range(k,16-k):
        print("-",end='')
    for star in range(16-k,16):
        print("*",end='')
    k =k-1

    print("\n")