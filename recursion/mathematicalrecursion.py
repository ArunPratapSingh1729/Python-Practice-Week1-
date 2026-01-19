#factorial of a number

def fun(N):
    if N <= 1:
        return 1
    return N * fun(N-1)

print(fun(5))

#power of x^n

def fun(base, exponent):
    if exponent == 1:
        return base
    elif exponent == 0 :
        return 1
  
    return base * fun(base,exponent - 1)

print(fun(3,0))

#gcd using the recursion


def fun(a , b):
    if b == 0 :
        return a 
    return fun(b, a%b)

print(fun(3,9))

#lcm using recursion

def fun(a,b):
    if b == 0:
        return a
    return fun(b, a%b)
    
a = 3
b = 9

gcd = fun(a,b)

lcm = (a*b)//gcd    

print(lcm)
