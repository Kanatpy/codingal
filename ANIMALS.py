from abc import ABC , abstractmethod

class animal(ABC):
    @abstractmethod
    def move(self):
        pass
class human(animal):
    def move(self):
    
       print("i can talk")
class dog(animal):
    def move(self):
    
        print("i can be a dog")
class cats(animal):
    def move(self):
        print("i can purr")
class girafes(animal):
    def move(self):
        print("i can have long necks")
class other_humans(animal):
    def move(self):
        print("i can be another human")

r = human()
r.move()

e = dog()
e.move()

c = cats()
c.move()

g = girafes()
g.move()

d = other_humans()
d.move()