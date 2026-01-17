s  = "this is a string"
substring = 'this'

a = s.startswith(substring)
if a:
    print("this is a substring starting")
else:
    print("this is not a substring starting")

b = s.endswith(substing)
if b :
    print("this is a substring ending")
else:
    print("this is a not a substring ending")