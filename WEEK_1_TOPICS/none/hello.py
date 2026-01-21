#None
# None means no value

# Use is None, not == None

# Every function returns something → default None

# print() always returns None

# None ≠ 0, False, ""

def fun():
    print("helo world")

x = fun()
print(x)

x = None
print(type(x))

if print(0):
    print('yes')
else:
    print("No")
    
print({})
print(None is None)
print(None is False)
print(None == 0)

def f():
    return

print(f())

def func(x=None):
    if x is None:
        print("No value passed")

func()

None + 1        ❌
len(None)       ❌
None > 5        ❌

