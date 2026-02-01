# Python Language — Scope & Closures 

> **Goal of this document**
> - Understand how Python resolves variable names (Scope)
> - Understand how functions *remember* variables (Closures)
> - Visualize memory and stack/heap behavior
> - Know when `global` / `nonlocal` should and should NOT be used

No shortcuts. No skipped concepts.

---

## PART 1️⃣ — What Is Scope in Python?

### Definition
**Scope** defines **where a variable name is visible and accessible** in a program.

Python decides which variable a name refers to using a strict rule called **LEGB**.

---

## PART 2️⃣ — The LEGB Rule (CRITICAL)

When Python encounters a variable name, it searches in this exact order:

```
L → Local
E → Enclosing
G → Global
B → Built‑in
```

The **first match wins**.

---

## PART 3️⃣ — Local Scope

```python
def demo():
    x = 10
    print(x)

demo()
```

### Explanation
- `x` exists **only inside** `demo`
- Created when the function is called
- Destroyed when the function returns

### Memory visualization
```
Call Stack
----------
demo frame
  x → 10
```

Outside the function:
```python
print(x)  # NameError
```

---

## PART 4️⃣ — Global Scope

```python
x = 5

def show():
    print(x)

show()
```

### Explanation
- `x` is stored in **global memory**
- Functions can READ global variables

### Memory
```
Global Memory
-------------
x → 5
show → function object
```

---

## PART 5️⃣ — Local vs Global Shadowing

```python
x = 10

def demo():
    x = 20
    print(x)

demo()
print(x)
```

### Output
```
20
10
```

### Why?
- Local `x` **shadows** global `x`
- No modification happens to global variable

---

## PART 6️⃣ — The `global` Keyword (VERY IMPORTANT)

### What `global` Does

```python
x = 10

def change():
    global x
    x = 50

change()
print(x)
```

### Output
```
50
```

### Memory behavior
- `global x` tells Python: *do NOT create local `x`*
- Assignment modifies **global memory directly**

---

## PART 7️⃣ — SHOULD You Use `global`?

### ❌ Why `global` Is Dangerous

1. Hidden side‑effects
2. Hard to debug
3. Breaks modularity
4. Makes functions non‑reusable

```python
# Dangerous
def update():
    global count
    count += 1
```

You cannot understand this function without reading global code.

## PART 8️⃣ — Built‑in Scope

```python
print(len([1, 2, 3]))
```

- `len` lives in **built‑in scope**
- Overriding built‑ins is dangerous

```python
len = 10
len([1,2,3])  # TypeError
```

---

## PART 9️⃣ — Enclosing Scope (Gateway to Closures)

```python
def outer():
    x = 10
    def inner():
        print(x)
    inner()

outer()
```

### Explanation
- `x` is **not local** to `inner`
- It is found in **enclosing scope**

---

## PART 🔟 — What Is a Closure?

### Definition (IMPORTANT)

> A **closure** is a function that **remembers variables from its enclosing scope even after that scope has finished execution**.

---

## PART 1️⃣1️⃣ — Basic Closure Example

```python
def outer():
    x = 10
    def inner():
        return x
    return inner

f = outer()
print(f())
```

### Output
```
10
```

### WHY THIS WORKS (KEY QUESTION)
- `outer()` has already finished
- Its stack frame is gone
- Yet `inner` still knows `x`

---

## PART 1️⃣2️⃣ — Closure Memory Visualization (CRITICAL 🔥)

When `outer()` executes:
```
Stack Frame: outer
------------------
x → 10
inner → function object
```

When `outer()` returns:
```
f → inner function object
inner.__closure__ → (cell containing x)
```

### Important truth
> Python **packs captured variables into closure cells** stored on the heap.

This is called **closure packing**.

---

## PART 1️⃣3️⃣ — Closure Packing Explained (DEPTH)

```python
def outer():
    x = 10
    def inner():
        return x
    return inner
```

Internally:
- `x` is copied into a **cell object**
- Cell is attached to `inner`

```
inner
 ├─ __code__
 ├─ __globals__
 └─ __closure__ → cell(x=10)
```

Even after `outer` exits, the cell survives.

---

## PART 1️⃣4️⃣ — Inspecting Closures (Advanced)

```python
print(f.__closure__[0].cell_contents)
```

Output:
```
10
```

This proves:
- `x` is stored separately from stack
- Closure uses **heap memory**

---

## PART 1️⃣5️⃣ — Modifying Enclosing Variables: `nonlocal`

```python
def outer():
    x = 0
    def inner():
        nonlocal x
        x += 1
        return x
    return inner

f = outer()
print(f())
print(f())
```

### Output
```
1
2
```

### Explanation
- `nonlocal` allows modification of closure variable
- Without `nonlocal` → UnboundLocalError

---

## PART 1️⃣6️⃣ — Closures vs Globals

| Closures | Globals |
|--------|--------|
| Encapsulated | Shared everywhere |
| Safe | Error‑prone |
| Testable | Hard to test |

> **Closures are a controlled alternative to `global`.**

---

## PART 1️⃣7️⃣ — Common Closure Pitfall (INTERVIEW FAVORITE)

```python
funcs = []
for i in range(3):
    def f():
        return i
    funcs.append(f)

print(funcs[0](), funcs[1](), funcs[2]())
```

### Output
```
2 2 2
```

### WHY?
- Closures capture **variable, not value**
- `i` changes over loop

### Fix
```python
def make_func(i):
    def f():
        return i
    return f
```

---

## PART 1️⃣8️⃣ — Questions & Answers

### Q1. How does Python resolve variable names?
**Ans:** Using the LEGB rule.

### Q2. Why are globals discouraged?
**Ans:** They introduce hidden dependencies and side‑effects.

### Q3. Where are closure variables stored?
**Ans:** In heap‑allocated cell objects attached to the function.

### Q4. Difference between `global` and `nonlocal`?
**Ans:** `global` modifies global scope; `nonlocal` modifies enclosing scope.

---

## FINAL MASTER MENTAL MODEL

```
Local      → stack frame
Global     → module memory
Closure    → heap cell
LEGB       → name resolution order
```

---

## FINAL TAKEAWAY

> **Scope controls visibility. Closures control lifetime.**

If you understand this document fully:
- Decorators become easy
- Callbacks make sense
- Bugs related to variables disappear

---

🔥 END — PYTHON SCOPE & CLOSURES

