# Python Language — Object Oriented Programming (OOP)
## Part 4: Polymorphism, Duck Typing & Operator Overloading

> **Goal of Part 4**
> - Understand **polymorphism** deeply (not just the definition)
> - Learn how Python achieves polymorphism **without interfaces**
> - Master **duck typing** and why it is central to Python design
> - Understand **operator overloading** using magic (dunder) methods
> - Visualize method calls, dispatch, and object behavior

This part explains **how different objects can respond to the same operation in different ways**.

---

## 1️⃣ What Is Polymorphism? 🧠

### Simple definition
> **Polymorphism** means *“many forms”* — the same operation behaves differently for different objects.

In Python:
- The **same method name**
- The **same operator**
- The **same function call**

can work with **different object types**.

---

## 2️⃣ Why Polymorphism Exists (REAL REASON) 💡

Polymorphism allows:
- Flexible code
- Loose coupling
- Easier extension

Instead of writing:
```python
if type(x) == Dog:
    x.bark()
elif type(x) == Cat:
    x.meow()
```

We write:
```python
x.speak()
```

And let the object decide **how** to respond.

---

## 3️⃣ Polymorphism via Method Overriding 🔁

```python
class Animal:
    def speak(self):
        print("Animal sound")

class Dog(Animal):
    def speak(self):
        print("Dog barks")

class Cat(Animal):
    def speak(self):
        print("Cat meows")
```

### Usage
```python
animals = [Dog(), Cat(), Animal()]

for a in animals:
    a.speak()
```

### Output
```
Dog barks
Cat meows
Animal sound
```

### Explanation
- Same method name: `speak`
- Different behavior depending on object

---

## 4️⃣ Runtime Method Dispatch (IMPORTANT) 🔍

When calling:
```python
a.speak()
```

Python decides at **runtime**:
1. Look at the object
2. Follow MRO
3. Call the first matching method

This is called **dynamic dispatch**.

---

## 5️⃣ Polymorphism WITHOUT Inheritance 🤯

This is where Python differs from Java/C++.

```python
class FileLogger:
    def write(self):
        print("Writing to file")

class SocketLogger:
    def write(self):
        print("Writing to socket")
```

```python
def log(writer):
    writer.write()
```

```python
log(FileLogger())
log(SocketLogger())
```

### Output
```
Writing to file
Writing to socket
```

No inheritance. Still polymorphism.

---

## 6️⃣ Duck Typing 🦆 (CORE PYTHON IDEA)

### Famous rule
> **“If it looks like a duck and quacks like a duck, it is a duck.”**

Meaning:
- Python does not care about the class
- Python cares about **behavior (methods)**

---

## 7️⃣ Duck Typing Example

```python
class Duck:
    def quack(self):
        print("Quack")

class Person:
    def quack(self):
        print("Person imitates duck")
```

```python
def make_quack(obj):
    obj.quack()
```

```python
make_quack(Duck())
make_quack(Person())
```

### Output
```
Quack
Person imitates duck
```

---

## 8️⃣ Why Duck Typing Is Powerful 💪

Advantages:
- No rigid inheritance trees
- Easy extension
- Works naturally with Python built-ins

Example:
```python
for x in [1, "hi", [1,2]]:
    print(len(x))
```

Each object implements `__len__()`.

---

## 9️⃣ Risks of Duck Typing ⚠️

Problem:
```python
make_quack(10)
```

Runtime error:
```
AttributeError: 'int' object has no attribute 'quack'
```

Python philosophy:
> **“Errors should happen at runtime, not be prevented by the language.”**

---

## 🔟 Operator Overloading 🧮

### Definition
> **Operator overloading** allows objects to define how operators behave.

Example:
```python
1 + 2
"a" + "b"
[1] + [2]
```

Same operator `+`, different behavior.

---

## 1️⃣1️⃣ How Operator Overloading Works Internally ⚙️

```python
a + b
```

Internally becomes:
```python
a.__add__(b)
```

---

## 1️⃣2️⃣ Custom Operator Overloading Example

```python
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)
```

```python
v1 = Vector(1, 2)
v2 = Vector(3, 4)
v3 = v1 + v2
```

### Output
```python
print(v3.x, v3.y)
```
```
4 6
```

---

## 1️⃣3️⃣ Common Operator Methods 📚

| Operator | Method |
|-------|--------|
| `+` | `__add__` |
| `-` | `__sub__` |
| `*` | `__mul__` |
| `/` | `__truediv__` |
| `==` | `__eq__` |
| `<` | `__lt__` |

---

## 1️⃣4️⃣ Comparison Overloading Example

```python
class Person:
    def __init__(self, age):
        self.age = age

    def __lt__(self, other):
        return self.age < other.age
```

```python
p1 = Person(20)
p2 = Person(30)
print(p1 < p2)
```

### Output
```
True
```

---

## 1️⃣5️⃣ Polymorphism + Operator Overloading 🔥

```python
items = [1, 2, 3]
print(sum(items))
```

Internally:
```
0 + 1 + 2 + 3
```

Uses `__add__()` repeatedly.

---

## 1️⃣6️⃣ When NOT to Overload Operators ❌

Avoid operator overloading when:
- Meaning is unclear
- Behavior is surprising
- Readability suffers

> Operator overloading should feel **natural**, not clever.

---

## 1️⃣7️⃣ Questions 🎯

### Q1. How does Python implement polymorphism?
**Answer:** Through dynamic typing and dynamic method dispatch.

### Q2. Is inheritance required for polymorphism?
**Answer:** No. Duck typing enables polymorphism without inheritance.

### Q3. What is duck typing?
**Answer:** Behavior-based typing instead of class-based typing.

### Q4. How does `+` work for custom objects?
**Answer:** Via `__add__()` magic method.

---

## 🧠 Final Mental Model (LOCK THIS)

```
Same call → different behavior
Method name → resolved at runtime
Operators → mapped to dunder methods
Duck typing → behavior > type
```

---

## ✅ End of Part 4

Next Part:
**Part 5 — Advanced OOP: Dunder Methods, Composition, Abstraction & Design Principles**

This will complete OOP in Python.

---

✨ END — OOP IN PYTHON (PART 4)

