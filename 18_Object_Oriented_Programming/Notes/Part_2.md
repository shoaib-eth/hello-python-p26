# Python Language — Object Oriented Programming (OOP)
## Part 2: Encapsulation, Class vs Instance Variables & Properties

> **Goal of Part 2**
> - Understand **Encapsulation** in Python (what it really means)
> - Clearly distinguish **instance variables vs class variables**
> - Learn Python’s access conventions (`_` and `__`)
> - Master **properties** (`@property`, setters, getters)
> - Understand memory behavior 

Nothing is skipped. Everything is explained with examples, output, and visualization.

---

## 1️⃣ What Is Encapsulation? 🧠

### Definition
> **Encapsulation** is the concept of **bundling data and methods together** and **controlling how data is accessed or modified**.

Encapsulation answers two questions:
1. Who is allowed to access this data?
2. Who is allowed to modify this data?

---

## 2️⃣ Why Encapsulation Exists (Real Reason) 🔐

Without encapsulation:
- Any part of the program can modify data
- Bugs become unpredictable
- Invariants break easily

Encapsulation provides:
- Safety
- Control
- Maintainability

---

## 3️⃣ Encapsulation in Python vs Other Languages ⚠️

Important truth:
> **Python does NOT enforce strict access control** like Java or C++.

Instead, Python uses **conventions**, not restrictions.

---

## 4️⃣ Public Members (Default Behavior) 🌍

```python
class BankAccount:
    def __init__(self, balance):
        self.balance = balance
```

### Usage
```python
acc = BankAccount(1000)
print(acc.balance)
acc.balance = 500
print(acc.balance)
```

### Output
```
1000
500
```

### Explanation
- `balance` is public
- Anyone can read or modify it

---

## 5️⃣ Why Public Data Can Be Dangerous ❌

Example problem:
```python
acc.balance = -10
```

This breaks business rules.

Encapsulation exists to **prevent invalid states**.

---

## 6️⃣ Protected Members (`_variable`) 🟡

```python
class BankAccount:
    def __init__(self, balance):
        self._balance = balance
```

### Meaning
- `_balance` is **protected by convention**
- Signals: *“Do not touch from outside unless you know what you are doing”*

### Important
> Python does NOT block access.

```python
acc._balance = -100  # Allowed, but discouraged
```

---

## 7️⃣ Private Members (`__variable`) 🔒

```python
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance
```

### What REALLY happens (CRITICAL)
Python performs **name mangling**.

```python
self.__balance  →  self._BankAccount__balance
```

### Proof
```python
print(acc.__dict__)
```

Output (example):
```
{'_BankAccount__balance': 1000}
```

---

## 8️⃣ Name Mangling (Interview Favorite) 🎯

Purpose:
- Avoid accidental override in subclasses
- Not for security

Accessing it manually:
```python
acc._BankAccount__balance
```

> This shows Python privacy is **by convention, not enforcement**.

---

## 9️⃣ Instance Variables 🧱

### Definition
> Instance variables belong to **individual objects**.

```python
class User:
    def __init__(self, name):
        self.name = name
```

### Memory
```
user1.name → "Alice"
user2.name → "Bob"
```

Each object has its own copy.

---

## 🔟 Class Variables 🏢

### Definition
> Class variables are **shared by all instances**.

```python
class User:
    role = "member"  # class variable

    def __init__(self, name):
        self.name = name
```

### Usage
```python
u1 = User("Alice")
u2 = User("Bob")

print(u1.role)
print(u2.role)
```

### Output
```
member
member
```

---

## 1️⃣1️⃣ Class vs Instance Variable (IMPORTANT DIFFERENCE)

```python
u1.role = "admin"
```

Now memory becomes:
```
u1.__dict__ → {'name': 'Alice', 'role': 'admin'}
User.role   → 'member'
```

Result:
```python
print(u1.role)  # admin
print(u2.role)  # member
```

---

## 1️⃣2️⃣ Variable Lookup Order (VERY IMPORTANT) 🔍

When accessing `obj.attr`:
1. Instance dictionary
2. Class dictionary
3. Parent classes

This explains shadowing behavior.

---

## 1️⃣3️⃣ Why Encapsulation Needs Properties ⚙️

We want:
- Controlled access
- Validation
- Clean syntax

But without changing how users access attributes.

---

## 1️⃣4️⃣ Property (`@property`) — The Pythonic Way ✨

```python
class BankAccount:
    def __init__(self, balance):
        self._balance = balance

    @property
    def balance(self):
        return self._balance
```

### Usage
```python
acc = BankAccount(1000)
print(acc.balance)
```

### Output
```
1000
```

Looks like attribute, behaves like method.

---

## 1️⃣5️⃣ Setter with Validation 🚧

```python
class BankAccount:
    def __init__(self, balance):
        self._balance = balance

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, value):
        if value < 0:
            raise ValueError("Balance cannot be negative")
        self._balance = value
```

### Usage
```python
acc.balance = 500
acc.balance = -10
```

### Output
```
ValueError: Balance cannot be negative
```

---

## 1️⃣6️⃣ Why Properties Are Better Than `global` or Direct Access ✅

Properties:
- Hide implementation
- Protect invariants
- Allow refactoring without breaking code

> **Professional Python code prefers properties.**

---

## 1️⃣7️⃣ Encapsulation Memory Model 🧠

```
Object
------
_balance → actual data
balance  → controlled interface (property)
```

Users interact with `balance`, not `_balance`.

---

## 1️⃣8️⃣ Common Questions 🎯

### Q1. Does Python have private variables?
**Answer:** No, Python uses name mangling and conventions.

### Q2. Difference between `_x` and `__x`?
**Answer:** `_x` is a convention; `__x` triggers name mangling.

### Q3. Why use properties?
**Answer:** To control access while keeping attribute syntax.

---

## 🧠 Final Mental Model (LOCK THIS)

```
Public      → open access
_Protected  → internal use
__Private   → name mangling
@property      → controlled access
```

---

## ✅ End of Part 2

Next Part:
**Part 3 — Inheritance, `super()`, Method Overriding & MRO**

This is where OOP becomes powerful.

---

✨ END — OOP IN PYTHON (PART 2)

