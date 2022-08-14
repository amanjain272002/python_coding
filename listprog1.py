n = int(input())
lst = []
for i in range(0,n):
    x= int(input())
    lst.append(x)

temp = lst[0]
lst[0]=lst[len(lst)-1]
lst[len(lst)-1] = temp
print(lst)