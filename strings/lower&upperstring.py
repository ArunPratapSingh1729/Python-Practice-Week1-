#there any lower or upper in a string 

userinput = input("Enter the input : ")

for ch in userinput:
    if ch.upper() in userinput:
        print(ch.upper())

for ch in userinput:
    if ch.lower() in userinput:
        print(ch.lower())

print()
        
