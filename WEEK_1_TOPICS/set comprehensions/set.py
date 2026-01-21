#list to set

l = [1,2,3,4]

s = {i for i in l}
print(s)

#From a string, create a set of unique characters.

s = "arunrnpratap"

s= {i for i in s}
print(s)

#list to set of even number 

l = [1,2,3,4,5,6,7,8,9,10]

s = {i for i in l if i % 2 ==0}
print(s)

#extract vowel out from a string

st = "arun pratap singh"
vowels = "aeiou"
s = {i for i in st if i in vowels}
print(s)


# From a string, create a set of characters excluding digits and special characters.

s = "arun pratap singh is coding now"
w = s.split()
st = {i for i in w if not i.isdigit() and i.isalpha()}

print(st)

# From a list of numbers, create a set that contains:

# square if number is even

# cube if number is odd

# what if only for even numbers 

l = [1,2,3,4,5]

s = {i*i if i%2 == 0 else i**3 for i in l if i%2 == 0}

print(s)

# From a sentence, create a set of words that:

# start with a vowel

# length > 3

sentence = "this issss how the python is working from the scratch"
words = sentence.split()
vowels= "aaeiou"
tuplevowels = tuple(i for i in vowels)

s = {i for i in words if i.startswith(tuplevowels) and len(i) > 3}
 
print(s)

# From two lists, create a set of common elements.

l1 = [1,2,3,4]
l2 = [5,2,3,8]

s = set(l1).intersection(set(l2))

print(s)
