d1 = {"a": 1}
d2 = {"b": 2}

d3 = {**d1, **d2}
print(d3)

d1 = {"a":1,"b":"arun","c":3}
a = d1  
print(*a)
print(*a.keys())    
print(*a.items())
print(*a.values())


def fun(**d):
    print(*d.values())
    print(*d.keys())

    
fun(**d1)

*a = {a:1, b:2,c:3,d:4}

print(a)





