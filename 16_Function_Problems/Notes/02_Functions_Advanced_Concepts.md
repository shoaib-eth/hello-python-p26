# Python Advanced Functions – `lambda`, `*args`, `**kwargs`, `yield` & Recursion (Deep Internals)

⚠️ **READ THIS FIRST**
These notes are **NOT surface-level**.
They explain **WHAT happens in memory**, **WHY Python behaves this way**.

---

# PART 1️⃣ `lambda` Function – Anonymous Function Internals

## 1.1 What is a lambda function?

> **A lambda is just a function object WITHOUT a name.**

```python
add = lambda a, b: a + b
print(add(2, 3))
```

**Output:**
```
5
```

🧠 Internally:
- Python creates a **function object**
- No `def`, but same execution model

```
add ──▶ <function object>
           └── bytecode: a + b
```

---

## 1.2 Why lambda is limited (INTERVIEW 🔥)

Lambda can have:
- ❌ No statements
- ❌ No assignments
- ❌ No loops
- ❌ No `return`

Because:
> **Lambda is designed for expressions only**

```python
lambda x: x * x   # valid
lambda x: print(x)  # ❌ side-effect
```

---

## 1.3 When to use lambda (REAL USE)

```python
nums = [1, 2, 3]
print(list(map(lambda x: x*x, nums))). # [1, 4, 9]
```

🧠 Short-lived, throwaway logic.

---

# PART 2️⃣ `*args` – Variable Positional Arguments

## 2.1 What is `*args` REALLY?

```python
def total(*args):
    print(args)

total(1, 2, 3)
```

**Output:**
```
(1, 2, 3)
```

🧠 Internally:
- Python packs extra positional arguments into a **tuple**

```
args ──▶ (1, 2, 3)
```

---

## 2.2 Memory Visualization

```python
def demo(*args):
    pass

demo(10, 20)
```

```
Stack Frame: demo
-----------------
args → tuple (10, 20)
```

🧠 Tuple is immutable → safe to share.

---

## 2.3 Argument Unpacking

```python
nums = [1, 2, 3]
print(*nums)
```

**Output:**
```
1 2 3
```

🧠 `*` UNPACKS iterable.

---

# PART 3️⃣ `**kwargs` – Keyword Arguments Dictionary

## 3.1 What is `**kwargs`?

```python
def info(**kwargs):
    print(kwargs)

info(name="Shoaib", role="Engineer")
```

**Output:**
```
{'name': 'Shoaib', 'role': 'Engineer'}
```

🧠 Internally:
- Python packs keyword args into **dict**

```
kwargs ──▶ {'name': 'Shoaib', 'role': 'Engineer'}
```

---

## 3.2 Memory Model

```
Stack Frame
------------
kwargs → dict object
```

Mutable ⚠️

---

## 3.3 Combined Usage

```python
def func(a, *args, **kwargs):
    print(a, args, kwargs)

func(1, 2, 3, x=4)
```

**Output:**
```
1 (2, 3) {'x': 4}
```

---

# PART 4️⃣ `yield` – Generator Internals (VERY IMPORTANT 🔥)

## 4.1 What is `yield`?

> **`yield` turns a function into a generator.**

```python
def gen():
    yield 1
    yield 2
```

Calling it:
```python
g = gen()
print(g)
```

```
<generator object>
```

🧠 No code executed yet.

---

## 4.2 Generator Execution Model

```python
print(next(g))
print(next(g))
```

**Output:**
```
1
2
```

Then:
```python
next(g)
```

```
StopIteration
```

---

## 4.3 Memory Visualization (CRITICAL)

```
Generator Object
-----------------
Instruction pointer
Local variables
Suspended frame
```

🧠 Generator:
- DOES NOT die after yield
- Pauses execution
- Resumes later

---

## 4.4 `return` vs `yield`

| return | yield |
|------|------|
| Ends function | Pauses function |
| Frame destroyed | Frame preserved |
| Single value | Stream of values |

---

## 4.5 Why Generators are Memory Efficient

```python
range(10**9)
```

🧠 Values produced on demand.

---

# PART 5️⃣ Recursion – Stack Explosion Explained

## 5.1 What is Recursion?

> **Function calling itself.**

```python
def fact(n):
    if n == 0:
        return 1
    return n * fact(n-1)
```

---

## 5.2 Stack Frame Visualization

Calling `fact(3)`:

```
fact(3)
└── fact(2)
    └── fact(1)
        └── fact(0)
```

Each call = new frame.

---

## 5.3 Base Case – MOST IMPORTANT

Without base case:
- Infinite recursion
- Stack overflow

---

## 5.4 Memory Danger ⚠️

Python recursion limit ~1000.

```python
import sys
sys.getrecursionlimit()
```

---

## 5.5 Recursion vs Loop (INTERVIEW)

| Recursion | Loop |
|---------|-----|
| Elegant | Efficient |
| More memory | Less memory |
| Risky | Safe |

---

# PART 6️⃣ Common Traps & Answers 🎯

### Q1. Why lambda can’t have statements?
**Ans:** Lambda supports expressions only to keep it lightweight.

### Q2. Is `*args` tuple or list?
**Ans:** Tuple.

### Q3. Why generators are memory efficient?
**Ans:** They produce values lazily and keep state.

### Q4. Why recursion is dangerous in Python?
**Ans:** Limited stack depth.

---

## 🧠 FINAL MASTER MENTAL MODEL (LOCK THIS 🔒)

```
lambda  → lightweight function object
*args   → tuple packing
**kwargs→ dict packing
yield   → suspended frame
recursion→ stacked frames
```

---

## ✅ FINAL TAKEAWAY

> **Advanced functions control MEMORY, not just logic.**

Once this is clear:
- Generators feel natural
- Decorators become easy
- Debugging becomes logical

---

🔥 END – ADVANCED PYTHON FUNCTIONS

