a = list(sorted(lambda x: x , key = dic.values()))
print(a)

s  = {i[1] for i in dic.items() if str(i[1]).isdigit() }
s = sorted(s)
print(s)

# Sort by last character
words = ["dog", "apple", "cat"]
l = sorted(words , key = lambda x : x[1],reverse = True)
num = [1,2,3,4]
l = sorted(num , key = lambda x : -x)
d = {"a": 3, "b": 1, "c": 2}
l = sorted(d, key = lambda x: d[x])
l = sorted(d.items() ,key = lambda x : x[1])



print(l)






