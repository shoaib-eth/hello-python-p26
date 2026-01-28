# Python Internal Working – Notes

These notes explain **how Python works internally**, from source code execution to bytecode and the Python Virtual Machine (PVM). These concepts are **frequently asked in interviews**, especially by **Big Tech & data-driven companies**.

---

## 1. High-Level Execution Flow (Big Picture)

```
hello.py (Source Code)
        │
        ▼
Python Compiler (Implicit)
        │
        ▼
Bytecode (.pyc)
        │
        ▼
Python Virtual Machine (PVM)
        │
        ▼
Actual Execution (CPU via interpreter loop)
```

📌 Important:
- Python is **NOT a pure interpreter**
- Python is **bytecode-interpreted** language

---

## 2. Step-by-Step Internal Execution

### Step 1: Python Source Code (`.py`)

Example:
```python
print("Hello")
```

- This is **human-readable code**
- Platform independent
- Cannot be executed directly by CPU

---

### Step 2: Compilation to Bytecode

When Python runs a file:
- It **first compiles** source code
- Generates **bytecode** (low-level instructions)

📌 Bytecode Characteristics:
- Platform independent
- Python-version dependent
- Stored in memory OR on disk

Example bytecode instruction:
```
LOAD_CONST
CALL_FUNCTION
PRINT_ITEM
```

---

## 3. Bytecode & `__pycache__`

### What is Bytecode?

- Bytecode is **NOT machine code** ❌
- It is **instruction set for PVM**
- Acts as an intermediate representation

---

### What is `__pycache__`?

- Directory where Python stores compiled bytecode
- Contains `.pyc` files

Example:
```
__pycache__/
  hello.cpython-312.pyc
```

Meaning:
- `cpython` → Python implementation
- `312` → Python version

---

### When is `.pyc` created?

✔ Only when:
- A file is **imported**

❌ Not created when:
- File is run directly as top-level script

📌 Interview Favorite Question
> Why doesn’t Python create `.pyc` for main files?

Answer:
- Main files are executed once
- Caching provides no performance benefit

---

## 4. Bytecode Caching Logic

Python checks:
1. Source file timestamp
2. Python version

If **source changes OR version changes**:
- Bytecode is regenerated

---

## 5. Python Virtual Machine (PVM)

### What is PVM?

- Runtime engine of Python
- Executes bytecode **instruction by instruction**
- Also called **Python Interpreter Loop**

---

### Responsibilities of PVM

- Reads bytecode
- Manages stack
- Handles memory allocation
- Performs garbage collection
- Executes control flow (loops, conditions)

---

### PVM is NOT

❌ Hardware VM
❌ OS-level virtualization
❌ Machine code executor

✔ It is a **software-based execution engine**

---

## 6. Interpreter Loop (Very Important)

Internally, PVM runs something like:

```
while True:
    instruction = fetch_bytecode()
    execute(instruction)
```

This loop:
- Runs continuously
- Decodes one instruction at a time
- Executes via C code (in CPython)

📌 This is why Python is slower than C

---

## 7. Python Implementations (Interview Gold)

### 1. CPython

- Default Python
- Written in C
- Uses GIL
- Bytecode → PVM

---

### 2. Jython

- Runs on JVM
- Bytecode → Java Bytecode
- No GIL

---

### 3. IronPython

- Runs on .NET CLR
- Integrates with C#

---

### 4. PyPy

- Uses JIT compiler
- Faster for long-running programs
- Different memory model

---

### 5. Stackless Python

- No C stack
- Lightweight task switching
- Microthreads

---

## 8. Why Bytecode is Faster Than Source Code

Reasons:
- Parsing done once
- Syntax analysis skipped
- Cached instructions reused

📌 Still slower than native machine code

---

## 9. Why Bytecode is Platform Independent

- Bytecode is interpreted by PVM
- PVM is platform-specific
- Same bytecode works everywhere

Analogy:
- Bytecode = English instructions
- PVM = Translator
- CPU = Listener

---

## 10. Why Python is Called an Interpreted Language

Technically:
- Python is **compiled + interpreted**

But called interpreted because:
- No explicit compile step
- Execution happens at runtime

---

## 11. Data Science Relevance

Understanding internals helps with:
- Performance optimization
- Memory-efficient code
- Choosing CPython vs PyPy
- Debugging slow pipelines

---

## 12. Common Interview Questions & Hints

### Q1. Is Python compiled or interpreted?
✔ Both

### Q2. What is PVM?
✔ Runtime engine executing bytecode

### Q3. Why `.pyc` is version dependent?
✔ Bytecode format changes per version

### Q4. Why Python is slower than C?
✔ Interpreter loop + dynamic typing

### Q5. Explain Python execution internally”

Start like this 👇

“When I run a Python program, the source code is first compiled into bytecode. This bytecode is then executed by the Python Virtual Machine, which is essentially a runtime interpreter loop written in C (in CPython). Bytecode is cached inside __pycache__ for imported modules to optimize performance.”
---

---

## 13. Final Mental Model

```
You write Python
Python compiles to bytecode
PVM interprets bytecode
CPU executes via C-runtime
```

---

✅ These notes cover **interview-level depth** and **real internal mechanics**

End of Notes

