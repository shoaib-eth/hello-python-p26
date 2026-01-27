# Numbers in Python – Zero to Advanced++ Deep Notes

These notes explain **NUMBERS in Python** in extreme depth — from basics to **internal behavior, precision, operator overloading, and interview-level subtleties**.

Python’s numeric system is **powerful, flexible, and very different from C/C++/Java**.

---

## 1. Big Picture: Numbers in Python

Python treats **numbers as objects**, not primitives.

That means:
- Numbers have **types**
- Numbers have **methods**
- Numbers participate in **operator overloading**
- Numbers are **immutable objects**

```python
x = 10
```

Internally:
```
x ───▶ int object (value=10)
```

---

## 2. How Many Numeric Types Does Python Support?

Python supports **6 main numeric types**:

1. `int`
2. `float`
3. `complex`
4. `bool` (subclass of int)
5. `Decimal` (from decimal module)
6. `Fraction` (from fractions module)

---

## 3. `int` – Integer Numbers (Unlimited Precision)

### 3.1 Basic Usage

```python
x = 2
y = 3
z = 4
(x + y) * z
```

**Output:**
```
20
```

---

### 3.2 Unlimited Precision (VERY IMPORTANT)

Unlike C/C++:
- Python integers **never overflow**
- Memory grows dynamically

```python
z ** 100
```

```python
2 ** 1000
```

✔ Python allocates more memory automatically

---

### 3.3 Why No Overflow?

Because:
- Python `int` is implemented as **variable-length object**
- Internally stored in base 2^30 (CPython)

---

## 4. `float` – Floating Point Numbers

### 4.1 Based on IEEE-754

```python
40 + 2.5
```

**Output:**
```
42.5
```

---

### 4.2 Precision Problem

```python
0.1 + 0.2
```

**Output:**
```
0.30000000000000004
```

Reason:
- Binary representation cannot exactly store 0.1

---

### 4.3 Conversions

```python
int(2.23)
float(50)
```

---

## 5. `Decimal` – Exact Decimal Arithmetic

```python
from decimal import Decimal
Decimal('0.1') + Decimal('0.1') + Decimal('0.1')
```

**Output:**
```
Decimal('0.3')
```

Used in:
- Finance
- Banking
- Accounting

---

## 6. `Fraction` – Rational Numbers

```python
from fractions import Fraction
Fraction(1, 3)
```

Stores numbers as numerator / denominator

---

## 7. `complex` – Complex Numbers

```python
2 + 1j
(2 + 1j) * 3
```

Attributes:
- `.real`
- `.imag`

---

## 8. Boolean (`bool`) – Subclass of int

```python
True == 1
False == 0
True + 4
```

Why?
- `bool` inherits from `int`

---

## 9. Numeric Operators & Overloading

Python operators are **method calls**:

```python
x + y   → x.__add__(y)
x ** y  → x.__pow__(y)
```

This is why:
- Custom numeric behavior is possible

---

## 10. Power Operator `**`

```python
z ** 2
z ** 10
z ** 100
```

Python handles huge powers safely

---

## 11. Comparison Operators

```python
1 < 2
5 == 6
1 == 2 < 3
```

Chained comparison:
```
1 == 2 < 3  → (1 == 2) and (2 < 3)
```

---

## 12. Representation Functions

```python
repr('hello')
str('hello')
print('hello')
```

Purpose:
- `repr()` → unambiguous
- `str()` → readable

---

## 13. Math Module

```python
import math
math.floor(3.5)
math.floor(-3.5)
math.trunc(-2.8)
```

Difference:
- `floor()` → towards −∞
- `trunc()` → towards 0

---

## 14. Number Systems (Base Conversion)

```python
0o20   # Octal
0xFF   # Hex
0b1000 # Binary
```

Conversions:
```python
oct(67)
hex(89)
bin(30)
```

Parsing:
```python
int('64', 8)
int('64', 16)
int('1000', 2)
```

---

## 15. Bitwise Operations

```python
x = 1
x << 4
```

Left shift = multiply by powers of 2

---

## 16. Random Numbers

```python
import random
random.random()
random.randint(1, 10)
random.choice(['hello', 'hey', 'bonjour'])
random.shuffle(l1)
```

Used in:
- Simulations
- ML sampling
- Games

---

## 17. Sets & Numeric Logic

```python
setone = {1, 2, 3, 4}
setone & {1, 3}
setone | {1, 2, 7}
setone - {1, 2, 3, 4}
```

---

## 18. Type Introspection (Important)

```python
type(1)
type(True)
type(bool)
type({})
```

---

## 19. Numeric Immutability

```python
x = 5
x = x + 2
```

Creates a NEW integer object

---

## 20. Why Python Numbers Feel Powerful

- Unlimited precision
- Operator overloading
- Multiple numeric domains
- Clean syntax

---

## 21. Interview Mental Model

```
Numbers are objects
No overflow
Precision depends on type
Operators are methods
```

---

## 22. Final Takeaway

> **Python numbers are high-level, safe, flexible numeric objects designed for correctness over raw speed.**

---

✅ End of Numbers in Python Notes

