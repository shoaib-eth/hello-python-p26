# Python Language — Object Oriented Programming
## 10 Core OOP Problems with Deep, Line‑by‑Line Explanation

> **Purpose of these notes**
> - Convert OOP *practice problems* into **conceptual mastery**
> - Explain **every line**, not just what it does but *why it exists*

These 10 problems together cover **almost the entire Python OOP syllabus**.

---

## 1️⃣ Basic Class and Object

### Code
```python
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

my_car = Car("Toyota", "Fortuner")
print(my_car.brand)
print(my_car.model)
```

### Line‑by‑Line Explanation

```python
class Car:
```
- Defines a **class blueprint** named `Car`
- No memory is allocated for objects yet

```python
def __init__(self, brand, model):
```
- `__init__` is a **constructor**
- Runs automatically when an object is created
- `self` → reference to the current object

```python
self.brand = brand
self.model = model
```
- Creates **instance variables**
- Stored inside the object’s memory

```python
my_car = Car("Toyota", "Fortuner")
```
- Creates an object
- Memory allocated → `__init__` called

```python
print(my_car.brand)
```
- Attribute lookup → object namespace

### Output
```
Toyota
Fortuner
```

---

## 2️⃣ Instance Method and `self`

### Code
```python
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def full_name(self):
        return f"{self.brand} {self.model}"

my_car = Car("Toyota", "Fortuner")
print(my_car.full_name())
```

### Key Concept
- Instance methods **always receive the object as `self`**

```python
my_car.full_name()
```
Internally becomes:
```python
Car.full_name(my_car)
```

### Output
```
Toyota Fortuner
```

---

## 3️⃣ Inheritance (IS‑A relationship)

### Code
```python
class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size
```

### Explanation

```python
class ElectricCar(Car):
```
- `ElectricCar IS‑A Car`
- Inherits all public behavior of `Car`

```python
super().__init__(brand, model)
```
- Calls parent constructor
- Ensures parent attributes are initialized

### Usage
```python
my_tesla = ElectricCar("Tesla", "Model S", "85KWH")
print(my_tesla.full_name())
```

### Output
```
Tesla Model S
```

---

## 4️⃣ Encapsulation (Private Attributes)

### Code
```python
class Car:
    def __init__(self, brand, model):
        self.__brand = brand
        self.model = model

    def get_brand(self):
        return self.__brand
```

### What `__brand` really means
- Python performs **name mangling**
- `__brand` → `_Car__brand`

```python
print(my_car.get_brand())
```

### Why Encapsulation?
- Protect internal state
- Prevent accidental modification
- Control access through methods

---

## 5️⃣ Polymorphism (Method Overriding)

### Code
```python
class Car:
    def fuel_type(self):
        return "Petrol or Diesel"

class ElectricCar(Car):
    def fuel_type(self):
        return "Electric Charge"
```

### Explanation
- Same method name
- Different behavior
- Decided **at runtime**

```python
vehicle.fuel_type()
```
→ Python checks object type, not reference type

---

## 6️⃣ Class Variables

### Code
```python
class Car:
    total_car = 0

    def __init__(self, brand, model):
        Car.total_car += 1
```

### Explanation
- `total_car` belongs to **class**, not objects
- Shared across all instances

```python
print(Car.total_car)
```

### Output
```
2
```

---

## 7️⃣ Static Methods

### Code
```python
@staticmethod
def general_description():
    return "Cars are means of transport"
```

### Key Idea
- No `self`
- No `cls`
- Logically related utility

```python
Car.general_description()
my_car.general_description()
```
Both are valid.

---

## 8️⃣ Property Decorators (Read‑Only Attribute)

### Code
```python
@property
def model(self):
    return self.__model
```

### Explanation
- Allows attribute‑like access
- Prevents modification

```python
print(my_car.model)
# my_car.model = "X" → ERROR
```

---

## 9️⃣ `isinstance()`

### Code
```python
print(isinstance(my_tesla, Car))
print(isinstance(my_tesla, ElectricCar))
```

### Explanation
- Checks **inheritance chain**
- Used heavily in runtime validation

### Output
```
True
True
```

---

## 🔟 Multiple Inheritance

### Code
```python
class Battery:
    def battery_info(self):
        return "Battery system"

class Engine:
    def engine_info(self):
        return "Engine system"

class ElectricCarTwo(Battery, Engine, Car):
    pass
```

### Explanation
- Class inherits from multiple parents
- Python resolves method calls using **MRO**

```python
print(ElectricCarTwo.__mro__)
```

### Output
```
(ElectricCarTwo, Battery, Engine, Car, object)
```

---

## 🧠 Final Master Mental Model

```
Class → blueprint
Object → real instance
Encapsulation → data safety
Inheritance → reuse
Polymorphism → flexibility
Static → utility
Property → controlled access
MRO → method lookup
```

---

## ✅ Interview Readiness Check

If you can explain:
- WHY `super()` is needed
- HOW attribute lookup works
- WHEN to use static vs instance methods
- WHY composition is often better

👉 You are **strong in Python OOP**.

---

✨ END — Python OOP Practice (10 Problems)

