import json

data = {
    "name": "Arun",
    "age": 25,
    "skills": ["Python", "Git"]
}

#python -> json (string) json.loads
#python <- json (dict) json.dumps

#write
with open('file.json', 'w') as f:
     print(type(json.dump(data,f,indent =4)))

#read
with open('file.json') as f:
    a = json.load(f)

print(a)
print(type(a))
