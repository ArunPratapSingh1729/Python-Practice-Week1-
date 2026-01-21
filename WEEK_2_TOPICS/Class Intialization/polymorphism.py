from abc import ABC,abstractmethod

class car(ABC):

    @abstractmethod
    def fun(self):
        pass

class a(car):

    def fun(self):
        print("This is the function inside the class a")


a1 = a()

a1.fun()


