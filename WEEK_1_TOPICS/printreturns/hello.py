#print returns None

def function(n):
    print("The value of the n is ", n)

# def function(n):
#     return n+1


def check(x):
    # print(x > 5)
    return x > 5

print(type(print()))
print(print(5))
print(function(5))
print(print(function(5)))

x = print(1,2,3)
print(x)


if check(10):
    print("Yes")
else:
    print("No")
