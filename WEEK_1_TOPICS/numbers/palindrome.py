b = int(input("Enter the number : "))
a = b

newnumber = 0

while a != 0:
    digit = a % 10
    newnumber = newnumber * 10 + digit
    a = a // 10

if newnumber == b:
    print("The number is a palindrome")
else:
    print("The number is not a palindrome")



 