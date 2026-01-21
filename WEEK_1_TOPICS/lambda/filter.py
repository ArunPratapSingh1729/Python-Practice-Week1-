# # Keep only even numbers
x  = list(filter(lambda x : int(x)%2 == 0, l))
print(x)

# Keep only numbers greater than 5
x  = list(filter(lambda x : int(x) > 5, l))
print(x)

# Keep only negative numbers
l = [1,2,3,4,5,45]
x = list(filter(lambda x : int(x) > 0, l))

print(x)

# Keep only vowels
vowels = "aeiou"
a  = list(filter(lambda x : x in vowels, "education"))
print(a)

# Remove all spaces
s = "I am learning Python"
a = list(filter(lambda x : not x.isspace(), s))
print(a)

# Keep only uppercase letters
s = "ApPlE"

l = list(filter(lambda x: x.isupper() , s))
print(l)

# Keep words with length > 4
l = ["apple", "kiwi", "banana", "fig"]

a = list(filter(lambda x : len(x) > 5, l))
print(a)    

# Keep characters that are not special characters
a = "a@b#c$1"

b = list(filter(lambda x : not x.isalpha() and not x.isdigit() , a))

print(b)