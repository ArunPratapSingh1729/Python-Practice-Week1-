class student:
    def __init__(self ,name):
        self.name = name
        
    def marks(self,m):
        self.m = m
        print(f"The marks of the student is {self.m}")
        
class school:
    def __init__(self,name):
        self.name = name
        
    def student_info(self,b):
        s.marks(b.m)
        print("The info about the student is given below: ")
        
s = student('Arun')
s.marks(45)

sc = school('ABC')
sc.student_info(s)