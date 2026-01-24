# Python Shell (REPL) – Zero to Advanced++ Notes

These notes explain **Python Shell / Interactive Mode** in extreme depth — from beginner concepts to **interview-grade internals**. This topic is very important for **Data Science, debugging, rapid experimentation, and interviews**.

---

## 1. What is Python Shell?

Python Shell is an **interactive execution environment** where Python code is:
- Executed **line by line**
- Evaluated immediately
- State (variables, functions) is **preserved in memory**

It is also called:
- REPL (Read → Evaluate → Print → Loop)
- Interactive Interpreter

---

## 2. How to Start Python Shell

### From Terminal

```bash
python
```
OR
```bash
python3
```

You will see:
```text
>>>
```
This is the **primary prompt**.

---

## 3. What Happens Internally in Shell?

Each line follows:

```
READ   → user types code
EVAL   → compile + execute
PRINT  → output
LOOP   → wait for next input
```

📌 Important:
- Code is **compiled to bytecode**
- Bytecode is executed by **PVM**
- Same internals as `.py` files

---

## 4. First Shell Examples

```python
>>> x = 10
>>> y = 20
>>> x + y
30
```

✔ Variables stay alive
✔ Memory is persistent until shell exits

---

## 5. Multi-line Statements in Shell

```python
>>> for i in range(3):
...     print(i)
...
0
1
2
```

- `...` indicates **continuation mode**
- Shell waits until block completes

---

## 6. Defining Functions in Shell

```python
>>> def add(a, b):
...     return a + b
...
>>> add(3, 4)
7
```

✔ Function exists in memory
✔ No file required

---

## 7. Importing Files into Python Shell

Assume file:

```python
# hello.py
x = 10

def greet():
    print("Hello")
```

### Import in Shell

```python
>>> import hello
>>> hello.x
10
>>> hello.greet()
Hello
```

📌 Important:
- `hello.py` becomes a **module object**
- Stored in memory

---

## 8. The BIG Question (Very Important)

### Scenario

1. You import `hello.py` in shell
2. You **modify hello.py** (add variables/functions)
3. Can shell access new changes?

### Answer: ❌ NO (by default)

---

## 9. Why Changes Are NOT Reflected Automatically

When you run:

```python
>>> import hello
```

Python:
- Loads module once
- Stores it in `sys.modules`
- Uses cached version

Even if file changes:
- Shell still refers to **old in-memory module**

---

## 10. Proof Example

### Step 1: Original File

```python
# hello.py
x = 10
```

### Step 2: Shell

```python
>>> import hello
>>> hello.x
10
```

### Step 3: Modify File (secretly 😄)

```python
# hello.py
x = 10
y = 99
```

### Step 4: Shell Again

```python
>>> hello.y
AttributeError
```

❌ New variable not visible

---

## 11. How to Load Changes? (reload)

### Solution 1: `importlib.reload`

```python
>>> import importlib
>>> import hello
>>> importlib.reload(hello)
>>> hello.y
99
```

✔ Reload recompiles file
✔ Updates module object

---

## 12. What Reload Actually Does

Internally:
- Reads file again
- Compiles to bytecode
- Executes top-level code
- Updates module namespace

📌 Old references may still exist

---

## 13. Dangerous Reload Case (Advanced)

```python
from hello import x
```

Even after reload:

```python
>>> importlib.reload(hello)
>>> x
10
```

❌ `x` does NOT update

Why?
- `x` was copied into local namespace

---

## 14. Correct Import Pattern for Shell Work

✔ Prefer:
```python
import hello
```

❌ Avoid:
```python
from hello import x
```

Especially for Data Science experiments

---

## 15. `sys.modules` (Interview Gold)

```python
>>> import sys
>>> sys.modules['hello']
<module 'hello'>
```

- Python keeps all imported modules here
- Reload updates this object

---

## 16. Running Files INSIDE Shell

```python
>>> exec(open("hello.py").read())
```

✔ Executes file in current namespace
❌ Not recommended for production

---

## 17. `__name__` in Shell

```python
>>> __name__
'__main__'
```

If imported:

```python
>>> import hello
>>> hello.__name__
'hello'
```

---

## 18. Shell vs Script Execution

| Feature | Shell | Script |
|------|------|------|
| Execution | Line-by-line | Full file |
| State | Persistent | Fresh run |
| Debugging | Excellent | Limited |
| Speed | Slower | Faster |

---

## 19. Advanced Shell Tools

### `dir()`
```python
>>> dir(hello)
```

### `help()`
```python
>>> help(hello)
```

### `_` (last result)
```python
>>> 5 + 5
10
>>> _ * 2
20
```

---

## 20. Shell Exit

```python
>>> exit()
```
OR
```python
>>> quit()
```

---

## 21. Common Interview Questions

### Q1. Does Python shell re-read file on import?
❌ No

### Q2. How to reflect file changes in shell?
✔ `importlib.reload`

### Q3. Why reload is risky?
✔ Old references remain

### Q4. Why shell is useful in Data Science?
✔ Fast experimentation

### Q5. Explain how Python shell handles imports and file changes.

“When a module is imported in the Python shell, it is loaded once and cached in sys.modules. Any subsequent changes to the source file are not reflected automatically because the shell keeps using the in-memory module object. To reflect changes, we must explicitly reload the module using importlib.reload, and even then, old references may remain.”

---

## 22. Mental Model

```
Shell = Live Python Memory
Import = Load once
Reload = Refresh module
Exit = Memory wipe
```

---

## 23. Real-Life Analogy

- Python file = Recipe 📄
- Import = Cook dish 🍲
- Modify recipe later ≠ dish updates
- Reload = Cook again 🔥

---

## 24. Final Takeaways

- Python shell is stateful
- Imports are cached
- Reload must be explicit
- Essential for debugging & DS

---

✅ End of Zero → Advanced++ Python Shell Notes

