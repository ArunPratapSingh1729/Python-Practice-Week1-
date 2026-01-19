**FOR THE LEARNING PURPOSE ONLY**



LEVEL 1: BASICS
Q1
a, b = (10, 20)
print(a, b)

Output

10 20


Reason: First element → a, second → b

Q2
x, y = 5, 7
print(x + y)


Output

12


Reason: 5, 7 is implicitly a tuple

Q3
a, b = [1, 2]
print(a, b)


Output

1 2


Reason: Any iterable supports unpacking

Q4
a, b = "hi"
print(a, b)


Output

h i


Reason: String is iterable (characters)

Q5
a, b = (100,)


❌ Error

ValueError: not enough values to unpack


Reason: Only 1 value, 2 variables

Q6
a, = (100,)
print(a)


Output

100


Reason: Trailing comma tells Python “one value”

LEVEL 2: COUNT MISMATCH
Q7
a, b = (1, 2, 3)


❌ Error

ValueError: too many values to unpack

Q8
a, b, c = (1, 2)


❌ Error

ValueError: not enough values to unpack

Q9
a, b = []


❌ Error

ValueError: not enough values to unpack


Reason: Empty iterable

Q10
a, b = (None, None)
print(a is b)


Output

True


Reason: None is a singleton

🟡 LEVEL 3: NESTED UNPACKING
Q11
a, (b, c) = (1, (2, 3))
print(a, b, c)


Output

1 2 3

Q12
(a, b), c = ((1, 2), 3)
print(a, b, c)


Output

1 2 3

Q13
(a, (b, c)) = (1, (2, 3))


✅ Valid
Parentheses are for grouping, not required logically

Q14
a, (b, c) = (1, (2, 3, 4))


❌ Error

ValueError: too many values to unpack

Q15
(a, b), (c, d) = (1, 2), (3, 4)
print(a, b, c, d)


Output

1 2 3 4

🟡 LEVEL 4: STAR UNPACKING
Q16
a, *b = (1, 2, 3, 4)
print(a, b)


Output

1 [2, 3, 4]

Q17
*a, b = (1, 2, 3, 4)


Output

[1, 2, 3] 4

Q18
a, *b, c = (1, 2, 3, 4, 5)


Output

1 [2, 3, 4] 5

Q19
*a, = (1, 2, 3)


Output

[1, 2, 3]


Reason: Star always produces a list

Q20
a, *b, c = (1, 2)


Output

1 [] 2


Valid: Star can absorb zero values

🟡 LEVEL 5: SWAPPING
Q21
a, b = b, a


How it works

RHS evaluated → tuple

LHS assigned simultaneously

Q22
a, b, c = 1, 2, 3
b, c, a = a, b, c


Output

3 1 2

Q23
x, y = y, x + y


Why valid: RHS evaluated first

🟡 LEVEL 6: FUNCTION RETURNS
Q24
def f(): return 1, 2


Output

1 2

Q25
a, b = (1, 2, 3)


❌ Error

too many values to unpack

Q26
a, *b = f()


Output

1 [2]

Q27
def h(): return [1, 2]


Types

<class 'int'> <class 'int'>

🔵 LEVEL 7: LOOPS
Q28
for a, b in [(1,2),(3,4)]:


Output

3
7

Q29
[(1,2),(3,4,5)]


❌ Error during second iteration

Q30
for a,(b,c) in data:


Output

1 2 3
4 5 6

🔵 LEVEL 8: DICTIONARY
Q31
x, y = {"a":1,"b":2}


Output

a b


Keys are unpacked

Q32
for k,v in d.items():


✅ Correct

Q33
for k,v in d:


❌ Error

ValueError: too many values to unpack

🔵 LEVEL 9: ENUMERATE & ZIP
Q34
enumerate([10,20,30])


Output

0 10
1 20
2 30

Q35
zip([1,2,3],[4,5,6])


Output

4
10
18

Q36
x, y = zip((1,2),(3,4))


Output

(1, 3) (2, 4)

🔴 LEVEL 10: TRAPS
Q37
a,b = b,a,


✅ Valid
Trailing comma still forms tuple

Q38
(a,b) = 1,2


✅ Parentheses = grouping

Q39
[a,b] = (1,2)


✅ LHS container type doesn’t matter

Q40
a,b = iter([1,2])


Uses iterator protocol

Q41
a,b = range(2)


Valid → 0 1

Q42
a,b = range(3)


❌ Too many values
