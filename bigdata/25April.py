# pattern que 1

# for outer in range(0, 4):
#     k = 65
#     for inner in range(0, outer+1):
#         print(chr(k), end=" ")
#         k = k+1
#     print()

# pattern que 2
# k = 65
# for outer in range(0, 4):
#     for inner in range(0, outer+1):
#         print(chr(k), end=" ")
#         k = k+1
#     print()

# pattern que 3
# up = 6
# dn = 4
# for outer in range(0,6):
#     if(outer%2==0):
#         for inner in range(0,up):
#             print("*",end=" ")
#         if(outer == 4):
#             print("*",end=" ")    
#         up = up - outer - 1

#     else:
#         for inner in range(0,dn):
#             print("*",end=" ")
#         dn = dn // 2
#     print()