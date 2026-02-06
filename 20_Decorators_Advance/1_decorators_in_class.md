# Python Language — DECORATORS

## Part 1: Class-Based Decorators (From Confusion → Clarity)

> **Why this part is IMPORTANT**
>
> You already understand **function-based decorators**.
>
> Class-based decorators answer the next big questions:
>
> - Why is a class sometimes better than a function?
> - How do decorators maintain **state** cleanly?
> - What is the role of `__init__` and `__call__`?
>
> Once this clicks, decorators stop being "syntax" and become **objects with behavior** 🧠

---

## 1️⃣ First Reality Check — Decorators Are CALLED OBJECTS

Very important idea:

```
@decorator

def my_func():
    pass
```

Python only requires **decorator to be callable**.

That means:

- Functions are callable ✅
- Classes with `__call__` are callable ✅

👉 **Decorator does NOT have to be a function**.

---

## 2️⃣ Why Use Class-Based Decorators? 🤔

Function decorators work great, BUT:

❌ Problems with function decorators:

- State is hidden inside closures
- Harder to debug
- Complex logic becomes messy

✅ Class decorators help when:

- You need **persistent state**
- You want cleaner structure
- You want object-oriented clarity

Think of it as:

```
Function decorator → lightweight
Class decorator    → heavy-duty
```

---

## 3️⃣ Smallest Possible Class-Based Decorator 🧱

Let’s build the **simplest** one.

```python
class MyDecorator:
    def __init__(self, func):
        self.func = func

    def __call__(self):
        print("Before function")
        self.func()
        print("After function")
```

Usage:

```python
@MyDecorator
def say_hi():
    print("Hi")

say_hi()
```

---

### 🔍 What Happens Internally (STEP BY STEP)

At definition time:

```python
say_hi = MyDecorator(say_hi)
```

So:

- `__init__` runs ONCE
- `self.func` stores original function

At call time:

```python
say_hi()
```

Actually runs:

```python
say_hi.__call__()
```

---

### Output

```
Before function
Hi
After function
```

---

## 4️⃣ Memory Visualization 🧠

```
say_hi ──▶ MyDecorator instance
              ├── func ──▶ original say_hi function
```

Decorator is now an **object sitting between caller and function**.

---

## 5️⃣ Adding Arguments Support (\*args, \*\*kwargs)

Real decorators must support **any function signature**.

```python
class MyDecorator:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        print("Before")
        result = self.func(*args, **kwargs)
        print("After")
        return result
```

Usage:

```python
@MyDecorator
def add(a, b):
    return a + b

print(add(2, 3))
```

Output:

```
Before
After
5
```

---

## 6️⃣ Stateful Decorator — Counting Calls 🔢

This is where class decorators shine ✨

```python
class CallCounter:
    def __init__(self, func):
        self.func = func
        self.count = 0

    def __call__(self, *args, **kwargs):
        self.count += 1
        print(f"Call #{self.count}")
        return self.func(*args, **kwargs)
```

Usage:

```python
@CallCounter
def greet(name):
    print(f"Hello {name}")


greet("Alice")
greet("Bob")
```

Output:

```
Call #1
Hello Alice
Call #2
Hello Bob
```

---

### 🧠 Why This Is Powerful

- `count` lives on the **decorator object**
- No closure confusion
- State is explicit and readable

---

## 7️⃣ Class Decorator WITH Arguments (Advanced but Important)

Sometimes decorators themselves need arguments.

Example:

```python
@retry(3)
def fetch_data():
    pass
```

This requires **two layers**.

---

### Implementation

```python
class Retry:
    def __init__(self, retries):
        self.retries = retries

    def __call__(self, func):
        def wrapper(*args, **kwargs):
            for attempt in range(self.retries):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    print(f"Attempt {attempt+1} failed")
            raise Exception("All retries failed")
        return wrapper
```

Usage:

```python
@Retry(3)
def unstable():
    print("Trying...")
    raise ValueError("Fail")
```

---

## 8️⃣ Definition-Time vs Call-Time (FINAL CLARITY)

```python
@MyDecorator

def f():
    pass
```

Definition time:

- `MyDecorator(f)` → object created

Call time:

- `__call__` executes

---

## 9️⃣ When to Use Class-Based vs Function-Based Decorators

| Situation      | Use                |
| -------------- | ------------------ |
| Simple logging | Function decorator |
| Timing         | Function decorator |
| Caching        | Either             |
| Counting calls | Class decorator    |
| Stateful retry | Class decorator    |

---

## 🔟 Gold Questions 🎯

### Q1. Why use class-based decorators?

Because they manage state cleanly and are easier to extend.

### Q2. What makes a class callable?

The presence of `__call__` method.

### Q3. When does `__init__` run?

At decoration (definition) time.

### Q4. When does `__call__` run?

At function invocation time.

---

## 🧠 FINAL MENTAL MODEL (LOCK THIS)

```
Decorator = callable object
__init__  → setup (once)
__call__  → execution (every call)
State     → stored on object
```

---

✨ END — Decorators Part 1

