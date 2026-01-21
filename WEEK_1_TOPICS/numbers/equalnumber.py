digit = (input("Enter the digits : "))
n = len(digit)

sum1 = 0
sum2 = 0
for i in digit[n//2:]:
    sum1 += int(i)

for j in digit[:n//2]:
    sum2 += int(j)

if sum1 == sum2 :
    print("both of the sum are equal")
else:
    print("no the sum are not equal")