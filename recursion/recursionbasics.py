#ascending order 

def fun(N):
    if N <= 0:
        return 
    fun(N-1) 
    print(N)

fun(5)

#descending order

def fun(N):
    if N <= 0 :
        return 
    print(N)
    fun(N-1)

#sum of a number till N
def fun(N):
   if N <= 0 :
       return 0 
    return N  + fun(N-1)

print(fun(10))

#sum of all the digits 
def fun(D):
    s = 0
    while D != 0:
        ld = D %10
        s += ld
        D = D//10
    return s
    
a = fun(51)
print(a)

#print character till given character
def fun(C):
    if C < 'A':
        return
    fun(chr(ord(C) - 1))
    print(C)
    
fun('E')
    
#prodcut of digits
def fun(N):
    s = 0
    if N <= 0:
        return 1
    return N * fun(N-1)
    
print(fun(5))

#even number only or odd one 
def fun(N):
   if N <= 0 :
       return 0 
    fun(N-1)
    print(N) if N%2 == 0 else None

print(fun(10))