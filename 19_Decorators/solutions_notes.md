# Python Language — Decorators (Deep Dive Before Advanced Parts)
## Timing, Debugging & Caching Decorators — Line‑by‑Line Explained

> **Why these notes exist**
>
> These 3 decorator examples look *small*, but internally they use:
> - Closures
> - `*args`, `**kwargs`
> - Function metadata (`__name__`)
> - Dictionaries as memory
> - Execution‑time vs definition‑time behavior
>
> If these feel confusing, **it’s normal**. After this document, they will feel *obvious*.

---

# 🧠 Mental Model You MUST Hold

Before touching code, lock this in:

```
@decorator
function()

⬇️ means

function = decorator(function)
```

- Decorator runs **once at definition time**
- Wrapper runs **every time the function is called**
- Any variable in decorator body = **persistent memory (closure)**

Keep this model active while reading.

---

## 🧩 Solution 1 — Timing Function Execution ⏱️

### Goal
Measure how long a function takes to execute.

---

### Full Code
```python
import time


def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} ran in {end-start} time")
        return result

    return wrapper


@timer
def example_func(n):
    time.sleep(n)


example_func(2)
```

---

### Step 1️⃣ — What Happens at Definition Time

```python
@timer
def example_func(n):
```

Internally Python does:

```python
example_func = timer(example_func)
```

So:
- `timer()` runs **once**
- `func` → original `example_func`
- `wrapper` is returned
- `example_func` now points to `wrapper`

⚠️ The original function is **not lost**, it lives inside `wrapper` via closure.

---

### Step 2️⃣ — Wrapper Execution (Call Time)

```python
example_func(2)
```

Actually runs:
```python
wrapper(2)
```

---

### Step 3️⃣ — Line‑by‑Line Wrapper Explanation

```python
start = time.time()
```
- Captures **current timestamp** (seconds since epoch)

```python
result = func(*args, **kwargs)
```
- Calls the **original function**
- `func` is still accessible via closure
- `time.sleep(2)` executes here

```python
end = time.time()
```
- Captures end timestamp

```python
print(f"{func.__name__} ran in {end-start} time")
```
- `__name__` gives original function name
- Difference = execution time

```python
return result
```
- IMPORTANT: preserves original return value

---

### Output (approximate)
```
example_func ran in 2.0021 time
```

---

### 🔑 Key Takeaways
- Timing logic is **outside** function
- Function code remains clean
- Decorator adds behavior transparently

---

## 🧩 Solution 2 — Debugging Function Calls 🐞

### Goal
Log:
- Function name
- Positional arguments
- Keyword arguments

---

### Full Code
```python
def debug(func):
    def wrapper(*args, **kwargs):
        args_value = " ,".join(str(arg) for arg in args)
        kwargs_value = " ,".join(f"{k} : {v}" for k, v in kwargs.items())
        print(
            f"Calling: {func.__name__} with args {args_value} and kwargs {kwargs_value}"
        )
        return func(*args, **kwargs)

    return wrapper
```

---

### Step 1️⃣ — Understanding `args` and `kwargs`

```python
*args   → tuple of positional arguments
**kwargs → dictionary of keyword arguments
```

This allows decorator to work with **any function signature**.

---

### Step 2️⃣ — Formatting Arguments

```python
args_value = " ,".join(str(arg) for arg in args)
```
- Iterates over tuple
- Converts each arg to string
- Joins them for display

```python
kwargs_value = " ,".join(f"{k} : {v}" for k, v in kwargs.items())
```
- Iterates over dictionary
- Formats key:value pairs

---

### Step 3️⃣ — Printing Debug Information

```python
print(f"Calling: {func.__name__} with args {args_value} and kwargs {kwargs_value}")
```

Example output:
```
Calling: greet with args Alice and kwargs greeting : Hola
```

---

### Step 4️⃣ — Returning Function Result

```python
return func(*args, **kwargs)
```

⚠️ Without this return, original function output is lost.

---

### Usage Example
```python
@debug
def greet(name, greeting="Hello 👋"):
    print(f"{greeting}, {name}")
```

Call:
```python
greet("Alice", greeting="Hola")
```

Output:
```
Calling: greet with args Alice and kwargs greeting : Hola
Hola, Alice
```

---

### 🔑 Key Takeaways
- Debug decorators are **logging tools**
- Extremely common in real systems
- Frameworks use similar logic internally

---

## 🧩 Solution 3 — Caching Return Values 🧠 (Most Important)

### Goal
Avoid recomputation by storing previous results.

---

### Full Code
```python
import time


def cache(func):
    cahce_value = {}
    print(cahce_value)

    def wrapper(*args, **kwargs):
        if args in cahce_value:
            return cahce_value[args]
        result = func(*args, **kwargs)
        cahce_value[args] = result
        return result

    return wrapper
```

---

### Step 1️⃣ — Definition‑Time Memory Creation (CRITICAL)

```python
cahce_value = {}
```

This dictionary:
- Is created **once**
- Lives in decorator’s scope
- Is captured by `wrapper` (closure)

👉 This is **persistent memory**.

---

### Step 2️⃣ — Wrapper Execution Logic

```python
if args in cahce_value:
    return cahce_value[args]
```

- Checks if same arguments were used before
- Uses tuple `args` as dictionary key

⚠️ Only works if arguments are **hashable**.

---

### Step 3️⃣ — Cache Miss

```python
result = func(*args, **kwargs)
```

- Function actually executes
- `time.sleep(4)` happens here

```python
cahce_value[args] = result
```

- Result stored in cache

---

### Usage
```python
@cache
def long_running_function(a, b):
    time.sleep(4)
    return a + b
```

---

### Call Sequence

```python
print(long_running_function(1, 2))
```
- Takes ~4 seconds

```python
print(long_running_function(1, 2))
```
- Returns instantly

```python
print(long_running_function(3, 2))
```
- Takes ~4 seconds again

---

### Output (timing simplified)
```
3
3
5
```

---

### 🔑 Key Takeaways
- Decorators can **store state**
- Cache is a real‑world performance optimization
- Python’s `functools.lru_cache` works on same principle

---

## 🧠 FINAL SUPER IMPORTANT SUMMARY (LOCK THIS)

```
Decorator runs → once (definition time)
Wrapper runs   → every call
Closure memory → persists across calls
*args/**kwargs → universal compatibility
```

---

## ✅ After These Notes, You Should Be Able To

- Explain **why cache works**
- Explain **where memory is stored**
- Explain **why wrapper has access to func**
- Write your own timing/debug/cache decorators

If this is clear, you are **READY for Part 1–4 roadmap** 🚀

---

✨ END — Decorator Practice (Deep Explanation)

