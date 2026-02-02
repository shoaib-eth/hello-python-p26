# Python OOP — Interview Questions (Deep, Tricky & Conceptual)

> **Purpose of this document**
> - Prepare you for **real Python OOP interviews** (not beginner questions)
> - Focus on **WHY**, **HOW**, and **INTERNAL BEHAVIOR**
> - Cover questions interviewers ask to test **depth**, not syntax

Each question includes:
- What the interviewer is testing
- A **clear, correct answer**
- Extra internal insight where required

---

## 1️⃣ What is Object Oriented Programming?

### Interviewer wants to test
Whether you understand OOP as a **design philosophy**, not just syntax.

### Answer
Object Oriented Programming is a way of designing software where **data and behavior are bundled together into objects**, making code easier to reason about, extend, and maintain.

OOP models real-world entities and relationships using classes and objects.

---

## 2️⃣ Why do we need OOP when functions already exist?

### What is being tested
Design thinking and scalability understanding.

### Answer
Functions alone work for small programs, but as systems grow:
- Data becomes scattered
- Changes cause ripple effects
- Code becomes hard to maintain

OOP solves this by **grouping related data and behavior**, improving modularity and long-term maintainability.

---

## 3️⃣ What is the difference between a class and an object?

### Answer
- A **class** is a blueprint or template
- An **object** is an instance created from that blueprint

A class defines structure; objects hold actual data.

---

## 4️⃣ What is `self` and why is it required?

### Interviewer trap
Many candidates say “self is a keyword” (wrong).

### Correct answer
`self` is a **reference to the current object**. It allows methods to:
- Access instance attributes
- Distinguish between object-level data

Python passes the object automatically as the first argument during method calls.

---

## 5️⃣ What happens in memory when an object is created?

### Strong answer
1. Class is already loaded in memory
2. `__new__()` allocates memory for the object
3. `__init__()` initializes the object
4. Reference to the object is returned

`__new__` creates, `__init__` configures.

---

## 6️⃣ Difference between instance variables and class variables?

### Answer
- Instance variables belong to individual objects
- Class variables are shared across all instances

Python first checks the instance namespace, then the class namespace.

---

## 7️⃣ Does Python support private variables?

### Correct answer
No. Python does not enforce true private variables.

Double underscore (`__var`) triggers **name mangling**, not privacy. It exists to avoid accidental overrides, not to provide security.

---

## 8️⃣ What is name mangling and why does Python use it?

### Answer
Name mangling rewrites `__var` to `_ClassName__var` internally.

It prevents accidental access and name clashes in subclasses.

---

## 9️⃣ What is inheritance and when should it be avoided?

### Answer
Inheritance allows a child class to reuse and extend behavior of a parent class.

It should be avoided when the relationship is **HAS-A** instead of **IS-A**.

In such cases, **composition** is preferred.

---

## 🔟 What is `super()` and how does it work internally?

### Tricky part
Many candidates think `super()` means parent class.

### Correct answer
`super()` returns a proxy that follows the **Method Resolution Order (MRO)**.

It calls the **next method in the MRO**, not necessarily the immediate parent.

---

## 1️⃣1️⃣ What is MRO and why is it needed?

### Answer
MRO defines the order in which Python searches classes for methods.

It is required to:
- Support multiple inheritance
- Avoid ambiguity
- Ensure consistent method lookup

Python uses **C3 Linearization**.

---

## 1️⃣2️⃣ Explain the Diamond Problem

### Answer
The Diamond Problem occurs when a class inherits from two classes that share a common ancestor.

Python resolves this using MRO, ensuring each class is visited only once.

---

## 1️⃣3️⃣ What is polymorphism in Python?

### Answer
Polymorphism allows the same method call or operator to behave differently depending on the object.

Python achieves this through **dynamic typing and runtime dispatch**, not interfaces.

---

## 1️⃣4️⃣ What is duck typing?

### Interview-level answer
Duck typing focuses on **behavior rather than type**.

If an object implements the required methods, it is acceptable regardless of its class.

---

## 1️⃣5️⃣ Is inheritance required for polymorphism?

### Answer
No.

Duck typing enables polymorphism without inheritance.

---

## 1️⃣6️⃣ How does operator overloading work in Python?

### Answer
Operators are mapped to **dunder methods**.

Example:
- `a + b` → `a.__add__(b)`

Custom behavior can be implemented by defining these methods.

---

## 1️⃣7️⃣ Difference between `__str__` and `__repr__`?

### Answer
- `__str__` → user-friendly representation
- `__repr__` → developer/debug representation

`__repr__` should ideally recreate the object.

---

## 1️⃣8️⃣ What is abstraction in Python?

### Answer
Abstraction exposes **what an object does**, not **how it does it**.

Python uses **Abstract Base Classes (ABC)** to enforce method contracts.

---

## 1️⃣9️⃣ Why is `global` discouraged in OOP?

### Answer
Because it:
- Introduces hidden dependencies
- Breaks encapsulation
- Makes testing and debugging harder

OOP prefers **encapsulation and controlled access**.

---

## 2️⃣0️⃣ What is composition and why is it preferred over inheritance?

### Strong answer
Composition builds behavior by combining objects rather than inheriting them.

It reduces coupling, improves flexibility, and avoids deep inheritance chains.

---

## 🧠 Final Interview Master Summary

```
Classes define structure
Objects hold state
Encapsulation protects data
Inheritance reuses behavior
Polymorphism enables flexibility
Composition improves design
```

---

## ✅ How to Use This Document

- Read answers aloud
- Focus on WHY, not just WHAT
- Practice explaining without code

If you can explain these clearly, you are **interview-ready for Python OOP**.

---

✨ END — PYTHON OOP INTERVIEW QUESTIONS

