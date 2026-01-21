import math

a = input("Enter the number ")
a = int(a)
sqrt = int(math.sqrt(a))

if ((sqrt * sqrt) == a):
    print("The number is a perfect square")
else:
    print("The number is not a perfect square")
