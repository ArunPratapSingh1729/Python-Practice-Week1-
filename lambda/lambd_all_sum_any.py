x = lambda x: any(i.isalpha() for i in x)
print(x("arun"))


#there is no requirement for if with any 
#after the loop you can use if you are using the sum

a = input("Enter the digits : ")

x = lambda x : sum(int(i) for i in x)
x = lambda x : sum(int(i) for i in x if int(i)%2 == 0)
u = lambda x : sum(int(i) for i in x if int(i)%2 != 0) 


# Check if a number contains at least one zero
print((lambda x: any(int(i) == 0 for i in x))("13"))

# Check if a string contains at least one uppercase letter
print((lambda x:any(i.isupper() for i in x))("Arun"))

# Check if a string contains both digit and alphabet
print(((lambda x:any(int(i).isdigit() for i in x)) and (lambda x:any
    (i).isalpha() for i in x) ))("1$"))

# Check if a list contains at least one negative even number
l = [1,-2,3,4]
a = lambda x : any(((int(i) > 0) %2) ==0 for i in x)
print(a(l))

# Check if a number contains any repeated digit
a = lambda x : any(x.count(i) > 1 for i in x)
print(a(str(112)))

# Check if all digits of a number are even
a = lambda x : all(int(i)%2 == 0  for i in x)
print(a('22'))

# Check if a number is prime number or not
num = 10

a= lambda x : all(int(x)%int(j) != 0 for j in range(2,int(x)))

print(a(str(num)))


# Check if all digits of a number are even
x = lambda x : "Even" if (sum(int(x) for i in str(x)))%2 == 0 else "Odd"
print(x(1234))

# Check if all characters in a string are lowercase letters
x  = lambda x: all(i.islower() for i in x)
print(x("arun1"))

# Check if all numbers in a list are divisible by 5
x = lambda x : all(int(i)%5 == 0 for i in x )
x = lambda x :  True if (int(x)%10 == 0  or int(x)%10 == 5 ) else False
print(x(125))

# Check if all words in a list start with a vowel
l = ["arn", "eop", "pop","loi"]
vowels = "aeiou"
x = lambda x : all(i[0] in vowels for i in x)
print(x(l))

# Check if all digits of a number are unique
number = 1234
x = lambda x : len(set(x)) == len(x)
print(x(str(number)))

# Check if a number contains only even digits
x = lambda x : all(int(i)%2 == 0 for i in x)
print(x("246"))

#Check if a string has at least one vowel and no digits
vowel = "aeiou"
x = lambda x : any(i in vowel for i in x ) and not any(i.isdigit() for i in x)

print(x('arun'))

# Check if sum of digits is greater than number of digits
digit = 123
x  = lambda x : True if sum(int(i) for i in x) > len(x) else False
print(x(str(digit)))


# Check if a password:
# has at least one uppercase
# has at least one digit
# has no spaces

x  = lambda x : all(any(i.isupper() for i in x) and any(i.isdigit() for i in x) 
and not any (i.isspace() for i in x)

print(x("aruMN12"))

# Find number whose square is maximum
l = [1,2,3,4,5]
a = lambda x : max(i**2 for i in x )
print(a(l))

# Find string with maximum vowels
sen = ["this", "arub", "hello"]
vowels = "aeiou"
a = lambda x : max(j.count(i) in in vowels for j in x)
print(a(sen))


