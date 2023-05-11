class driver:
    def __init__(self,name,email):
        self.name = name
        self.email = email
    def info(self):
        print("detaile is ",self.name,self.email)


class Customer(driver):
    def __init__(self,name,email,wallet):
        super().__init__(name,email)
        self.wallet = wallet
    def cinfo(self):
        super().info()
        print("details are  ",self.name,self.email,self.wallet)

c1 = Customer("name","abs",191)
c1.cinfo()


# class CounterValue:
#     count  = 0
#     def __init__(self,x):
#         self.x = x
        # self.count+=1
        # CounterValue.count+=1
# c1 = CounterValue()
# c1 = CounterValue(12)
# print(c1.count)
# c2 = CounterValue(20)

# print(c2.count)


# class datascience:
#     def deinfo(self):
#         print("ds")


# class dataengineer(datascience):
#     def deinfo(self):
#         # super().dsinfo(self)
#         print("de")

# class regex(dataengineer):
#     def deinfo(self):
#         super().deinfo()
#         print("regex")

# r = regex()
# r.deinfo()


# class bluewhale:
#     def henfo(self):
#         print("whale")

# class human:
#     def henfo(self):
#         print("human")


# class mammal(human,bluewhale):
#     def minfo(self):
#         super().henfo()
#         # super().info()
#         print("mammal")


# m = mammal()
# m.minfo()