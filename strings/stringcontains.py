# Check if first character is a vowel

# Check if last character is a digit

# Check if string starts with a capital letter

# Check if string ends with a special character

# Check if string contains only alphabets

# Check if string contains only digits

# Check if string contains both letters and digits

userinput = input("Enter the input : ")

vowels = "aeiou"
specialchar = "!@#$%^&*()"

if userinput[0] in vowels:
    print("Yes it is a vowel for the first")

if userinput[-1].isdigit():
    print("Yes it is a number ")

if userinput[0].isupper():
    print("Yes it is a upper character")
    print(userinput.upper())

if userinput.isalpha():
    print("Yes it si the alpha ")

if userinput.isdigit():
    print("Yes it is the number")

def has_letter_and_digit(s):
    has_letter = False
    has_digit = False

    for ch in s:
        if ch.isalpha():
            has_letter = True
        elif ch.isdigit():
            has_digit = True

    if has_letter and has_digit:
        print("String contains both letters and digits")
    else:
        print("String does NOT contain both letters and digits")


for ch in userinput[-1]:
    if ch in specialchar:
        print("Yes it is ")



