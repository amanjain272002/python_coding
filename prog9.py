from math import sqrt
flag = 0
n = int(input())
for i in range(2,int(sqrt(n))+1):
    if (n%i==0):
        flag = 1
        break

if(flag==1):
    print("prime number ")
else:
    print("Not prime")

