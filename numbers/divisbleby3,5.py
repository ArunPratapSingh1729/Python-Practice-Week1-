a = input("Enter the number : ")
b = int(a)
c = int(a)
check1 = False
check2 = False

while b != 0:
    lastdigit = b%10
    if(lastdigit == 0 or lastdigit == 5):
        check1 = True     
    b = b//10

sum = 0
while c != 0:
    lastdigit = c%10
    sum+=lastdigit
    if sum%3 == 0:
        check2 = True
    c = c//10

if check1 and check2 :
    print("The number is divisible by both 3 and 5")



