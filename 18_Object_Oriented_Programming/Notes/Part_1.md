# Python Language — Object Oriented Programming (OOP)
## Part 1: Foundations & Core Concepts

> **Important note (read first)**
Object Oriented Programming in Python is a **very large topic**.
To ensure **no concept is missed**, these notes will be divided into **multiple parts**.

### Planned Structure
- **Part 1 (this document)**: What OOP is, why it exists, classes, objects, `__init__`, attributes, methods
- **Part 2**: Encapsulation, access conventions, properties, class vs instance variables
- **Part 3**: Inheritance, method overriding, `super()`, MRO
- **Part 4**: Polymorphism, duck typing, operator overloading
- **Part 5**: Advanced OOP — dunder methods, composition, abstraction, design principles

We will go **slow, visual, and deep**. Nothing will be skipped.

---

## 1️⃣ What Is Object Oriented Programming? 🤔

### Simple definition
> **Object Oriented Programming (OOP)** is a way of structuring programs by **modeling real-world entities as objects** that combine **data (state)** and **behavior (methods)**.

---

## 2️⃣ Why OOP Exists (The REAL Reason) 🧠

Before OOP, programs were written using only:
- Variables
- Functions

This is called **procedural programming**.

### Problem with procedural style ❌
- Data and functions are scattered
- Hard to manage large codebases
- Changes in data require changes in many functions

### OOP solution ✅
OOP **bundles related data and behavior together**.

```
Data + Functions  →  Object
```

This makes code:
- Easier to understand
- Easier to extend
- Easier to maintain

---

## 3️⃣ Real-World Analogy 🌍

### Example: Car 🚗

A car has:
- **Data (state)**: color, speed, fuel
- **Behavior**: start(), stop(), accelerate()

In OOP:
```
Car → Class
MyCar → Object
```

---

## 4️⃣ Core Pillars of OOP 🏛️

OOP is built on four pillars:

1. **Class**
2. **Object**
3. **Encapsulation**
4. **Inheritance**
5. **Polymorphism**
6. **Abstraction**

(Yes, Python practitioners often include 5 pillars.)

We will cover **all of them**, step by step.

---

## 5️⃣ Class — The Blueprint 🧩

### Definition
> A **class** is a blueprint that defines:
- What data an object will have
- What actions an object can perform

### Basic class example

```python
class Car:
    pass
```

This defines a class named `Car`.

🧠 At this point:
- No object exists
- Only a **class object** is created in memory

---

## 6️⃣ Object — The Real Instance 🧍

### Creating an object

```python
my_car = Car()
```

### Memory visualization
```
Global Memory
-------------
Car     → class object
my_car  → instance of Car
```

> **Class** = blueprint
> **Object** = real thing built from blueprint

---

## 7️⃣ `__init__` — Object Initialization ⚙️

### What is `__init__`?

> `__init__` is a **special method** that runs automatically when an object is created.

### Example

```python
class Car:
    def __init__(self, color, speed):
        self.color = color
        self.speed = speed
```

### Creating object

```python
car1 = Car("Red", 0)
```

---

## 8️⃣ Understanding `self` (CRITICAL) 🔥

### What is `self`?

> `self` refers to the **current object**.

It allows the object to:
- Store its own data
- Access its own attributes

### Memory visualization
```
car1
 ├─ color → "Red"
 └─ speed → 0
```

`self.color = color` means:
> Store `color` **inside this object**.

---

## 9️⃣ Instance Attributes 🧱

```python
class Car:
    def __init__(self, color):
        self.color = color
```

Each object gets **its own copy**.

```python
car1 = Car("Red")
car2 = Car("Blue")
```

Memory:
```
car1.color → Red
car2.color → Blue
```

Objects do **not share** instance attributes.

---

## 🔟 Instance Methods 🛠️

### Defining methods

```python
class Car:
    def start(self):
        print("Car started")
```

### Calling method

```python
car1.start()
```

Internally:
```python
Car.start(car1)
```

🧠 Python automatically passes `self`.

---

## 1️⃣1️⃣ Full Example (Class + Object + Methods)

```python
class Car:
    def __init__(self, color):
        self.color = color

    def describe(self):
        print(f"This car is {self.color}")

car1 = Car("Red")
car2 = Car("Blue")

car1.describe()
car2.describe()
```

### Output
```
This car is Red
This car is Blue
```

---

## 1️⃣2️⃣ Flow of Object Creation 🔄

```python
car1 = Car("Red")
```

Execution flow:
1. `Car` class is found
2. New empty object is created
3. `__init__` is called
4. Attributes are assigned
5. Object reference returned

---

## 1️⃣3️⃣ Why OOP Is Important in Python 💡

- Models real-world problems naturally
- Enables reuse through inheritance
- Makes large systems manageable
- Foundation of frameworks (Django, Flask)

---

## 🧠 Mental Model to Lock In 🔒

```
Class   → blueprint
Object  → instance
self    → current object
__init__→ initialization
```

---

## ✅ End of Part 1

In the next part, we will cover:
- Encapsulation
- Access conventions (`_` and `__`)
- Properties
- Class variables vs instance variables

Nothing will be skipped.

---

✨ END — OOP IN PYTHON (PART 1)

