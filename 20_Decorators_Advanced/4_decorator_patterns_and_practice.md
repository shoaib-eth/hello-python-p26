# Python Language — DECORATORS

## Part 4: Real-World Decorator Patterns & Practice (LOCK-IN MODE 🔒)

> **Purpose of this part**
>
> Part 1 → mechanics Part 2 → frameworks Part 3 → generators vs decorators
>
> **Part 4 is where decorators become muscle memory.**
>
> We will build the **same decorators used in production systems**, step by step, with:
>
> - real use-cases
> - execution flow
> - memory behavior
> - interview insights

---

## 1️⃣ Logging Decorator 📝 (MOST COMMON)

### Problem

You want to log whenever a function is called.

### Decorator

```python
def log_call(func):
    def wrapper(*args, **kwargs):
        print(f"Calling function: {func.__name__}")
        return func(*args, **kwargs)
    return wrapper
```

### Usage

```python
@log_call
def add(a, b):
    return a + b

print(add(2, 3))
```

### Output

```
Calling function: add
5
```

### Mental Model

```
Caller → wrapper → original function
```

---

## 2️⃣ Timing Decorator ⏱️ (Performance Monitoring)

### Problem

Measure how long a function takes.

### Decorator

```python
import time

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} took {end - start:.4f} seconds")
        return result
    return wrapper
```

### Usage

```python
@timer
def slow_task():
    time.sleep(1)

slow_task()
```

### Output

```
slow_task took 1.000x seconds
```

### Real World

- API latency
- DB query timing

---

## 3️⃣ Authorization Decorator 🔐

### Problem

Only allow authorized users.

### Decorator

```python
def authorize(func):
    def wrapper(user, *args, **kwargs):
        if not user.get("is_admin"):
            print("Access Denied")
            return
        return func(user, *args, **kwargs)
    return wrapper
```

### Usage

```python
@authenticate
def delete_user(user):
    print("User deleted")

admin = {"is_admin": True}
user = {"is_admin": False}

delete_user(admin)
delete_user(user)
```

### Output

```
User deleted
Access Denied
```

---

## 4️⃣ Retry Decorator 🔁 (Fault Tolerance)

### Problem

Retry a failing function.

### Decorator

```python
def retry(times):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for attempt in range(times):
                try:
                    return func(*args, **kwargs)
                except Exception:
                    print(f"Retry {attempt + 1}")
            raise Exception("All retries failed")
        return wrapper
    return decorator
```

### Usage

```python
@retry(3)
def unstable():
    print("Trying")
    raise ValueError("Fail")

unstable()
```

---

## 5️⃣ Caching Decorator 🧠 (Performance Booster)

### Problem

Avoid recomputation.

### Decorator

```python
def cache(func):
    storage = {}

    def wrapper(*args):
        if args in storage:
            return storage[args]
        result = func(*args)
        storage[args] = result
        return result

    return wrapper
```

### Usage

```python
@cache
def slow_add(a, b):
    time.sleep(2)
    return a + b

print(slow_add(2, 3))
print(slow_add(2, 3))
```

### Output

```
5
5  # instant
```

### Memory Visualization

```
wrapper → storage { (2,3): 5 }
```

---

## 6️⃣ Decorator Stacking 🔗

```python
@log_call
@timer
def compute():
    time.sleep(1)
```

Equivalent to:

```python
compute = log_call(timer(compute))
```

### Execution Order

```
Caller → log → timer → function
```

---

## 7️⃣ Common Mistakes ❌

- Forgetting `return func(...)`
- Not using `*args, **kwargs`
- Confusing decorator execution time

---

## 8️⃣ Interview GOLD 🎯

### Q1. Why use decorators?

To add cross-cutting behavior without modifying core logic.

### Q2. When do decorators execute?

At function definition time.

### Q3. Why closures are important in decorators?

They allow persistent state across calls.

---

## 🧠 FINAL MASTER MODEL

```
Decorator = control layer
Wrapper = gatekeeper
Function = pure logic
Closure/Object = memory
```

---

## 🏁 DECORATORS COMPLETE

You now understand decorators from:

- syntax
- memory
- frameworks
- real-world systems

You are officially **advanced Python decorator ready** 🚀

---

✨ END — Decorators Part 4

