# Python Loops – 10 Real‑World Problems 

⚠️ **Important:**
These notes are intentionally **LONG, DETAILED, and SLOW**.

Goal:
- Understand **HOW loops think internally** 🧠
- Understand **WHY each line exists**
- See **what would break if logic/order changed**

---

## 🔰 Core Reminder: How Loops Execute Internally

### `for` loop internal model
```
Get iterable
↓
Fetch next item
↓
Assign to loop variable
↓
Execute body
↓
Repeat until iterable ends
```

### `while` loop internal model
```
Check condition
↓
If True → execute body
↓
Go back & re‑check condition
↓
If False → exit loop
```

---

# 1️⃣ Counting Positive Numbers ➕

```python
positive_number_count = 0
```
🧠 Counter initialized **once**, outside loop.
If inside loop → resets every iteration ❌

```python
for num in numbers:
```
Each element assigned to `num` one‑by‑one.

```python
if num > 0:
```
Decision for **each element individually**.

```python
positive_number_count += 1
```
Shortcut for:
```python
positive_number_count = positive_number_count + 1
```

🧠 **Why loop needed?**
Because condition must be checked for *every element*.

---

# 2️⃣ Sum of Even Numbers 🔢

```python
for num in range(1, number + 1):
```
🧠 `range()` is **lazy** – does not create full list.

```python
if num % 2 == 0:
```
Modulo `%` checks remainder.
Even → remainder `0`.

```python
sum_even += 1
```
⚠️ Logical issue:
This code **counts evens**, not sums them.

Correct summation would be:
```python
sum_even += num
```

🎯 **Interview Insight:**
Always confirm *what variable represents*.

---

# 3️⃣ Multiplication Table (Skip Iteration) ✖️

```python
for i in range(1, 11):
```
Loop runs exactly 10 times.

```python
if i == 5:
    continue
```
🧠 `continue`:
- Skips current iteration
- Jumps to **next loop cycle**

```python
print(number * i)
```
Runs for all except `i == 5`.

🧠 **Difference from `break`:**
- `continue` skips
- `break` stops loop entirely

---

# 4️⃣ Reverse a String 🔄

```python
reversed_str = ""
```
Empty string accumulator.

```python
reversed_str = char + reversed_str
```
🧠 Key logic:
Each new character added to **front**.

Example step‑by‑step (`"abc"`):
```
''  → 'a'
'a' → 'ba'
'ba'→ 'cba'
```

🎯 **Why this works:**
Strings are immutable → new string created each time.

---

# 5️⃣ First Non‑Repeated Character 🔍

```python
input_str.count(char)
```
Counts **entire string each time**.

🧠 Time Complexity:
- Outer loop → O(n)
- `count()` → O(n)
Total → O(n²)

```python
break
```
Stops loop once first unique found.

🎯 **Interview Insight:**
Correct but **not optimal**.
Better approach uses dictionary.

---

# 6️⃣ Factorial using `while` 🔢

```python
factorial = 1
```
Identity value for multiplication.

```python
while number > 0:
```
Loop runs until number becomes 0.

```python
factorial *= number
number -= 1
```
🧠 Two critical updates:
- Multiply
- Reduce condition variable

⚠️ Missing decrement → infinite loop ❌

---

# 7️⃣ Input Validation Loop 🔐

```python
while True:
```
Creates **intentional infinite loop**.

```python
if 1 <= number <= 10:
```
Python chained comparison:
```python
1 <= number and number <= 10
```

```python
break
```
Only safe exit point.

🧠 **Pattern used everywhere**:
CLI tools, forms, validation systems.

---

# 8️⃣ Prime Number Checker 🔍

```python
is_prime = True
```
Assume prime **until proven otherwise**.

```python
for i in range(2, input_num):
```
Check divisibility excluding 1 & itself.

```python
if input_num % i == 0:
```
If divisible → NOT prime.

```python
break
```
Stops unnecessary checks.

🧠 Optimization hint:
Check till `sqrt(n)` only.

---

# 9️⃣ List Uniqueness Checker 🧺

```python
unique_item = set()
```
Set chosen for **O(1) lookup**.

```python
if item in unique_item:
```
Detect duplicate immediately.

```python
unique_item.add(item)
```
Executed only if item is new.

🎯 **Why set over list?**
Performance + intent clarity.

---

# 🔟 Exponential Backoff ⏳

```python
wait_time *= 2
```
Doubles delay every retry.

```python
time.sleep(wait_time)
```
Pauses execution.

🧠 Used in:
- Network retries
- API calls
- Distributed systems

```python
while attempts < max_attempts:
```
Prevents infinite retry.

---

## 🧠 Cross‑Problem Patterns (IMPORTANT)

| Pattern | Seen In |
|------|------|
| Counter | #1, #2 |
| Accumulator | #4, #6 |
| Sentinel loop | #7, #10 |
| Early exit (`break`) | #3, #5, #8, #9 |
| Validation | #6, #7 |

---

## 🎯 Questions & Answers

### Q1. Why initialize variables outside loop?
**Ans:** To preserve state across iterations.

### Q2. When to use `break`?
**Ans:** When goal is achieved early.

### Q3. Difference between `for` & `while` here?
**Ans:** `for` → known iterations, `while` → condition‑driven.

### Q4. Why sets used in uniqueness check?
**Ans:** Faster membership testing.

---

## 🧠 FINAL MENTAL MODEL

```
Loop = Controlled repetition
State variables control loop life
Break = emergency exit
Continue = skip step
```

---

🔥 END – ULTRA‑DEEP LOOPS PROBLEM NOTES

