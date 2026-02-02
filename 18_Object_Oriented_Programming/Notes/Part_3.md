# Python Language — Object Oriented Programming (OOP)
## Part 3: Inheritance, `super()`, Method Overriding & MRO

> **Goal of Part 3**
> - Understand **inheritance** deeply (why it exists, not just how)
> - Learn how Python resolves methods using **MRO (Method Resolution Order)**
> - Understand `super()` correctly (most misunderstood concept)
> - Master **method overriding** and common pitfalls
> - Visualize memory, lookup flow, and execution order

---

## 1️⃣ What Is Inheritance? 🧬

### Definition
> **Inheritance** allows a class (child) to reuse and extend the behavior of another class (parent).

In simple terms:
```
Child IS-A Parent
```

Example:
```
Car IS-A Vehicle
Dog IS-A Animal
```

---

## 2️⃣ Why Inheritance Exists (REAL REASON) 🧠

Inheritance exists to:
- Avoid code duplication
- Represent real-world hierarchies
- Enable polymorphism

Without inheritance:
- Same logic repeated in multiple classes
- Harder maintenance

---

## 3️⃣ Basic Inheritance Syntax 🧩

```python
class Animal:
    def speak(self):
        print("Animal makes a sound")

class Dog(Animal):
    pass
```

### Usage
```python
d = Dog()
d.speak()
```

### Output
```
Animal makes a sound
```

### Explanation
- `Dog` inherits from `Animal`
- `Dog` does not define `speak`
- Python looks up `speak` in parent

---

## 4️⃣ Memory & Attribute Lookup Visualization 🔍

When calling:
```python
d.speak()
```

Lookup order:
```
1. Dog instance
2. Dog class
3. Animal class
4. object class
```

This lookup order is controlled by **MRO**.

---

## 5️⃣ Method Overriding 🔁

### Definition
> **Method overriding** means redefining a parent method in the child class.

```python
class Animal:
    def speak(self):
        print("Animal sound")

class Dog(Animal):
    def speak(self):
        print("Dog barks")
```

### Usage
```python
d = Dog()
d.speak()
```

### Output
```
Dog barks
```

### Explanation
- Child method replaces parent method
- Parent method is hidden (not deleted)

---

## 6️⃣ Calling Parent Method Without `super()` ❌

```python
class Dog(Animal):
    def speak(self):
        Animal.speak(self)
        print("Dog barks")
```

### Why this is discouraged
- Breaks multiple inheritance
- Hardcodes parent class name

---

## 7️⃣ `super()` — The RIGHT Way ✅

### What `super()` Does
> `super()` returns a **proxy object** that follows MRO.

```python
class Dog(Animal):
    def speak(self):
        super().speak()
        print("Dog barks")
```

### Output
```
Animal sound
Dog barks
```

---

## 8️⃣ `super()` Is NOT “Parent” (IMPORTANT) ⚠️

> `super()` does **NOT** mean “call parent class”.

It means:
> “Call the **next class in MRO**.”

This distinction matters in multiple inheritance.

---

## 9️⃣ Multiple Inheritance 🧩

```python
class A:
    def show(self):
        print("A")

class B:
    def show(self):
        print("B")

class C(A, B):
    pass
```

```python
c = C()
c.show()
```

### Output
```
A
```

Why?
- Python follows MRO
- `A` comes before `B`

---

## 🔟 Method Resolution Order (MRO) 🧠

### What is MRO?
> **MRO defines the exact order in which Python searches classes for methods.**

```python
print(C.__mro__)
```

Output:
```
(C, A, B, object)
```

---

## 1️⃣1️⃣ Diamond Problem (Classic Interview Topic) 💎

```python
class A:
    def show(self):
        print("A")

class B(A):
    def show(self):
        print("B")

class C(A):
    def show(self):
        print("C")

class D(B, C):
    pass
```

```python
d = D()
d.show()
```

### Output
```
B
```

### Why?
```python
print(D.__mro__)
```

```
(D, B, C, A, object)
```

---

## 1️⃣2️⃣ `super()` with Multiple Inheritance 🔥

```python
class A:
    def show(self):
        print("A")n
class B(A):
    def show(self):
        super().show()
        print("B")

class C(A):
    def show(self):
        super().show()
        print("C")

class D(B, C):
    def show(self):
        super().show()
        print("D")
```

Calling:
```python
d = D()
d.show()
```

### Execution order
```
A
C
B
D
```

This works **only because of MRO**.

---

## 1️⃣3️⃣ Why MRO Uses C3 Linearization 🧮

Python uses **C3 Linearization** to:
- Preserve inheritance order
- Avoid ambiguity
- Ensure consistency

You are NOT expected to implement it, but must understand its effect.

---

## 1️⃣4️⃣ `isinstance()` and `issubclass()` 🔍

```python
isinstance(d, Dog)      # True
isinstance(d, Animal)   # True

issubclass(Dog, Animal) # True
```

Used for runtime type checks.

---

## 1️⃣5️⃣ When NOT to Use Inheritance ❌

Avoid inheritance when:
- Relationship is HAS-A, not IS-A
- You only want code reuse

Prefer **composition** instead.

---

## 🧠 Final Mental Model (LOCK THIS)

```
Inheritance → reuse + polymorphism
Override    → replace behavior
super()     → next in MRO
MRO         → method lookup order
```

---

## ✅ End of Part 3

Next Part:
**Part 4 — Polymorphism, Duck Typing & Operator Overloading**

This will complete the behavioral side of OOP.

---

✨ END — OOP IN PYTHON (PART 3)

