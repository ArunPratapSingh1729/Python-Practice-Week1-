dic = {
    "aame": "arnu",
    "class":5,
    "rollnow":13
}
a = list(map(lambda x : dic[x]  ,(filter( lambda x: x.startswith('a') , dic.keys() )) ))

print(a)

a=  list(filter(lambda x : str(x).isdigit() and int(x) > 10  , dic.values()))
print(a)

a = list(filter(lambda x : str(x).isdigit() and int(x)%2 ==0 , dic.values()))
print(a)


dic = {
    "aame": "arnu",
    "class":5,
    "rollnow":13
}

l = [[1,2],[3,4],[6,5]]
name = "hello world"
vowels = "aeiou"
a = lambda x : max(x.count(i) for i in vowels) 
a = lambda x : sum(x.count(i) for i in vowels) 
print(a(name))
