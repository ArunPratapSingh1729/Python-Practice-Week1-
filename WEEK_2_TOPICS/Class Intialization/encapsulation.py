class car:

    def __init__(self,name,age):
        self.__name = name
        self.age = age

    def description(self):
        return f"The {self.__name} is the private keyword and their age is {self.age}"


c = car('Arun',12)
print(c._car__name)
print(c.description())
print(c.age)

class main():
    Name = "Arun"
    def __init__(self):
        self.name = "arun"
        self._brand = "Toyota"
    def fun(self):
        print("The name of the car is", self._brand)
        
class Child(main):
    def __init__(self):
        super().__init__()
    def fun(self):
        print("this is the function variable",self._name)
    
m = main()
c  = Child()

print(m.fun())
print(m._brand)
print(c.fun())
