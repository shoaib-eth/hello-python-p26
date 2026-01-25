# Python Data Types – Zero to Advanced++ Deep Notes

These notes explain **ALL Python data types** in **extreme depth**, starting from absolute basics to **interview + real-world + Data Science level** understanding.

Python is **dynamically typed**, but **strongly typed**, and **everything in Python is an object**.

---

## 1. Numbers (Numeric Data Types)

Python supports multiple numeric types.

### 1.1 `int` (Integer)

```python
x = 10
print(x)
print(type(x))
```

**Output:**
```
10
<class 'int'>
```

Properties:
- Arbitrary precision (no overflow)
- Immutable

```python
x = 10
x = x + 5
print(x)
```

---

### 1.2 `float` (Floating Point)

```python
pi = 3.1415
print(type(pi))
```

⚠ Floating-point precision issue:

```python
print(0.1 + 0.2)
```

**Output:**
```
0.30000000000000004
```

---

### 1.3 `complex`

```python
z = 3 + 4j
print(z.real)
print(z.imag)
```

---

### 1.4 Binary, Octal, Hex

```python
b = 0b111   # binary
o = 0o12    # octal
h = 0xA     # hex
print(b, o, h)
```

---

### 1.5 `Decimal`

```python
from decimal import Decimal
x = Decimal('0.1') + Decimal('0.2')
print(x)
```

Used in **finance & accounting**.

---

### 1.6 `Fraction`

```python
from fractions import Fraction
f = Fraction(1, 3)
print(f)
```

---

## 2. Strings (`str`, `bytes`, `bytearray`)

### 2.1 `str` (Unicode String)

```python
s = "Hello Python"
print(s)
print(type(s))
```

Properties:
- Immutable
- Unicode by default

---

### 2.2 Indexing & Slicing

```python
print(s[0])
print(s[0:5])
```

---

### 2.3 `bytes`

```python
b = b'a\x01c'
print(b)
print(type(b))
```

Used in networking & binary files.

---

### 2.4 `bytearray`

```python
ba = bytearray(b'abc')
ba[0] = 100
print(ba)
```

Mutable version of bytes.

---

## 3. List (`list`)

```python
lst = [1, 2, 3]
print(lst)
```

Properties:
- Ordered
- Mutable
- Allows duplicates

---

### Common Operations

```python
lst.append(4)
lst[0] = 100
print(lst)
```

---

## 4. Tuple (`tuple`)

```python
t = (1, 'spam', 4)
print(t)
```

Properties:
- Ordered
- Immutable

---

### Named Tuple

```python
from collections import namedtuple
Point = namedtuple('Point', ['x', 'y'])
p = Point(2, 3)
print(p.x, p.y)
```

---

## 5. Dictionary (`dict`)

```python
d = {'food': 'spam', 'taste': 'yum'}
print(d['food'])
```

Properties:
- Key-value store
- Keys must be immutable

---

### Dictionary Creation Styles

```python
d1 = dict(hours=10)
d2 = dict([('a', 1), ('b', 2)])
```

---

## 6. Set (`set`, `frozenset`)

```python
s = {'a', 'b', 'c'}
print(s)
```

Properties:
- Unordered
- Unique values

---

### Set Operations

```python
a = {1, 2, 3}
b = {3, 4}
print(a & b)
print(a | b)
```

---

## 7. Boolean (`bool`)

```python
x = True
y = False
print(type(x))
```

Internally:
- `True` → 1
- `False` → 0

---

## 8. None (`NoneType`)

```python
x = None
print(x)
print(type(x))
```

Used to represent absence of value.

---

## 9. Functions

```python
def add(a, b):
    return a + b

print(type(add))
```

Functions are **first-class objects**.

---

## 10. Classes & Objects

```python
class User:
    def __init__(self, name):
        self.name = name

u = User('Shoaib')
print(type(u))
```

---

## 11. Modules & Packages

```python
import math
print(type(math))
```

---

## 12. Advanced Object Types

### 12.1 Iterators

```python
it = iter([1, 2, 3])
print(next(it))
```

---

### 12.2 Generators

```python
def gen():
    yield 1
    yield 2

for i in gen():
    print(i)
```

---

### 12.3 Decorators

```python
def my_dec(fn):
    def wrapper():
        print('Before')
        fn()
    return wrapper
```

---

### 12.4 Metaprogramming (Intro)

```python
class Meta(type):
    pass
```

---

## 13. File Object (Not a Data Type)

```python
f = open('hello.txt', 'w')
f.write('Hello')
f.close()
```

File is an **OS-level resource handler**, not a pure data type.

---

## 14. Mutable vs Immutable Summary

| Type | Mutable |
|---|---|
| int | ❌ |
| str | ❌ |
| list | ✅ |
| dict | ✅ |
| set | ✅ |
| tuple | ❌ |

---

## 15. Interview Takeaways

- Everything is an object
- Data type defines behavior
- Mutability affects bugs
- Numbers & strings are immutable

---

## 16. Final Mental Model

```
Variable → Reference → Object → Type
```

---

## 17. Code Examples WITH OUTPUT (Consolidated)

This section shows **actual Python shell outputs** for the most important examples above. These are exactly what you would see in `>>>` shell.

---

### Numbers

```python
>>> x = 10
>>> type(x)
<class 'int'>
>>> x + 5
15
```

```python
>>> 0.1 + 0.2
0.30000000000000004
```

```python
>>> from decimal import Decimal
>>> Decimal('0.1') + Decimal('0.2')
Decimal('0.3')
```

---

### Strings

```python
>>> s = "Hello"
>>> s[0]
'H'
>>> s + " World"
'Hello World'
```

```python
>>> b = b'ac'
>>> b
b'ac'
```

---

### List (Mutable)

```python
>>> lst = [1, 2, 3]
>>> lst.append(4)
>>> lst
[1, 2, 3, 4]
```

---

### Tuple (Immutable)

```python
>>> t = (1, 2, 3)
>>> t[0]
1
>>> t[0] = 10
TypeError: 'tuple' object does not support item assignment
```

---

### Dictionary

```python
>>> d = {'food': 'spam', 'taste': 'yum'}
>>> d['food']
'spam'
>>> d['price'] = 100
>>> d
{'food': 'spam', 'taste': 'yum', 'price': 100}
```

---

### Set

```python
>>> a = {1, 2, 3}
>>> b = {3, 4}
>>> a & b
{3}
>>> a | b
{1, 2, 3, 4}
```

---

### Boolean

```python
>>> True + True
2
>>> False == 0
True
```

---

### None

```python
>>> x = None
>>> x is None
True
```

---

### Function Object

```python
>>> def add(a, b): return a + b
>>> add(2, 3)
5
>>> type(add)
<class 'function'>
```

---

### Class & Object

```python
>>> class User:
...     def __init__(self, name): self.name = name
...
>>> u = User('Shoaib')
>>> u.name
'Shoaib'
```

---

### Iterator

```python
>>> it = iter([1, 2, 3])
>>> next(it)
1
>>> next(it)
2
```

---

### Generator

```python
>>> def gen():
...     yield 1
...     yield 2
...
>>> list(gen())
[1, 2]
```

---

### Mutability Proof

```python
>>> x = 10
>>> y = x
>>> x = 15
>>> y
10
```

```python
>>> a = [1, 2]
>>> b = a
>>> a.append(3)
>>> b
[1, 2, 3]
```

---

### File Object

```python
>>> f = open('hello.txt', 'w')
>>> f.write('Hello')
5
>>> f.close()
```

---

## Final Interview Reminder

> **Mutable objects change in-place, immutable objects create new memory. Variables only hold references.**

---

✅ End of Python Data Types Notes

