# Numeric Libraries in Python – Complete Practical Guide

This note explains **ALL IMPORTANT Python libraries related to numbers**, why they exist, **when to use which library**, and **how they are used in real code**.

This is extremely useful for **Data Science, ML, backend engineering, and interviews**.

---

## 1. Why Do We Need Numeric Libraries?

Python’s built-in numeric types (`int`, `float`, `complex`) are powerful, but:
- They cannot handle **exact decimal finance math** reliably
- They do not provide **advanced math/statistics**
- They are slow for **large-scale numeric computation**

Hence, Python provides **specialized numeric libraries**.

---

## 2. `math` Module (Core Numeric Library)

### Purpose
- Real-number mathematics
- Fast C-implemented math functions

### Import
```python
import math
```

### Common Functions

```python
import math
print(math.sqrt(16))
print(math.floor(3.7))
print(math.ceil(3.2))
print(math.trunc(-2.8))
```

**Output:**
```
4.0
3
4
-2
```

📌 Works only with **real numbers**, not complex.

---

## 3. `cmath` Module (Complex Math)

### Purpose
- Mathematical operations on **complex numbers**

### Import
```python
import cmath
```

### Example

```python
import cmath
print(cmath.sqrt(-1))
print(cmath.exp(1j))
```

**Output:**
```
1j
(0.5403023058681398+0.8414709848078965j)
```

📌 `cmath` ALWAYS returns complex results.

---

## 4. `decimal` Module (Exact Decimal Arithmetic)

### Purpose
- Accurate base-10 arithmetic
- Financial & accounting calculations

### Import
```python
from decimal import Decimal, getcontext
```

### Example

```python
from decimal import Decimal, getcontext
getcontext().prec = 4
print(Decimal('1') / Decimal('3'))
```

**Output:**
```
0.3333
```

📌 Avoid passing floats into `Decimal`.

---

## 5. `fractions` Module (Rational Numbers)

### Purpose
- Exact rational arithmetic (fractions)

### Import
```python
from fractions import Fraction
```

### Example

```python
from fractions import Fraction
f = Fraction(2, 3)
print(f)
print(f * 3)
```

**Output:**
```
2/3
2
```

---

## 6. `random` Module (Pseudo-Random Numbers)

### Purpose
- Random sampling
- Simulations
- ML data shuffling

### Import
```python
import random
```

### Examples

```python
import random
print(random.random())
print(random.randint(1, 10))
print(random.choice(["a", "b", "c"]))
```

**Output (example):**
```
0.42
7
b
```

📌 Outputs vary each run.

---

## 7. `statistics` Module (Descriptive Statistics)

### Purpose
- Mean, median, variance, stdev

### Import
```python
import statistics
```

### Example

```python
import statistics
data = [10, 20, 30, 40]
print(statistics.mean(data))
print(statistics.median(data))
```

**Output:**
```
25
25.0
```

---

## 8. `numbers` Module (Numeric Abstract Base Classes)

### Purpose
- Type checking for numeric behavior

### Import
```python
import numbers
```

### Example

```python
import numbers
print(isinstance(10, numbers.Integral))
print(isinstance(3.14, numbers.Real))
```

**Output:**
```
True
True
```

📌 Interview favorite.

---

## 9. `sys` Module (Numeric Limits & Info)

### Purpose
- System-level numeric information

### Example

```python
import sys
print(sys.maxsize)
print(sys.float_info.epsilon)
```

**Output (example):**
```
9223372036854775807
2.220446049250313e-16
```

---

## 10. `numpy` (Scientific & High-Performance Numbers)

### Purpose
- Fast numerical computing
- Vectorized operations
- Fixed-size numeric arrays

### Import
```python
import numpy as np
```

### Example

```python
import numpy as np
a = np.array([1, 2, 3])
print(a * 2)
```

**Output:**
```
[2 4 6]
```

📌 Used heavily in Data Science & ML.

---

## 11. `scipy` (Advanced Scientific Math)

### Purpose
- Optimization
- Linear algebra
- Numerical integration

### Example

```python
from scipy import linalg
import numpy as np
A = np.array([[1, 2], [3, 4]])
print(linalg.det(A))
```

**Output:**
```
-2.0
```

---

## 12. Comparison Table (When to Use What)

| Task | Library |
|----|-------|
| Basic math | math |
| Complex math | cmath |
| Finance | decimal |
| Fractions | fractions |
| Random numbers | random |
| Statistics | statistics |
| Type checking | numbers |
| Performance computing | numpy |
| Advanced science | scipy |

---

## 13. Interview Gold Tip

> **Use `decimal` for money, `numpy` for speed, `math` for simple calculations.**

---

## Final Takeaway

Python’s numeric power comes from **layered libraries**, each solving a specific numeric problem domain.

---

✅ End of Numeric Libraries Notes

