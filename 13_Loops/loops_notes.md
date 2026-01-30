# Python Loops – `for` & `while` 

These notes explain **loops in Python** at a **deep, engineering level**.

You will learn:
- WHY loops exist 🤔
- Difference between `if`, `for`, `while` 🧠
- How `for` and `while` actually work internally ⚙️
- Every loop keyword (`break`, `continue`, `pass`, `else`) 🔥
- Real‑world & Data Science use‑cases 📊
- Code + OUTPUT for every concept 💻
- Interview questions & traps 🎯

---

## 1️⃣ Why Do Loops Exist? (VERY IMPORTANT) 🤔

Without loops, computers would be **useless** for real work.

### 🧠 Core Idea
> **Loops exist to repeat logic automatically.**

### 🌍 Real‑life analogy
- Washing 10 plates 🍽️
- Checking attendance of 60 students 👨‍🎓
- Processing 1 million rows of data 📊

Without loops → copy‑paste same code again & again ❌

---

## 2️⃣ `if` vs `for` vs `while` (FOUNDATION CLARITY) 🧠🔥

| Statement | Purpose | Repetition? |
|--------|--------|-------------|
| `if` | Decision | ❌ No |
| `for` | Iteration over sequence | ✅ Yes |
| `while` | Loop until condition fails | ✅ Yes |

### 🔑 One‑line definitions

- `if` → **decide once**
- `for` → **repeat for each item**
- `while` → **repeat while condition is true**

---

## 3️⃣ `for` Loop – Deep Concept 🧠

### 🔹 What `for` REALLY means in Python

> **`for` loop iterates over an iterable, not numbers directly.**

```python
for x in [1, 2, 3]:
    print(x)
```

**Output:**
```
1
2
3
```

🧠 Internally:
```
Get iterator → get next item → run block → repeat
```

---

## 4️⃣ Common Iterables Used with `for` 🔁

### List
```python
for x in [10, 20, 30]:
    print(x)
```

**Output:**
```
10
20
30
```

---

### String
```python
for ch in "hi":
    print(ch)
```

**Output:**
```
h
i
```

---

### Tuple
```python
for x in (1, 2):
    print(x)
```

**Output:**
```
1
2
```

---

### Dictionary
```python
d = {'a': 1, 'b': 2}
for k in d:
    print(k, d[k])
```

**Output:**
```
a 1
b 2
```

---

## 5️⃣ `range()` – Backbone of Loops ⚙️

```python
for i in range(5):
    print(i)
```

**Output:**
```
0
1
2
3
4
```

🧠 `range()` is:
- Memory efficient
- Lazy (does not create list)

---

## 6️⃣ Nested `for` Loops 🔁🔁

```python
for i in range(2):
    for j in range(3):
        print(i, j)
```

**Output:**
```
0 0
0 1
0 2
1 0
1 1
1 2
```

🧠 Inner loop runs **fully** for each outer loop iteration.

---

## 7️⃣ `while` Loop – Deep Concept 🧠🔥

### 🔹 What `while` REALLY means

> **Repeat until condition becomes false.**

```python
x = 3
while x > 0:
    print(x)
    x -= 1
```

**Output:**
```
3
2
1
```

🧠 Loop condition checked **before every iteration**.

---

## 8️⃣ Infinite Loops ⚠️

```python
while True:
    print("Running")
```

🧠 Used in:
- Servers
- Games
- Event listeners

⚠️ Must have `break` to stop.

---

## 9️⃣ Loop Control Keywords 🔥

### `break` – stop loop immediately
```python
for i in range(5):
    if i == 3:
        break
    print(i)
```

**Output:**
```
0
1
2
```

---

### `continue` – skip current iteration
```python
for i in range(5):
    if i == 2:
        continue
    print(i)
```

**Output:**
```
0
1
3
4
```

---

### `pass` – do nothing (placeholder)
```python
for i in range(3):
    pass
print("Done")
```

**Output:**
```
Done
```

---

## 🔟 `else` with Loops (INTERVIEW FAVORITE 🎯)

```python
for i in range(3):
    print(i)
else:
    print("Loop completed")
```

**Output:**
```
0
1
2
Loop completed
```

⚠️ `else` runs **only if loop didn’t break**.

---

## 1️⃣1️⃣ `while` vs `for` (WHEN TO USE WHAT) 🧠

| Situation | Use |
|--------|----|
| Known number of iterations | `for` |
| Unknown stopping point | `while` |
| Iterating data | `for` |
| Waiting / polling | `while` |

---

## 1️⃣2️⃣ Common Bugs & Traps ❌

- Forgetting to update condition in `while`
- Infinite loops
- Modifying list while looping

---

## 1️⃣3️⃣ Loops in Data Science 📊

- Cleaning datasets
- Feature extraction
- Batch processing

```python
for value in data:
    clean(value)
```

⚠️ In DS, prefer **vectorized ops** over loops when possible.

---

## 🎯 Questions & Answers

### Q1. Difference between `for` and `while`?
**Ans:** `for` iterates over sequence, `while` depends on condition.

### Q2. What happens if condition never becomes false?
**Ans:** Infinite loop.

### Q3. When does loop `else` execute?
**Ans:** When loop completes without `break`.

### Q4. Is `for` faster than `while`?
**Ans:** Usually yes, due to iterator optimizations.

---

## 🧠 Final Mental Model (MUST REMEMBER)

```
if     → Decide once
for    → Iterate items
while  → Repeat until stop
```

---

## ✅ Final Takeaway

> **Loops are controlled repetition. Master loops, and you master automation.** 🔥

---

🔥 END – PYTHON LOOPS NOTES

