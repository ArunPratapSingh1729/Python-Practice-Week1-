# Convert each number to "Even" or "Odd"
l = [1,2,3,4]
x  = list(map(lambda x : "Even" if x%2 == 0 else "Odd" , l))

print(x)

#Convert each number into a string
l = [1,2,3,4]
x  = list(map(lambda x : str(x) , l))

print(x)

# Convert each string to its length

l = ["apple", "banana", "kiwi"]
x  = list(map(lambda x : len(x) , l))

print(x)

# Replace numbers less than 5 with 0, else keep number

l = [1,2,3,6,7,8,9]
x  = list(map(lambda x: 0 if x<5 else x ,l))

print(x)

# Convert each character to "Vowel" or "Consonant"

a = "arun"
vowels = "aeiou"
x = list(map(lambda x : "Even" if x in vowels else "consonants" if x.isalpha() else "special character" , a))

print(x)

# Convert each character to uppercase

x = list(map(lambda x : x.upper() , "arun"))
print((x))

# Convert list of numbers to strings

# Find length of each word


l = [1,2,3,4,5]
a  = list(map(lambda x : str(x) , l))
print(a)

l = "this is to me "
l = l.split()
a=  list(map(lambda x : len(x), l))
print(a)

# From list of words, return word length if length > 3 else 0s = "This is for me the world"
s = s.split()
a = list(map(lambda x : x if len(x) > 3 else 0 , s))

print(a)