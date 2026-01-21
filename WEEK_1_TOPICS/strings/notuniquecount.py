s = "string is here"

for i in s:
    if s.count(i) > 1:
        print(i,"is not a unique number")
        break
    
c = {}

for ch in s:
    if ch in c:
        c[ch] += 1
    else:
        c[ch] = 1
        
for i in c:
    if c[i] >= 2 :
        print("These are not unique ", i)
    
print("The values of c are ", c)