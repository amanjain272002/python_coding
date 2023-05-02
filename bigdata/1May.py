# que1
# n = int(input())
# for outer in range(1,n):
#     for k in range(1,n-outer):
#         print(" ",end="")
#     for inner in range(1,2*outer):
#         if( inner %2 == 0):
#             print(" ",end="")
#         else:
#             print("*",end="")
#     print()    

#que2
# n = int(input())
# for outer in range(1,n):
#     for k in range(1,outer):
#         print(" ",end="")
#     for inner in range(1,2*(n-outer)):
#         if(inner%2==0):
#             print(" ",end="")
#         else:
#             print("*",end="")
#     print()

# que3

n = int(input())
for outer in range(1,n):
    for k in range(1,n-outer):
        print(" ",end="")
    for inner in range(1,outer+1):
        print("*",end="")
    print()