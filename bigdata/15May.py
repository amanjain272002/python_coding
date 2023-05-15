# class student:
#     age  =10
#     @staticmethod
#     def info(x,y):
#         print(x+y)


# print(student.info(10,20))

# class student:
#     age  =10
#     @classmethod
#     def info(cls):
#         print("he ",cls.__name__)
    
# student.info()

class dollar:
    def __init__(self,amount):
        self.amount = amount

    def __repr__(self) :
        return f"dollar amount is ${self.amount}"

    def amountConvert(self,num1,num2):
        # return "hey"

        # calling constructor and repr again
        return dollar(num1+num2)
    
    @staticmethod
    def amountConvert1(num1,num2):
        return dollar(num1+num2)
    
    
    @classmethod
    def amountConvert2(cls,num1,num2):
        return cls(num1+num2)
    
# d1 = dollar(10)
# print(d1)
# print(d1.amountConvert(10,20))
# print(dollar.amountConvert1(23,89))


class euro(dollar):
    def __init__(self,amount):
        super().__init__(amount)
        self.symbol = "yen"

    def __repr__(self):
        return f"amount is {self.symbol} {self.amount}"


e1 = euro(99)
# print(e1)
# print(euro.amountConvert1(33,44))
print(euro.amountConvert2(33,44))