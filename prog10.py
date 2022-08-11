n = int(input())
a= 0 ;b = 1;
lst  = []
lst.append(a)
lst.append(b)
for i in range(2,n+1):
    c = a+b
    lst.append(c)
    a = b
    b = c

print(n ," position is ",lst[n-1])