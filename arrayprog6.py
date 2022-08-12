n = int(input())
lst = [1,2,3,4,5,6]
multiply = 1
for i in range(0,len(lst)):
    multiply = multiply *int(lst[i])
multiply= multiply%n
print(multiply)