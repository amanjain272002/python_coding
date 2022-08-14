n = int(input())
lst = []
for i in range(0,n):
    x= int(input())
    lst.append(x)
    
k =int(input())
for i in range(0,k):
    print(max(lst))
    lst.remove(max(lst))