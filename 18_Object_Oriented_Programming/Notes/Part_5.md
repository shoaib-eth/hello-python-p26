# Python Language — Object Oriented Programming (OOP)
## Part 5: Advanced OOP — Dunder Methods, Composition, Abstraction & Design Principles

> **Goal of Part 5 (Final Part)**
> - Understand Python’s **magic (dunder) methods** and object protocol
> - Learn **composition vs inheritance** (WHEN and WHY)
> - Understand **abstraction** the Pythonic way (ABCs)
> - Learn **core OOP design principles** used in real systems
> - See how everything connects (memory, dispatch, behavior)

This part completes OOP in Python. Nothing essential is skipped.

---

## 1️⃣ Dunder (Magic) Methods — The Object Protocol 🧙‍♂️

### What are dunder methods?
> Methods with double underscores (`__method__`) that Python **calls automatically** to implement object behavior.

They allow objects to integrate with:
- Operators
- Built-ins (`len`, `print`, `for`, `in`)
- Comparisons
- Attribute access

---

## 2️⃣ Object Creation & Representation Dunders

### `__new__` vs `__init__`

```python
class A:
    def __new__(cls):
        obj = super().__new__(cls)
        return obj

    def __init__(self):
        self.x = 10
```

- `__new__` → **creates** the object (rarely overridden)
- `__init__` → **initializes** the object

Memory flow:
```
__new__ → object allocated
__init__ → attributes assigned
```

---

### `__str__` and `__repr__`

```python
class User:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"User({self.name})"

    def __repr__(self):
        return f"User(name={self.name!r})"
```

```python
u = User("Alice")
print(u)
u
```

Output:
```
User(Alice)
User(name='Alice')
```

Rules:
- `__str__` → user-friendly
- `__repr__` → developer/debug-friendly

---

## 3️⃣ Attribute Access Control Dunders 🔐

### `__getattr__`, `__getattribute__`

```python
class Demo:
    def __getattr__(self, name):
        return f"{name} not found"
```

```python
d = Demo()
print(d.x)
```

Output:
```
x not found
```

Notes:
- `__getattribute__` runs **for every access** (dangerous)
- `__getattr__` runs **only if attribute is missing**

---

## 4️⃣ Callable Objects — `__call__` 📞

```python
class Counter:
    def __init__(self):
        self.count = 0

    def __call__(self):
        self.count += 1
        return self.count
```

```python
c = Counter()
print(c())
print(c())
```

Output:
```
1
2
```

Objects behaving like functions.

---

## 5️⃣ Container Protocol — Iteration & Membership 🔁

### `__len__`, `__iter__`, `__next__`, `__contains__`

```python
class Bag:
    def __init__(self, items):
        self.items = items

    def __len__(self):
        return len(self.items)

    def __contains__(self, item):
        return item in self.items
```

```python
b = Bag([1, 2, 3])
print(len(b))
print(2 in b)
```

Output:
```
3
True
```

---

## 6️⃣ Composition vs Inheritance (VERY IMPORTANT) 🧩

### Inheritance
```
Car IS-A Vehicle
```

### Composition
```
Car HAS-A Engine
```

---

### Composition Example

```python
class Engine:
    def start(self):
        print("Engine started")

class Car:
    def __init__(self):
        self.engine = Engine()

    def drive(self):
        self.engine.start()
        print("Car is moving")
```

Why composition is better:
- Less coupling
- More flexible
- Easier to change behavior

> **Rule:** Prefer composition over inheritance.

---

## 7️⃣ Abstraction in Python 🧠

### What is abstraction?
> Exposing **what an object does**, not **how it does it**.

Python uses **Abstract Base Classes (ABC)**.

---

### Abstract Base Class Example

```python
from abc import ABC, abstractmethod

class Payment(ABC):
    @abstractmethod
    def pay(self, amount):
        pass
```

```python
class CardPayment(Payment):
    def pay(self, amount):
        print(f"Paid {amount} by card")
```

```python
p = CardPayment()
p.pay(100)
```

Trying to instantiate `Payment` directly raises an error.

---

## 8️⃣ Why Use Abstraction? 🎯

- Enforces contracts
- Prevents incomplete implementations
- Makes large systems safe

---

## 9️⃣ Core OOP Design Principles (Python-Friendly SOLID) 🏗️

### S — Single Responsibility
One class → one reason to change

### O — Open/Closed
Open for extension, closed for modification

### L — Liskov Substitution
Child must be usable as parent

### I — Interface Segregation
Prefer small focused interfaces

### D — Dependency Inversion
Depend on abstractions, not concrete classes

---

## 🔟 Common OOP Anti-Patterns ⚠️

- God objects
- Deep inheritance chains
- Overusing `global`
- Clever but unreadable operator overloading

---

## 🧠 Final Unified Mental Model (LOCK THIS)

```
Object protocol → dunder methods
Behavior reuse  → composition > inheritance
Contracts       → abstraction (ABC)
Maintainability → SOLID principles
```

---

## ✅ End of Part 5 — OOP COMPLETE

You now understand:
- How objects work internally
- How Python dispatches behavior
- How to design clean, extensible systems

This completes **Object Oriented Programming in Python**.

---

✨ END — OOP IN PYTHON (PART 5)

