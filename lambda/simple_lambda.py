# Lambda handles ONE element

# Loop / iteration is done by map, filter, sorted, min, max

#sq of a number 

print((lambda x : x**2)(5))

#cube of a number 

print((lambda x : X**3)(3))

#add 10 to a number 

print((lambda x : x  + 10))

# no is positve
print((lambda x:x>0)(9))

#if no is greater

print((lambda x: x > 10)(9))

#area of rectangle 

print((lambda x , y: x*y) (2,3))

#mulitple if else 
print((lambda x: 'A' if x>=90 else 'B' if x >=75 else 'C' )(90))
print((lambda x : 'A leap year' if x %400 == 0 else x if x %100 !=0 and x%4 ==0 else 'Not a leap year')(2024))
print((lambda x : 'Positive' if x > 0  else 'Negative' if x < 0 else '0')(2024))

#lambda with strings
print((lambda x: len(x))("arun"))

#sum of digits 
print((lambda n: sum(int(d) for d in str(n)))(123))

#printing strings
print((lambda firstname ,lastname : f'Full name: {firstname.title()} {lastname.title()}')("arun","pratap"))

#findingvowels 
a = "arun pratap singh"
vowels = "aeiou"

x = lambda x : "vowels" if x in vowels else "space" if x.isspace() else "consonants"
for i in a:
    print(i , x(i))

#remove space and calculate the lenght 
a = "arun pratap singh"
vowels = "aeiou"

x =( lambda x :"Valid" if len(x.strip())%2 == 0 else "Invalid")
print(x(a))

#-8
print((lambda x : x if x > 10 else -x)(8)   )
#9
print((lambda x,y: x if x> y  else y)(8,9))
#True
print((lambda x,y: x == y)(8,8))
#False
print((lambda x,y: x == y)(9,8))


# Lambda to return max of two numbers

# Lambda to return absolute value

# Lambda to convert string to lowercase

a = lambda x,y : max(x,y)
print(a(9,4))

a = lambda x : -x if x<0 else x
print(a(-4))

a = lambda x : x.lower() if x.isalpha() else "Invalid input"
print(a("ARUN"))

# Lambda to return second character of string
# Lambda to return last digit of number
# Lambda to return string without first character

a = lambda x: x[1] 
print(a("arun")) 
a = lambda x: x%10
print(a(123))
a = lambda x : x[len(x):0 :-1]
print(a("arun"))

