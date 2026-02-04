# Python Language — DECORATORS 

> **Important note (read this first)**
>
> Decorators feel hard **only because people start from syntax**.
>
> In these notes we will start from:
>
> 1. Functions as objects
> 2. Functions inside functions
> 3. Returning functions
> 4. THEN decorators
>
> If you understand the flow below, **decorators will feel natural, not magical** ✨

---

## 1️⃣ What is a Decorator? (Very Simple Definition)

> A **decorator** is a function that **takes another function**, **adds extra behavior**, and **returns a new function** — *without modifying the original code*.

In one line:

```
Decorator = function → modifies another function
```

Think of decorators like **wrapping a gift 🎁**:

- Gift = original function
- Wrapper paper = decorator
- Gift inside stays same, but presentation/behavior changes

---

## 2️⃣ Why Do We Need Decorators? (Real Problem)

Imagine you want to:

- Log function calls
- Measure execution time
- Check permissions
- Validate inputs

❌ BAD approach (repeating code):

```python
def func1():
    print("Logging...")
    print("Function 1")


def func2():
    print("Logging...")
    print("Function 2")
```

Problems:

- Code duplication
- Hard to maintain
- Violates DRY principle

✅ Decorators solve this **cleanly**.

---

## 3️⃣ VERY IMPORTANT FOUNDATION — Functions Are Objects 🧠

In Python:

```python
def greet():
    print("Hello")
```

This means:

- `greet` is a **variable**
- It points to a **function object in memory**

```python
print(greet)
```

Output (example):

```
<function greet at 0x102fae8b0>
```

Because functions are objects, we can:

- Pass them as arguments
- Return them from other functions
- Store them in variables

Decorators are built **entirely on this fact**.

---

## 4️⃣ Functions Inside Functions (Step 1)

```python
def outer():
    def inner():
        print("I am inner")
    print("I am outer")
```

Nothing special yet.

Key idea:

> Functions can live **inside** other functions

---

## 5️⃣ Returning a Function (Step 2 — VERY IMPORTANT)

```python
def outer():
    def inner():
        print("Hello from inner")
    return inner
```

Usage:

```python
my_func = outer()
my_func()
```

Output:

```
Hello from inner
```

What happened?

- `outer()` returned `inner`
- `my_func` now points to `inner`

👉 This is the **core mechanic** behind decorators.

---

## 6️⃣ Passing a Function as Argument (Step 3)

```python
def shout(func):
    func()
```

```python
def say_hello():
    print("hello")

shout(say_hello)
```

Output:

```
hello
```

So now we know:

- Functions can be **passed in**
- Functions can be **returned out**

Now we are READY for decorators 💥

---

## 7️⃣ Your FIRST Decorator (NO @ yet)

```python
def my_decorator(func):
    def wrapper():
        print("Before function")
        func()
        print("After function")
    return wrapper
```

Using it manually:

```python
def say_hi():
    print("Hi")

say_hi = my_decorator(say_hi)
say_hi()
```

Output:

```
Before function
Hi
After function
```

What happened internally?

1. `say_hi` passed into `my_decorator`
2. `wrapper` created
3. `wrapper` returned
4. `say_hi` now points to `wrapper`

Original function is **wrapped**, not changed.

---

## 8️⃣ The `@decorator` Syntax (Just Syntactic Sugar 🍬)

This:

```python
@my_decorator
def say_hi():
    print("Hi")
```

Is EXACTLY SAME as:

```python
def say_hi():
    print("Hi")

say_hi = my_decorator(say_hi)
```

No magic. Just cleaner syntax.

---

## 9️⃣ Decorators with Arguments (\*args, \*\*kwargs)

Problem:

```python
def add(a, b):
    print(a + b)
```

Wrapper must accept **any arguments**.

Correct decorator:

```python
def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("Before")
        result = func(*args, **kwargs)
        print("After")
        return result
    return wrapper
```

Usage:

```python
@my_decorator
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

## 🔟 REAL WORLD EXAMPLE — Authentication 🔐

```python
def login_required(func):
    def wrapper(user):
        if user != "admin":
            print("Access denied")
            return
        return func(user)
    return wrapper
```

```python
@login_required
def dashboard(user):
    print(f"Welcome {user}")
```

```python
dashboard("admin")
dashboard("guest")
```

Output:

```
Welcome admin
Access denied
```

Decorator = security guard 🚨

---

## 1️⃣1️⃣ Decorators Returning Values

Always remember:

> Wrapper should return the original function’s return value

Otherwise you lose it.

---

## 1️⃣2️⃣ Multiple Decorators 🔗

```python
@decorator1
@decorator2
def func():
    pass
```

Execution order:

```
func = decorator1(decorator2(func))
```

Bottom decorator runs first.

---

## 1️⃣3️⃣ Built‑in Decorators (IMPORTANT)

### `@staticmethod`

- No `self`

### `@classmethod`

- Receives `cls`

### `@property`

- Converts method → attribute

You already used these in OOP.

---

## 1️⃣4️⃣ Common Decorator Mistakes ⚠️

❌ Forgetting `return func()` ❌ Not using `*args, **kwargs` ❌ Thinking decorators modify original function

---

## 🧠 FINAL MENTAL MODEL (LOCK THIS)

```
Function → object in memory
Decorator → function wrapping another function
@syntax → assignment shortcut
Wrapper → controls execution
```

---

## 🎯 Questions You MUST Be Ready For

### Q1. What is a decorator?

A function that modifies another function without changing its source code.

### Q2. Are decorators executed at definition or call time?

Definition time.

### Q3. Why use \*args and \*\*kwargs?

To support any function signature.

---

## ✅ What You Should Feel Now

If you understand:

- Why wrapper exists
- Why functions are returned
- Why @ is just syntax

👉 Decorators are **NOT hard anymore** 😄

---

✨ END — Python Decorators (Complete Guide)

