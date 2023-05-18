# def test(a,b):
#     return(a+b)



# def newvalue(z,func):
#     print(z)
#     # print("Func value is ",func)
#     return(func(10,20))

# # newvalue(10,test(12,13))
# print(newvalue(10,test))


# def arith():
#     print("arithmet")
#     def subtract():
#         print("hello")
#     return subtract

# x = arith()
# x()

# def arith(func):
#     print("arithmet ",func)
#     def subtract():
#         print("hello")
#         func()
#     return subtract

# def add():
#     print("add function ")

# x = arith(add)
# x()



def arith(func):
    print("arithmet ",func)
    def subtract():
        print("hello")
        func(10,20)
    return subtract


# decorated function 
@arith
def add(x,y):
    print("add function ",x + y)
    
add()

