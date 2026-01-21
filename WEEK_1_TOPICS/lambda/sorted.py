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


l = [(1,2), (2,3), (4,5), (0,0)]
words = ["cat", "elephant", "dog", "tiger"]

words = ["sky", "apple", "education"]
vowels = "aeiou"

result = sorted(words , key=lambda x: sum(1 for i in x if i in vowels)) 
result = sorted(words , key = lambda x : sum(1 for ch in x if ch in vowels))


words = ["Banana", "apple", "cherry"]
result = sorted(words, key = lambda x :x.lower())

nums = [5, 2, 8, 1, 3]
result = sorted(nums, key = lambda x: not x%2)

nums = [5,2,8,1,3]
result = sorted(filter(lambda x : x%2 == 0, nums))

result = sorted(map(lambda x: x**2 , nums))

d = {"apple": 1, "hi": 2, "banana": 3}

result = sorted(d,key = lambda x : len(x))
result = sorted(map(lambda x : (x,d.get(x)) ,d),reverse = True)
result = sorted(d.items() , key = lambda x: len(x[0]) )



# d = {'a':3, 'b':2, 'c':4}
# result = (sorted(d.items(), key = lambda x: x[1] ))


# result =  sorted(l , key = lambda x : x[0]+x[1])
# print(result)



# result = sorted(words, key = lambda x : len(x))
# print(result)


# result = max( words , key = len)
print(result)




