# Python Dictionary – Missing & Extra Concepts (Add-On Notes)

These notes cover **dictionary concepts that were NOT fully explicit earlier.**

All examples are **cleaned, structured, and generalized 🎯**

---

## 1️⃣ Updating Values vs Syntax Errors ⚠️

### ❌ Wrong way (Syntax Error)

```python
d = {'a': 1}
d['a' = 2]
```

**Output:**
```
SyntaxError: cannot assign to literal
```

### ✅ Correct way

```python
d['a'] = 2
print(d)
```

**Output:**
```
{'a': 2}
```

🧠 **Reason**: Assignment (`=`) works only on variables, not inside indexing.

---

## 2️⃣ Looping Over Dictionary (DEFAULT BEHAVIOR) 🔁

```python
d = {'x': 10, 'y': 20}
for item in d:
    print(item)
```

**Output:**
```
x
y
```

🧠 Looping over a dictionary **iterates over KEYS by default**.

---

## 3️⃣ Looping: Keys, Values & Items (Clear Difference) 🔍

```python
d = {'x': 10, 'y': 20}

for k in d.keys():
    print(k)

for v in d.values():
    print(v)

for k, v in d.items():
    print(k, v)
```

**Output:**
```
x
y
10
20
x 10
y 20
```

---

## 4️⃣ Membership Test Checks KEYS Only 🔐

```python
d = {'x': 10, 'y': 20}
print('x' in d)
print(10 in d)
```

**Output:**
```
True
False
```

🧠 `in` always checks **keys**, not values.

---

## 5️⃣ `pop()` vs `popitem()` (INTERVIEW FAVORITE 🎯)

```python
d = {'a': 1, 'b': 2}
print(d.pop('a'))
print(d)
```

**Output:**
```
1
{'b': 2}
```

```python
d = {'a': 1, 'b': 2}
print(d.popitem())
print(d)
```

**Output:**
```
('b', 2)
{'a': 1}
```

🧠 `popitem()` removes the **last inserted item** (Python 3.7+).

---

## 6️⃣ `del` vs `pop()` 🗑️

```python
d = {'a': 1, 'b': 2}
del d['a']
print(d)
```

**Output:**
```
{'b': 2}
```

Difference:
- `pop()` → returns value
- `del` → no return

---

## 7️⃣ `copy()` vs Reference Assignment ⚠️

### ❌ Reference assignment

```python
a = {'x': 1}
b = a
b['y'] = 2
print(a)
```

**Output:**
```
{'x': 1, 'y': 2}
```

---

### ✅ Shallow copy

```python
a = {'x': 1}
b = a.copy()
b['y'] = 2
print(a)
print(b)
```

**Output:**
```
{'x': 1}
{'x': 1, 'y': 2}
```

---

## 8️⃣ Nested Dictionaries 🪜

```python
store = {
    'fruits': {'apple': 10, 'banana': 5},
    'drinks': {'water': 20}
}

print(store['fruits']['apple'])
```

**Output:**
```
10
```

---

## 9️⃣ Dictionary Comprehension (Revisited) 🧠

```python
squares = {x: x**2 for x in range(5)}
print(squares)
```

**Output:**
```
{0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
```

---

## 🔟 `clear()` Method 🧹

```python
d = {'a': 1, 'b': 2}
d.clear()
print(d)
```

**Output:**
```
{}
```

---

## 1️⃣1️⃣ `dict.fromkeys()` (LESS KNOWN BUT IMPORTANT) ⭐

```python
keys = ['x', 'y', 'z']
default = 0
d = dict.fromkeys(keys, default)
print(d)
```

**Output:**
```
{'x': 0, 'y': 0, 'z': 0}
```

## 🎯 Interview Questions & Answers

### Q1. What does looping over a dict return by default?
**Ans:** Keys.

### Q2. Difference between `pop()` and `popitem()`?
**Ans:** `pop()` removes by key, `popitem()` removes last inserted item.

### Q3. What does `in` check in dictionaries?
**Ans:** Keys only.

### Q4. Is `dict.copy()` deep copy?
**Ans:** No, it’s shallow copy.

---

## 🧠 Final Mental Model

```
Dict = Hash Table
Keys → Hash → Buckets
Iteration → Keys
Copy ≠ Reference
```

---

✅ End of Dictionary Add-On Notes

