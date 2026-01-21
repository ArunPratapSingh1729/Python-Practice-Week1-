#number of vowels in a string

a  = input("Enter the input ")

vowels = "aeiou"
c = {}

for ch in a:
    if ch in c and ch in vowels :
        c[ch] += 1
    elif ch not in c and ch in vowels:
        c[ch] = 1
    else:
        continue

print(c)

    