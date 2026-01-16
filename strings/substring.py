substring = "appl"
string = "apple"

if substring in string :
    print("yes it is subtring")


f = True
for i in string :
    if f == False:
        break
    for j in set(substring):
        if i == j and string.count(i) != substring.count(j):
            print("Not a subtring ")
            f = False
            break
if f :
    print("It's a substring")
            
    
