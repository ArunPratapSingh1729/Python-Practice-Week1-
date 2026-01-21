userinput = input("Enter the input : ")

for i in userinput:
    if i.islower():
        print("there is a lowercase")
    if i.isupper():
        print("there is a uppercase")