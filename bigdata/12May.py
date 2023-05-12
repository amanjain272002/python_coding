# class student:
    # protected
    # _x = 10 
    
    # private
#     __fee = 9989


# class StudentHobby(student):
#     y = 10


# sh1 = StudentHobby()
# print(sh1._x)
# print(sh1.__fee
# print(dir(sh1))
# print(sh1._student__fee)


class addnumber:
    def __init__(self,x,y):
        self.x = x 
        self.y = y
    
    def __repr__(self) :
        return f"Data is {self.x} and {self.y}"
    
    
    def __add__(self,arg) :
        # return f"Data is {self.x} and {self.y}"
        num1 = self.x + arg.x
        num2 = self.y + arg.y
        return addnumber(num1,num2)
a1 = addnumber(10,20)
# print(a1)
a2 = addnumber(30,40)
# print(a2)


# a1 + a2 => a1.__add__(a2) 
# self = a1 and arg = a2
print(a1+a2)