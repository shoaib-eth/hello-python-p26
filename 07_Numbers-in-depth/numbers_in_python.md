# Numbers in Python – Deep Notes (With Code & Output)

These notes explain **Python Numbers** from **absolute basics to advanced internals**, with **EVERY code example followed by its OUTPUT**.

This document is written assuming **no prior shell experiments** — everything is explained cleanly and independently.

---

## 1. Numbers in Python: Core Idea

In Python:
- Numbers are **objects**
- Numbers are **immutable**
- Numbers have **types & methods**
- Python supports **multiple numeric systems**

```python
x = 10
print(type(x))
```

**Output:**
```
<class 'int'>
```

---

## 2. Integer (`int`) – Unlimited Precision

### 2.1 Basic Integer Arithmetic

```python
x = 2
y = 3
print(x + y)
print(x * y)
```

**Output:**
```
5
6
```

---

### 2.2 Power Operator & Big Integers

```python
print(2 ** 10)
print(2 ** 100)
```

**Output:**
```
1024
1267650600228229401496703205376
```

✔ No overflow
✔ Memory grows dynamically

---

## 3. Floating Point (`float`)

### 3.1 Float Basics

```python
x = 40 + 2.5
print(x)
print(type(x))
```

**Output:**
```
42.5
<class 'float'>
```

---

### 3.2 Floating Point Precision Problem

```python
print(0.1 + 0.2)
```

**Output:**
```
0.30000000000000004
```

Reason: Binary floating-point representation (IEEE-754)

---

## 4. Type Conversion (Casting)

```python
print(int(2.99))
print(float(50))
```

**Output:**
```
2
50.0
```

---

## 5. Decimal – Exact Arithmetic

```python
from decimal import Decimal
print(Decimal('0.1') + Decimal('0.2'))
```

**Output:**
```
Decimal('0.3')
```

Used in finance & accounting

---

## 6. Fraction – Rational Numbers

```python
from fractions import Fraction
f = Fraction(1, 3)
print(f)
print(f * 3)
```

**Output:**
```
1/3
1
```

---

## 7. Complex Numbers (`complex`)

```python
z = 2 + 3j
print(z)
print(z.real)
print(z.imag)
```

**Output:**
```
(2+3j)
2.0
3.0
```

---

## 8. Boolean Numbers (`bool`)

```python
print(True + 4)
print(False == 0)
print(True == 1)
```

**Output:**
```
5
True
True
```

✔ `bool` is subclass of `int`

---

## 9. Comparison Operators

```python
print(1 < 2)
print(5 == 6)
print(1 == 2 < 3)
```

**Output:**
```
True
False
False
```

---

## 10. Operator Overloading (Internal Working)

```python
x = 5
y = 3
print(x + y)
```

Internally:
```
x.__add__(y)
```

**Output:**
```
8
```

---

## 11. Representation Functions

```python
print(repr('hello'))
print(str('hello'))
print('hello')
```

**Output:**
```
"'hello'"
'hello'
hello
```

---

## 12. Math Module

```python
import math
print(math.floor(3.9))
print(math.floor(-3.5))
print(math.trunc(-2.8))
```

**Output:**
```
3
-4
-2
```

---

## 13. Number Systems (Binary, Octal, Hex)

```python
print(0b1000)
print(0o20)
print(0xFF)
```

**Output:**
```
8
16
255
```

---

## 14. Base Conversion Functions

```python
print(bin(30))
print(oct(67))
print(hex(89))
```

**Output:**
```
0b11110
0o103
0x59
```

---

## 15. Parsing Numbers from Strings

```python
print(int('64', 8))
print(int('64', 16))
print(int('1000', 2))
```

**Output:**
```
52
100
8
```

---

## 16. Bitwise Operations

```python
x = 1
print(x << 4)
```

**Output:**
```
16
```

---

## 17. Random Numbers

```python
import random
print(random.random())
print(random.randint(1, 5))
```

**Output (example):**
```
0.483920184
3
```

---

## 18. Numeric Immutability

```python
x = 5
x = x + 2
print(x)
```

**Output:**
```
7
```

✔ New integer object created

---

## 19. Type Checking

```python
print(type(1))
print(type(True))
print(type(3.14))
```

**Output:**
```
<class 'int'>
<class 'bool'>
<class 'float'>
```

---

## 20. Final Mental Model

```
Numbers are objects
Numbers are immutable
Precision depends on numeric type
Operators call methods
```

---

## Final Takeaway

> **Python numbers prioritize correctness, safety, and flexibility over low-level speed.**

---

✅ End of Numbers in Python (With Output) Notes

