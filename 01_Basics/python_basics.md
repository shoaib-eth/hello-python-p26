# Python Basics Notes: Modules, Functions & __pycache__

These notes explain the behavior of the following two Python files and the automatically created `__pycache__` folder.

---

## 1. File: `hello.py`

```python
print("Hello 👋 Python Learners ")

def Namaste(n):
    print(n)

Namaste("Hello 👋")
Namaste(10)
```

### 1.1 What happens line by line?

#### 🔹 `print("Hello 👋 Python Learners ")`
- This line executes **immediately** when the file runs.
- It prints a greeting message to the console.

---

#### 🔹 `def Namaste(n):`
- This defines a **function** named `Namaste`.
- `n` is a **parameter** (input value).

```python
print(n)
```
- Prints whatever value is passed to the function.

📌 Important:
- Python functions are **dynamically typed**.
- `n` can be a string, number, list, etc.

---

#### 🔹 Function Calls

```python
Namaste("Hello 👋")
Namaste(10)
```

- First call passes a string
- Second call passes an integer

✔ Both work because Python does not restrict parameter types.

### Output of `hello.py`

```
Hello 👋 Python Learnners
Hello 👋
10
```

---

## 2. File: `Namaste.py`

```python
from hello import Namaste;

Namaste("Hello 👋 Python Learners!")
```

### 2.1 What is happening here?

#### 🔹 `from hello import Namaste`
- Imports the **Namaste function** from `hello.py`
- `hello.py` is treated as a **module**

📌 Python rule:
- Any `.py` file can act as a module
- File name = module name

---

#### 🔹 Function Call

```python
Namaste("Hello 👋 Python Learners!")
```
- Calls the imported function
- Prints the passed string

### Output of `Namaste.py`

```
Hello 👋 Python Learnners 
Hello 👋
10
Hello 👋 Python Learners!
```

⚠ Why is the first line printed?
- Because when `hello.py` is imported, **all top-level code runs**

---

## 3. Why did `__pycache__` folder get created?

### 3.1 What is `__pycache__`?

`__pycache__` is a folder where Python stores **compiled bytecode files**.

Example file:
```
hello.cpython-314.pyc
```

---

### 3.2 Why Python creates it?

When you run or import a Python file:
1. Python converts `.py` → **bytecode** (`.pyc`)
2. Bytecode runs faster than source code
3. Stored inside `__pycache__` for reuse

✔ This improves performance
✔ Next run is faster

---

### 3.3 Is `__pycache__` important?

- ❌ Not required to keep
- ❌ Should NOT be committed to Git
- ✔ Can be safely deleted

Recommended `.gitignore` entry:

```
__pycache__/
*.pyc
```

---

## 4. Best Practice: Prevent unwanted execution on import

### Problem

Currently, this code runs automatically when imported:

```python
print("Hello 👋 Python Learnners ")
Namaste("Hello 👋")
Namaste(10)
```

---

### Solution: `if __name__ == "__main__"`

### Improved `hello.py`

```python
def Namaste(n):
    print(n)

if __name__ == "__main__":
    print("Hello 👋 Python Learnners")
    Namaste("Hello 👋")
    Namaste(10)
```

✔ Code runs only when file is executed directly
✔ Code does NOT run when imported

---

## 5. Key Concepts Summary

| Concept | Meaning |
|------|--------|
| Function | Reusable block of code |
| Module | A Python file used for imports |
| Import | Using code from another file |
| `__pycache__` | Bytecode cache folder |
| `.pyc` | Compiled Python file |
| `__main__` | Entry-point protection |

---

## 6. Real-World Analogy

- `hello.py` → A toolbox 🧰
- `Namaste()` → A tool inside it 🔧
- `Namaste.py` → Someone borrowing that tool 👷
- `__pycache__` → Pre-assembled tools for faster work ⚡

---

## 7. Data Science Relevance

These concepts are **core foundations** for:
- Writing reusable ML utilities
- Importing NumPy / Pandas modules
- Building pipelines & notebooks

Mastering this = smooth Data Science journey 🚀

---

✅ End of Notes

