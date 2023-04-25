# stri = input()
# # print(type(stri))
# if(type(stri) == str):
#     for i in range(0,len(stri)):
#         if (stri[i] != 'a')and(stri[i] != 'e')and(stri[i] != 'i')and (stri[i] != 'o') and (stri[i] != 'u') and (stri[i] != 'A')and(stri[i] != 'E')and(stri[i] != 'I')and (stri[i] != 'O') and (stri[i] != 'U'):
#             print(stri[i],end=" ")

# import copy
# org = [1,2,3,4]
# new_org = copy.copy(org)
# new_org[0] = 'a'
# print(org)
# print(new_org)

# mylist = [12,2,4,56,90]
# # mylist.append([12,23])
# # print(mylist)
# mylist.extend([12,23])
# print(mylist)

# my = ()
# print(type(my))
# my = (10)
# print(type(my))

my_tuple = ()  # create an empty tuple
k = my_tuple
print(id(my_tuple))
# later fill it in with values
my_tuple = (1, 2, 3)
print(id(my_tuple))
print()