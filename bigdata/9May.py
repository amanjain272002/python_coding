# f = open('data.txt', 'r')
# print(f.tell())
# print(f.read())
# print(f.seek(3))

# print(f.read())
# f.close()
# with open("data1.txt","r") as f:
    # f.write("hello")
    # f.write("kaise ho")
    
    # print(f.tell())
    # x = f.readlines()
    # print(x)
    # print(x)
    # y = f.readline()
    # print(y)

# with open("data1.txt","w") as f:
f = open("bye.txt","w")
f.write("hello\n")
f.write('bye')

f = open("bye.txt","r")
print(f.read())



# try:
#     print("hello")
#     x=10
#     print(x/y)
# except:
#     print("whatever")