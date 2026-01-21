class a:
    def fun(self,marks):
        self.mark  = marks
        print('this is the self ',self.mark)
        
class b:
    def fun(self,marks):
        self.m = marks
        print('this is the self ',self.m)
        
        
def run(a,o):
    a.fun(o)
    
A = a()
B = b()
run(B,90)
run(A,45)