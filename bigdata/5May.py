# que1

# print(1)
# print(2)
# for i in range(3,51):
#     if (i%3 == 0) and (i%5==0):
#         print("FizzBuzz")
#     elif (i%3==0):
#         print("Fizz")
#     elif (i%5==0):
#         print("Buzz")
#     else:
#         print(i)


# que2
# for outer in range(1,5):
#     c = 0
#     for inner in range(1,8-outer+1):
#         if(inner < outer):
#             print(" ",end=" ")
#         elif(c==0):
#             print("1",end=" ")
#             c=1
#         elif(c==1):
#             print("0",end=" ")
#             c=0
#     print()

# que3
# for outer in range(1,6):
#     c=0
#     for k in range(0,5-outer):
#         print(" ",end=" ")
#     for inner in range(1,2*outer):
#         if(c==0):
#             print("*",end=" ")
#             c=1
#         elif(c==1):
#             print(" ",end=" ")
#             c=0
#     print()

# for outer in range(1,5):
#     c=0
#     for inner in range(0,outer):
#         print(" ",end=" ")
#     for inner in range(1,2*(5-outer)):
#         if(c==0):
#             print("*",end=" ")
#             c=1
#         elif(c==1):
#             print(" ",end=" ")
#             c=0
#     print()


#  que4
for outer in range(0,7):
    a=1
    for inner in range(0,outer+1):
        if(inner == 0):
            print(1,end=" ")
        else: 
            a = a*(outer-inner+1)//inner
            print(a,end=" ")

    print()