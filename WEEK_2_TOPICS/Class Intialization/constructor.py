#python doesnt not support constructor overloading 
#default parameters 

class Employee():
    def __init__ (self,name = None,age = None):
        self.name = name
        self.age = age

e1 = Employee('arun',12)
e1 = Employee('arun')
e2 = Employee()

print(e1.name)
print(e1.age)
print(e2.name)
print(e2.age)


#using *args 

class Employee():
    def __init__ (self,*args):
        self.name = name
        self.age = age

e1 = Employee('arun',12)
e1 = Employee('arun')
e2 = Employee()

print(e1.name)
print(e1.age)
print(e2.name)
print(e2.age)



#new is used to updating the mutable project
class PositiveInt(int):
    def __new__(cls, value):
        if value < 0:
            raise ValueError("Only positive integers allowed")
        return super().__new__(cls, value)

x = PositiveInt(10)
print(x)      # 10

y = PositiveInt(-5)  # ValueError

