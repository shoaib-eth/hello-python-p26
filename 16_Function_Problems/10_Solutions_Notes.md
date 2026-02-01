# Python Language — Functions Practice (Line-by-Line Deep Notes with Memory Visualization)

> **Goal of these notes**
> - Explain each solution **line by line** 
> - Understand what happens **in memory during function calls**
> - Build strong intuition for `lambda`, `*args`, `**kwargs`, `yield`, and `recursion`

---

## 1. Basic Function Syntax — Square of a Number

```python
def calculate_square(number):
    result = number ** 2
    return result
```

### Line-by-line explanation
- `def calculate_square(number)`
  - A function object named `calculate_square` is created in global memory.
  - `number` will be a **local variable** when the function is called.

- `result = number ** 2`
  - `**` is the exponent operator.
  - A new integer object is created and assigned to `result`.

- `return result`
  - The function exits immediately.
  - The value of `result` is returned to the caller.

### Memory visualization
```
Global Memory
-------------
calculate_square → function object

Call Stack (during call)
------------------------
calculate_square frame
  number → 5
  result → 25
```

After `return`, the stack frame is destroyed.

---

## 2. Function with Multiple Parameters — Sum of Two Numbers

```python
def calculate_sum(num1, num2):
    result = num1 + num2
    return result
```

### Key concept
- Each parameter gets its **own local binding**.
- Parameters exist only inside the function stack frame.

### Call-time memory
```
calculate_sum frame
-------------------
num1 → 10
num2 → 20
result → 30
```

### About `map(int, input().split())`
- `input()` returns a string
- `split()` converts it into a list of strings
- `map(int, ...)` converts each value into an integer

---

## 3. Polymorphism in Functions — `multiply`

```python
def multiply(a, b):
    return a * b
```

### Important idea
> Python functions do not enforce data types. The **operator decides behavior**.

- `int * int` → numeric multiplication
- `int * str` → string repetition

### Memory behavior
```
a → 3
b → "hi"
return → "hihihi"
```

This is an example of **operator overloading**.

---

## 4. Function Returning Multiple Values — Circle Statistics

```python
def circle_stats(radius):
    area = math.pi * radius ** 2
    circumference = 2 * math.pi * radius
    return area, circumference
```

### Key truth
> Python returns **a tuple**, not multiple values.

```python
return area, circumference
```
is internally:
```python
return (area, circumference)
```

### Unpacking
```python
area, circumference = circle_stats(radius)
```

Memory:
```
returned tuple → (78.5, 31.4)
area → 78.5
circumference → 31.4
```

---

## 5. Default Parameter Value — Greeting Function

```python
def greet(name="Alice"):
    return f"Hello 👋 {name}"
```

### Concept
- Default values are evaluated **once at function definition time**.
- If no argument is passed, the default is used.

### Calls
```python
greet("Bob")   → Hello Bob
greet()        → Hello Alice
```

### Input validation
```python
if input_name.strip() == "":
```
- `strip()` removes whitespace
- Empty string triggers default behavior

---

## 6. Lambda Function — Cube of a Number

```python
cube = lambda x: x ** 3
```

### Important truth
> A lambda is still a **function object**, just without a name.

Equivalent to:
```python
def cube(x):
    return x ** 3
```

### Limitations
- One expression only
- No statements, assignments, or loops

Memory:
```
cube → function object
```

---

## 7. Function with `*args`

```python
def sum_all(*args):
    print(args)
    for i in args:
        print(i * 2)
```

### Core idea
> `*args` packs all positional arguments into a **tuple**.

Call:
```python
sum_all(1, 2, 3)
```

Memory:
```
args → (1, 2, 3)
```

### Why tuple?
- Immutable
- Predictable
- Safe to reuse

---

## 8. Function with `**kwargs`

```python
def print_kwargs(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")
```

### Core idea
> `**kwargs` packs keyword arguments into a **dictionary**.

Call:
```python
print_kwargs(name="Alice", role="Data Scientist")
```

Memory:
```
kwargs → {
  "name": "Alice",
  "role": "Data Scientist"
}
```

---

## 9. Generator Function — `yield` (Memory-Focused)

```python
def even_generator(limit):
    for i in range(2, limit + 1, 2):
        yield i
```

### Core idea
> `yield` pauses the function instead of terminating it.

Call:
```python
g = even_generator(10)
```

Memory:
```
g → generator object
  • instruction pointer
  • local variable i
```

### Step-by-step execution
- `next(g)` → yields 2, pauses
- `next(g)` → yields 4, pauses
- Continues until exhausted

The function frame is **preserved**, not destroyed.

---

## 10. Recursive Function — Factorial

```python
def factorial(num):
    if num == 0:
        return 1
    return num * factorial(num - 1)
```

### Core idea
> A function calls itself with a smaller problem.

### Base case
```python
if num == 0:
    return 1
```
Prevents infinite recursion.

### Call stack visualization (`factorial(3)`)
```
factorial(3)
  → 3 * factorial(2)
      → 2 * factorial(1)
          → 1 * factorial(0)
              → return 1
```

### Stack unwinding
```
factorial(1) → 1
factorial(2) → 2
factorial(3) → 6
```

Each call creates a new stack frame.

---

## Final Summary (Mental Model)

```
Normal function → frame created → frame destroyed
*args           → tuple packing
**kwargs        → dictionary packing
lambda          → unnamed function object
yield           → pause & resume same frame
recursion       → multiple frames on call stack
```

---

## Final Takeaway

> **Functions control both logic and memory.**

If you understand these ten examples and their memory behavior, your function fundamentals are strong and interview-ready.

