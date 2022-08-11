n = int(input())
lst = []
for i in range(0,n):
    x= int(input())
    lst.append(x)

p = int(input("rotate element by "))

lst[:] = lst[p:n]+lst[0:p]
print(lst)

