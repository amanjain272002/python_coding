from abc import ABC,abstractmethod
class dog(ABC):

    @abstractmethod 
    def info(self):
        pass

class fish(dog):
    # def info(self):
    #     print("0 legs")

    def newfun(self):
        print("hello")


f1 = fish()
f1.info()
f1.newfun()