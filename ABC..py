from abc import ABC, abstractmethod
class abcclass(ABC):
    def print(self,x):
        print(x)
    @abstractmethod
    def abstract(self):
        print("you shall not see me")
class random_class(abcclass):
    def abstract(self):
        print("you shall see me")

tobj = random_class()
tobj.abstract()
tobj.print(8383883838)