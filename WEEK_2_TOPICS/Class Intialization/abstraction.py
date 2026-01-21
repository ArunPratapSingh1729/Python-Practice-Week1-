from abc import ABC, abstractmethod

class car(ABC):
    def __init__ (self):
        print("This is the abstract class ")
    
    @abstractmethod
    def price(self,x):
        pass


class new(car):
    def price(self,x):
        print(f"The {self.name}'s price is {x} lakhs.")

obj = new('Hero honda')
