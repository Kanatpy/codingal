from abc import ABC , abstractmethod

class car(ABC):
    @abstractmethod
    def vroom_vroom(self):
        pass
class bmw(car):
    def vroom_vroom(self):
        print("i am bmw")
class frarri(car):
    def vroom_vroom(self):
        print("i am frarri")
class motor(car):
    def vroom_vroom(self):
        print("why is my parent a car because im jus' a motor")