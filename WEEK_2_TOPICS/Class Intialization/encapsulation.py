class car:

    def __init__(self,name,age):
        self.__name = name
        self.age = age

    def description(self):
        return f"The {self.__name} is the protected keyword and their age is {self.age}"


c = car('Arun',12)
print(c._car__name)
print(c.description())
print(c.age)
