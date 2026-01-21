#class variable -> assigned inside the class and shared among all the instances of that class
#instance variable -> assigned to each instance separately 

#python first check for the variable inside the instacne and 
#than inside the class if an object have the same name for the vairable as like the 
#class variable than they will overrite the class variable with the instance variable 

class student():
    school_name = 'ABC_'
    def __init__ (self,name=None):
        self.name = name
        student.school_name = 'Pop' #updating inside the __init__ method 


s1 = student('arun')
s2 = student('pratap')

print(s1.name)  
print(s1.school_name)
print(s2.name)
print(s2.school_name)
# student.school_name = 'XYZ_' #updating the class variable 
print(s1.school_name)
print(s2.school_name)

