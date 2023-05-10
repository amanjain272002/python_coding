class student:
    
    # def __init__(self,id):
    #     #  make here so that only that particuar object can acces if formed above class can also access
    #     self.sid = id
    #     print("hey")
    
    def __init__(x,id):
        x.sid = id
        
    # def __init__(self):
    #     print("hello")


#  constructor envoke when object is formed
s1 = student(10) 
print(s1.sid)
# print(s1)