# From a list of numbers, create
# {num : True/False} depending on whether the number is prime

dic = { i: 'True' if i ==  1 or not any(i%j==0 for j in range(2,int(i * 0.5)+1) )  else 'False' for i in l }

words = ["ari", "okp", "pop", "pop"]
l = [1,2,3,4,5,6,6,6,6,10]
w= ["apple", "banana", "cherry"]
students = {"ar" :13 , "b": 45, "c":98, "d": 90}

d = {k:k.upper() for k in w}

d  = {k: "many" if words.count(k) > 1 else "one" for k in set(words)}

d = {k : words.count() for k in words} 

print(d)
d =  {k:k*k for k in l if k%2 == 0}

print(d)

