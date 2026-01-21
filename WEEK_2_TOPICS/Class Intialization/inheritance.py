class parent:
    b = "this is the class variable"
    def __init__(this,name,age):
        this.name = name
        this.age = age
        print("The name of the uesr is ", name)
        print("the age of the user is ", age)

class child(parent):
    def fun(self):
        super().__init__('pratap',22)
        print("this is the function in the child class")

class child1(child):
    def fun(self):
        print("this si the fucntion in the child 1 class")

# p = parent()
c = child('arun',12)
# b  = child1('arun',13)

b.fun()
c.fun()


#Using the super 


class parent:
    b = "this is the class variable"
    def __init__(this,name,age):
        this.name = name
        this.age = age
        print("The name of the uesr is ", name)
        print("the age of the user is ", age)

class child(parent):
    def fun(self):
        super().__init__("aurn",56)
        print("this is the function in the child class")

class child1(child):
    def __init__(self):
        print("this is the constructor of the child1")
    def fun(self):
        super().fun()
        print("this si the fucntion in the child 1 class")

# p = parent()
c = child('ar',12)
b  = child1()

b.fun()
c.fun()


class A:
    def __new__(cls):
        print("New")
        return super().__new__(cls)

    def __init__(self):
        print("Init")

class B(A):
    def __init__(self):
        # Correct way to call the parent's constructor
        super().__init__() 
        print("constructor B")

a = A()
b = B()
