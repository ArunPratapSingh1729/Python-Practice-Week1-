digit = 123 
a = int(digit)
count = 0

while a != 0:
    count +=1

    a = a//10

if count == 2:
    print("the number is a two digit number")
elif count == 3:
    print("the number is a three ..")
elif count > 3:
    print("the number is greater than 3")
else:
    print("the number is less than 2 ")
