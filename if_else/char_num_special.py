a = input("Enter the character : ")

if ('a' <= a <= 'z') or ('A' <= a <= 'Z'):
    print("It is a character")
elif '0' <= a <= '9':
    print("It is a number")
else:   
    print("It is a special character")