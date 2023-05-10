lst  = []
class hobies:
    # def hobbie(self):
        
    def __init__(self,sname ,email,hobie_name):
        self.hobie = []
        self.sname = sname
        self.email = email
        self.hobie.append(hobie_name)
    
    def appen(self,hob):
        self.hobie.append(hob)
            
    def pr(self):
        print(self.hobie)


s1 = hobies("a","abs@gmail.com","play")
s1.appen("y")
s1 = hobies("a","abs@gmail.com","tea")
s2 = hobies("a","abs@gmail.com","play1")
s1.pr()