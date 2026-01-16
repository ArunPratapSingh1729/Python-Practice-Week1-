#start and end with a vowel

s = input("Enter the string ")
s = s.upper()
v = "aeiou"
v = v.upper()

if s[0] and s[-1] in v:
   print("Yes it starts and end with a vowel") 
