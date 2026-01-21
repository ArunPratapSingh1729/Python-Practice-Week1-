class Employee(): #class Employee:
    pass

e1 = Employee()
e2 = Employee()

print(e1)
print(e2) #different location for both of the employee objects

e1.name= "arun"
e1.age = 12

e2.name = "pratap"
e2.age = 14

print(e1.name)
print(e2.age)

# this method is very lengthy and not efficient 
# now we will use the dhunder method which we can 

# __init__

class Employee():
    def __init__ (self, name):
        self.name = name

e = Employee('arun')
# e.name = "arun pratap singh"

print(e.name)

class E():
    def __init (self):
       self.name = name

e = E()
e('arun')
print(e)


# 
class c :
    def __init__ (self,name,age):
        self.name = name
        self.age = age
        self.email = self.name , "." , self.age , "@company.com"
    def fun(self):
        return '{} {}'.format(self.name,self.email)

c1 = c('arun',21)
print(c1.name)
print(c1.age)
print(c1.email)
print(c1.fun())


