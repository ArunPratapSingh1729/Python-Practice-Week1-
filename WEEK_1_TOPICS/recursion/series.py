
#fibonacci series

def fun(n):
    if n <= 0:
        return 0
    if n == 1:
        return 1
    return fun(n-1) + fun(n-2)
    
for i in range(6+1):
    print(fun(i) ,end =" ")
    
fun(5)

# airthmetic progression

count = 0
def fun(a,d,n):
    global count
    count +=1
    if a > n:
        return 0
    if a == n:
        count 
    return fun(a+d,d,n)

a=2
d=3
n=15

print(fun(a,d,n))

#geometric progression

count = 0 

def fun(a,d,n):
    global count 
    count += 1
    if count == n:
        return a
    
    return fun(a*d,d,n)
    

a = 2
d = 2
n = 5
print(fun(a,d,n))
    

count = 0 

def fun(a,d,n):
    global count 
    count += 1
    if a == n:
        return count
    if a > n :
        return -1
        
    return fun(a*d,d,n)
    

a = 2
d = 2
n = 5
print(fun(a,d,n))
    
#sum of the elements of an array
def fun(arr,index,summ):
    if index == -1:
      return summ
    summ += arr[index]
    return fun(arr,index-1,summ)


arr = [1,2,3,4,5]
print(fun(arr,len(arr)-1,0))   

#max in an array
def fun(arr,index,maxx):
    if index == -1:
      return maxx
    if maxx < arr[index]:
        maxx = index
    return fun(arr,index-1,maxx)


arr = [1,2,30,4,5]
print(arr[fun(arr,len(arr)-1,arr[0])])    