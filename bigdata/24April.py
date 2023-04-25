# que1

import math
# k = 0
# num = int(input())

# if (num == 1) or (num==2):
#     print("YES prime number ")

# else:
#     for i in range(2, int(math.sqrt(num))+1):
#         if (num % i == 0):
#             k = 1
#             break
#     if (k == 1):
#         print("NO prime number")
#     else:
#         print("YES prime number ")


#  que2
num1 = int(input("Enter num1 : "))
num2 = int(input("Enter num2 : "))
k = 0
if (num1 < num2):
    if(num2%num1 == 0):
        k=1
    else:
        for i in range(2, int(math.sqrt(num1))+1):
            if (num1 % i == 0) and (num2 % i == 0):
                k = 1
                break

elif (num1 > num2):
    if(num1%num2 == 0):
        k = 1
    else: 
        for i in range(2, int(math.sqrt(num2))+1):
            if (num1 % i == 0) and (num2 % i == 0):
                k = 1
                break

else:
    k = 1
# print(k)
if (k == 1):
    print("No coprime ")
else:
    print("Yes coprime")
