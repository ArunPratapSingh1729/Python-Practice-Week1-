 ** FOR THE LEARNING PURPOSE ONLY ** 

 MASTER LIST: Lambda Expression Errors (All Types)

---

## 🟥 1. **SyntaxError** (Most common)

### ❌ Cause

Using statements inside lambda

```python
lambda x:
    if x > 0:
        return x
```

### 🧠 Symptom

```
SyntaxError: invalid syntax
```

### ✅ Fix

Use expression-only form

```python
lambda x: x if x > 0 else -x
```

---

## 🟥 2. **Trying to use loops inside lambda**

### ❌ Cause

```python
lambda x: for i in x
```

### 🧠 Error

```
SyntaxError
```

### ✅ Fix

Use generator expressions

```python
lambda x: sum(i for i in x)
```

---

## 🟥 3. **Forgetting parentheses when calling lambda**

### ❌ Cause

```python
x = lambda n: n*n
print x(5)
```

### 🧠 Error

```
SyntaxError
```

### ✅ Fix

```python
print(x(5))
```

---

## 🟥 4. **Calling lambda incorrectly**

### ❌ Cause

```python
(lambda x: x+1)(5)
```

✔️ Correct

```python
lambda x: x+1(5)
```

❌ Wrong

### 🧠 Error

```
TypeError: 'int' object is not callable
```

---

## 🟥 5. **TypeError: 'str' / 'int' object is not callable**

### ❌ Cause

Overwriting function names

```python
sum = 10
sum([1,2,3])
```

### 🧠 Error

```
TypeError: 'int' object is not callable
```

### ✅ Fix

Never shadow built-ins

---

## 🟥 6. **Wrong unpacking in lambda**

### ❌ Cause

```python
lambda k, v: k+v   # but passing single value
```

### 🧠 Error

```
TypeError: cannot unpack non-iterable object
```

### ✅ Fix

Match unpacking to data structure

---

## 🟥 7. **Using lambda where list comprehension is needed**

### ❌ Cause

```python
list(lambda x: x*x for x in l)
```

### 🧠 Error

```
TypeError
```

### ✅ Fix

```python
[x*x for x in l]
```

---

## 🟥 8. **Misplacing `if–else` in lambda**

### ❌ Cause

```python
lambda x: if x > 0 else -x
```

### 🧠 Error

```
SyntaxError
```

### ✅ Fix

```python
lambda x: x if x > 0 else -x
```

---

## 🟥 9. **Using `if` filter incorrectly**

### ❌ Cause

```python
lambda x: x for x in l if x > 0
```

### 🧠 Error

```
SyntaxError
```

### ✅ Fix

Use comprehension or filter

---

## 🟥 10. **Returning nothing accidentally**

### ❌ Cause

```python
lambda x: print(x)
```

### 🧠 Result

Always returns `None`

### ✅ Fix

Use lambda only for expressions

---

# 🔵 Errors with map / filter / sorted

---

## 🟦 11. **Forgetting iterable in map/filter**

### ❌ Cause

```python
map(lambda x: x*x)
```

### 🧠 Error

```
TypeError
```

### ✅ Fix

```python
map(lambda x: x*x, l)
```

---

## 🟦 12. **Using filter expecting transformation**

### ❌ Cause

```python
filter(lambda x: x*x, l)
```

### 🧠 Bug

Keeps everything except zero

### ✅ Fix

Filter must return True/False

---

## 🟦 13. **sorted key misunderstanding**

### ❌ Cause

```python
sorted(words, key=lambda x: x > 3)
```

### 🧠 Bug

Wrong ordering

### ✅ Fix

Return comparison value

---

# 🟣 Dict / Set / Tuple specific lambda issues

---

## 🟪 14. **Trying to create dict directly inside lambda**

### ❌ Cause

```python
lambda x: {k:v for k,v in x.items()}
```

✔️ Valid but unreadable

### ✅ Advice

Use normal function or comprehension directly

---

## 🟪 15. **Assuming tuple comprehension exists**

### ❌ Cause

```python
(lambda x: (i*i for i in x))(l)
```

### 🧠 Confusion

This is a generator, not tuple

### ✅ Fix

Wrap with `tuple()`

---

## 🟪 16. **Shadowing variables inside lambda**

### ❌ Cause

```python
x = 10
f = lambda x: x + 1
```

🧠 Confusing but valid

### ✅ Advice

Use clear variable names

---

# 🟨 Logical errors (most dangerous)

---

## 🟨 17. **Expecting lambda to loop**

### ❌ Cause

Thinking lambda processes full list

### 🧠 Reality

Lambda handles **ONE element**

### ✅ Fix

Use map/filter/comprehension

---

## 🟨 18. **Using lambda where readability dies**

### ❌ Cause

Nested lambdas

### ✅ Fix

Switch to normal function

---

# 🔐 FINAL DEBUGGING CHECKLIST (SAVE THIS)

Before writing lambda, ask:

1. Am I returning an **expression**?
2. Am I processing **one element**?
3. Is iteration happening **outside**?
4. Am I shadowing a built-in?
5. Do I really need lambda here?

---

## 🏁 One-line truth

> **Lambda is for simple logic, not clever logic.**

You now have a **debugging map** most beginners don’t.
If you want next:

* lambda → comprehension conversion
* real debugging practice
* interview trick questions
