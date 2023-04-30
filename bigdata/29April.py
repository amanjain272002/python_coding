# st = set()
# print(type(st))

# st = set([1,2,3,4,5,5,5,90,6])
# st = {1,2,3,4,5,5,5,90,6}
# print(st)

# st.add(45)
# print(st)

# mySet = {10, 20, 30, 4, 50, 70, 'a'}
# mySet.remove(10)
# print(mySet)
# mySet.discard(10)
# print(mySet)
# mySet.update([12,23,34,4,67])
# print(mySet)

#   que 1
for outer in range(0,4):
    for inner in range(0,4):
        if (outer == 0 or outer == 3):
            print("*",end=" ")
        elif (inner == 0 or inner == 3):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

