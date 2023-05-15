# normal fibonacci
# def fibo(n):
#     a = 0
#     b = 1
#     while(n>0):
#         c = a+b
#         print(c)
#         n=n-1
#         a = b
#         b = c
    
# n = int(input("Enter number of terms "))
# fibo(n)

#  using generators
def fibo(n):
    a = 0
    b = 1
    while(n>0):
        c = a+b
        yield c
        n=n-1
        a = b
        b = c
    
n = int(input("Enter number of terms "))
x = fibo(n)
# print(x.__next__())
# print(x.__next__())
# print(x.__next__())
# print(x.__next__())
# print(x.__next__())
for i in x:
    print(i)