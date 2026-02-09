# Python Language — ERROR HANDLING

## Error Handling in Python 

> **Why this topic is CRITICAL**
>
> Error handling is NOT about avoiding crashes.
>
> It is about:
>
> - writing **robust** programs
> - handling **unexpected situations** gracefully
> - protecting **user experience & data**
>


---

## 1️⃣ What Is an Error? (First Principles)

An **error** is a situation where Python **cannot continue normal execution**.

There are **two broad categories**:

1. **Syntax Errors** ❌ (Python can’t even start)
2. **Runtime Errors / Exceptions** ⚠️ (Program starts, but fails later)

---

## 2️⃣ Syntax Error ❌ (Compile-Time)

Example:

```python
if True
    print("Hello")
```

Output:

```
SyntaxError: invalid syntax
```

🔴 Program **never runs**.

➡️ Syntax errors **cannot be caught** using try-except.

---

## 3️⃣ Runtime Errors (Exceptions) ⚠️

These occur **while program is running**.

Examples:

```python
print(10 / 0)
```

Output:

```
ZeroDivisionError: division by zero
```

```python
lst = [1, 2]
print(lst[5])
```

Output:

```
IndexError: list index out of range
```

---

## 4️⃣ What Is an Exception? 🧠

An **exception** is:

> A special Python object that signals an error condition.

When an exception occurs:

```
Normal flow ❌
Stack unwinding starts
Program crashes (if unhandled)
```

---

## 5️⃣ try-except (Core of Error Handling)

### Basic Structure

```python
try:
    risky_code
except ErrorType:
    recovery_code
```

Example:

```python
try:
    x = int("abc")
except ValueError:
    print("Conversion failed")
```

Output:

```
Conversion failed
```

---

## 6️⃣ Execution Flow Visualization 🧭

```
try block
   ↓
Error occurs?
   ↓ yes → except block executes
   ↓ no  → except skipped
```

Only **one except** runs.

---

## 7️⃣ Catching Multiple Exceptions 🎯

```python
try:
    num = int(input("Enter number: "))
    print(10 / num)
except ValueError:
    print("Invalid number")
except ZeroDivisionError:
    print("Cannot divide by zero")
```

---

## 8️⃣ Catching Multiple Errors Together

```python
except (ValueError, ZeroDivisionError):
    print("Something went wrong")
```

Useful when handling logic is same.

---

## 9️⃣ The `else` Block ✅

Runs **only if no exception occurred**.

```python
try:
    x = int("10")
except ValueError:
    print("Error")
else:
    print("Success", x)
```

Output:

```
Success 10
```

---

## 🔟 The `finally` Block 🧹

Runs **ALWAYS**, whether exception occurs or not.

```python
try:
    f = open("file.txt")
except FileNotFoundError:
    print("File missing")
finally:
    print("Cleanup done")
```

Used for:

- closing files
- releasing resources

---

## 1️⃣1️⃣ Why finally Is Important (Interview Favorite)

Because **resources must be released even on failure**.

```
try → error → finally still runs
```

---

## 1️⃣2️⃣ Common Built-in Exceptions 🧨

| Exception         | When it occurs    |
| ----------------- | ----------------- |
| ValueError        | Wrong value type  |
| TypeError         | Invalid operation |
| IndexError        | Invalid index     |
| KeyError          | Missing dict key  |
| ZeroDivisionError | Divide by zero    |
| FileNotFoundError | File missing      |

---

## 1️⃣3️⃣ Using `Exception` (Catch-All) ⚠️

```python
try:
    risky()
except Exception as e:
    print(e)
```

⚠️ Use carefully.

Bad practice:

- swallowing errors
- hiding bugs

---

## 1️⃣4️⃣ Raising Exceptions Manually 🚨

```python
age = -5
if age < 0:
    raise ValueError("Age cannot be negative")
```

Output:

```
ValueError: Age cannot be negative
```

Used for:

- enforcing rules
- validating inputs

---

## 1️⃣5️⃣ Custom Exceptions 🧩

```python
class InvalidAgeError(Exception):
    pass

raise InvalidAgeError("Invalid age")
```

Used in **large systems** for clarity.

---

## 1️⃣6️⃣ Exception Hierarchy 🌳 (VERY IMPORTANT)

```
BaseException
 ├── Exception
 │     ├── ValueError
 │     ├── TypeError
 │     ├── IndexError
 └── SystemExit
```

Catching parent catches children.

---

## 1️⃣7️⃣ Anti-Patterns ❌

❌ Bare except:

```python
except:
    pass
```

❌ Hiding real bugs ❌ Making debugging impossible

---

## 1️⃣8️⃣ Error Handling vs Validation ⚖️

- Validation → Prevent errors
- Error handling → Recover from errors

Good code uses **both**.

---

## 1️⃣9️⃣ Error Handling in Real Projects 🏗️

Used in:

- APIs
- Databases
- File systems
- User input handling

Example:

```python
try:
    data = fetch_from_api()
except TimeoutError:
    retry()
```

---

## 2️⃣0️⃣ Interview GOLD 🎯

### Q1. Difference between error and exception?

Error crashes program; exception can be handled.

---

### Q2. Why finally is important?

To release resources safely.

---

### Q3. Should we use bare except?

No, it hides bugs and is bad practice.

---

## 🧠 FINAL MENTAL MODEL (LOCK THIS)

```
Error occurs
 → Exception object created
 → Stack unwinds
 → except handles (if present)
 → finally cleans up
```

✨ END — Python Error Handling

