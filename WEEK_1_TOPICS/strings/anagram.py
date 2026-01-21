text = "listen"
text1 = "silentt"

ch = {}
ch1 = {}
for i in text:
    if i in ch:
        ch[i] +=1
    else:
        ch[i] = 1
        
for i in text1 :
    if i in ch1:
        ch1[i] += 1
    else:
        ch1[i] = 1

for i in ch.keys():
    if i in ch1.keys():
        if ch1.get(i) != ch.get(i):
            print('Not a anagram')
            break
    else:
        print("not a anagram")
        
       