# try:
#     int("abs")
#     print("This is the statement in the try")
# except ValueError as e:
#     print("Issue : ", e)
#     print("This is the statement in the except")
# finally:
#     print("This is the statement in the finally")

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


print((result))

# result =  sorted(l , key = lambda x : x[0]+x[1])
# print(result)



# result = sorted(words, key = lambda x : len(x))
# print(result)


# result = max( words , key = len)
print(result)