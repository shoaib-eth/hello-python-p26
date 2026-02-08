# Python Dictionaries – Complete Notes

These notes explain **Python Dictionaries (`dict`)** from **absolute basics to deep internals**, with:
- Real-world use cases 🌍
- Memory & hashing internals 🧠
- ALL dictionary methods
- Code examples with OUTPUT
- Performance tips ⚡
- Interview questions & answers 🎯

---

## 1️⃣ What is a Dictionary? (Why do we use it?) 🤔

A **dictionary** is a **mutable collection of key–value pairs**, optimized for **fast lookups**.

### 🧠 Why dictionaries exist
- To store data with **meaningful keys** instead of numeric indexes
- To get **O(1) average-time access**

### 🌍 Real-world examples
- User profile → `{id: 101, name: "Alice"}`
- JSON / API responses
- Config files
- Database-like records

---

## 2️⃣ Creating Dictionaries (ALL Ways) 🧱

### 2.1 Literal syntax

```python
d = {'name': 'Alice', 'age': 20}
print(d)
print(type(d))
```

**Output:**
```
{'name': 'Alice', 'age': 20}
<class 'dict'>
```

---

### 2.2 `dict()` constructor

```python
d = dict(name='Alice', age=20)
print(d)
```

**Output:**
```
{'name': 'Alice', 'age': 20}
```

---

### 2.3 From list of tuples

```python
d = dict([('a', 1), ('b', 2)])
print(d)
```

**Output:**
```
{'a': 1, 'b': 2}
```

---

## 3️⃣ Dictionary Rules (VERY IMPORTANT) ⚠️

- ✅ Keys must be **immutable** (`int`, `str`, `tuple`)
- ❌ Keys cannot be mutable (`list`, `dict`)
- ✅ Values can be **anything**

```python
d = {(1, 2): 'ok'}
print(d)
```

**Output:**
```
{(1, 2): 'ok'}
```

---

## 4️⃣ Accessing & Modifying Data 🔑

```python
d = {'name': 'Alice', 'age': 20}
print(d['name'])
d['age'] = 21
print(d)
```

**Output:**
```
Alice
{'name': 'Alice', 'age': 21}
```

---

## 5️⃣ Safe Access: `get()` 🛡️

```python
print(d.get('name'))
print(d.get('salary', 0))
```

**Output:**
```
Alice
0
```

---

## 6️⃣ Adding & Removing Items ➕➖

### Add / Update

```python
d['city'] = 'Delhi'
print(d)
```

**Output:**
```
{'name': 'Alice', 'age': 21, 'city': 'Delhi'}
```

---

### Remove: `pop`, `del`, `clear`

```python
print(d.pop('city'))
del d['age']
print(d)
```

**Output:**
```
Delhi
{'name': 'Alice'}
```

---

## 7️⃣ Dictionary Methods (COMPLETE LIST) 🧰

```python
d = {'a': 1, 'b': 2}
print(d.keys())
print(d.values())
print(d.items())
```

**Output:**
```
dict_keys(['a', 'b'])
dict_values([1, 2])
dict_items([('a', 1), ('b', 2)])
```

---

### `update()`

```python
d.update({'c': 3})
print(d)
```

**Output:**
```
{'a': 1, 'b': 2, 'c': 3}
```

---

### `setdefault()` (Interview favorite 🎯)

```python
scores = {}
scores.setdefault('math', 0)
print(scores)
```

**Output:**
```
{'math': 0}
```

---

## 8️⃣ Looping Through Dictionaries 🔁

```python
d = {'a': 1, 'b': 2}
for k, v in d.items():
    print(k, v)
```

**Output:**
```
a 1
b 2
```

---

## 9️⃣ Dictionary Comprehensions (VERY IMPORTANT) 🧠

```python
squares = {x: x*x for x in range(4)}
print(squares)
```

**Output:**
```
{0: 0, 1: 1, 2: 4, 3: 9}
```

---

## 🔟 Nested Dictionaries 🪜

```python
user = {
    'name': 'Alice',
    'skills': {'python': 'advanced', 'solidity': 'advanced'}
}
print(user['skills']['python'])
```

**Output:**
```
advanced
```

---

## 1️⃣1️⃣ Dictionary Internals (HASH TABLE) 🧠🔥

- Dictionaries use **hash tables**
- Key → `hash(key)` → bucket
- Average lookup time: **O(1)**

```python
print(hash('python'))
```

---

## 1️⃣2️⃣ Mutability & Reference Behavior ⚠️

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

## 1️⃣3️⃣ Performance Tips ⚡

- Use dict for lookups, not lists
- Prefer `get()` over try/except
- Keys should be simple & immutable

---

## 1️⃣4️⃣ Common Interview Traps ❌

- ❌ Using list as key
- ❌ Assuming order (pre Python 3.7)
- ❌ Modifying dict while iterating

---

## 1️⃣5️⃣ Questions & Answers 🎯

### Q1. Why dictionary keys must be immutable?
**Ans:** Because hashing requires stable values.

### Q2. Time complexity of dict lookup?
**Ans:** O(1) average, O(n) worst-case.

### Q3. Difference between `get()` and `[]`?
**Ans:** `get()` avoids KeyError.

### Q4. Is dict ordered?
**Ans:** Yes, insertion-ordered from Python 3.7+.

---

## 🧠 Mental Model (Must Remember)

```
Dictionary = Hash Table
Keys → Hash → Buckets
Fast lookup
Mutable container
```

---

## ✅ Final Takeaway

> **Python dictionaries are mutable, hash-based data structures designed for fast key-based access and real-world data modeling.**

---

🔥 End of Python Dictionary Notes

