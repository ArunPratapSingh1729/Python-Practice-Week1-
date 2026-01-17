# From a string, extract characters that are:
# alphabetic
# lowercase
# NOT a vowel
name = "Arun Pratap Singh 123 "
vowels = "aeiou"

l = [i for i in name if i.isalpha() and i.islower() and i not in vowels]

print(l)

# From a list of words, keep words that:
# start with a vowel
# end with a consonant

name = "Arun"
vowels = "aeiou"

l = [i for i in name if name[0].lower() in vowels and name[-1].lower() not in vowels]

print(l)

#  Given a list of numbers, keep numbers that are:
# divisible by 2 or
# divisible by 3
# But not both

l = [1,2,3,4,5,6,6,7,8,9]

lt = [i for i in l if i%2 == 0 and i%3 != 0  or i%2 !=0 and i%3 == 0]

print(lt)

# From a matrix (list of lists), extract diagonal elements.

l = [
 [1, 2, 3],
 [4, 1, 6],
 [7, 8, 1]
]

a = [l[i+1][i+1] for i in range(-1,len(l)) if i<(len(l)-1) and l[i][i] == l[i+1][i+1]  ]
print(a)

# Create a list of strings:
# "Arun scored 80"

l = [str(i) + "scored" + str(j) for i in names for j in scores]
l = [names[i] + " scored " + str(scores[i]) for i in range(len(names))  ]
print(l)