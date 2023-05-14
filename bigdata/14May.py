# class addnumber:
#     def __init__(self,x,y):
#         self.x = x 
#         self.y = y
    
#     def __repr__(self) :
#         return f"Data is {self.x} and {self.y}"
    
    
#     def __add__(self,arg) :
#         num  = addnumber(0,0)
#         num.x = self.x + arg.x
#         num.y = self.y + arg.y
#         print(num.__repr__())

# a1 = addnumber(10,20)
# a2 = addnumber(30,40)
# a1 + a2


class greaterThan:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    
    def __repr__(self) :
        return f"Data is {self.x} and {self.y}"

    def __gt__(self,arg):
        if(pow(self.x,2)+pow(self.y,2)>pow(arg.x,2)+pow(arg.y,2)):
            return False
        else:
            return True
            
o1 = greaterThan(3,2)
o2 = greaterThan(3,4)
# print(o1)
print(o1>o2)
# print(dir(greaterThan))