class Car:   
    car_type = "Sedan" 

    def __init__(self, name, mileage):
        self.name = name 
        self.mileage = mileage 

    def description(self):                 
        return f"The {self.name} car gives the mileage of {self.mileage}km/l"

    def max_speed(self, speed):
        return f"The {self.name} runs at the maximum speed of {speed}km/hr"

obj2 = Car("Honda City",24.1)
print(obj2.description())
print(obj2.max_speed(150))


class c:
    a ="A class"
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def fun(self):
        print("We called the fucntion fun ")
        print(f'the name of the person is {self.name} and their age is {self.age}')
    
    def fun1(self, name):
        print("the name is passed into the fun1 ",name)

a = c('arun',12)
b = c('pratap',14)

print(a.name)
print(a.age)
a.fun()
a.fun1('pop')
print(a.name)



