from dataclasses import dataclass:

@dataclasses
class A():
    name :str
    id:int

a = A()
a.name ="arun"

print(a.name)