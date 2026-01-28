# Lists in Python – Zero to Advanced++ Complete Notes

These notes explain **Python Lists** from **absolute basics to deep internals**, including:
- What lists are and why they exist
- Memory & mutability behavior
- ALL commonly used list methods
- Slicing, copying, sorting
- List comprehensions
- Performance tips & interview traps

👉 **Every concept includes code + OUTPUT** so nothing is left to imagination.

---

## 1. What is a List in Python?

A **list** is an **ordered, mutable collection** of elements.

```python
lst = [1, 2, 3]
print(lst)
print(type(lst))
```

**Output:**
```
[1, 2, 3]
<class 'list'>
```

Properties:
- Ordered (index-based)
- Mutable (can change)
- Allows duplicates
- Can store mixed data types

---

## 2. Creating Lists (ALL Ways)

### 2.1 Literal Syntax

```python
lst = [1, 'hello', 3.14]
print(lst)
```

**Output:**
```
[1, 'hello', 3.14]
```

---

### 2.2 Using `list()` Constructor

```python
lst = list("abc")
print(lst)
```

**Output:**
```
['a', 'b', 'c']
```

---

### 2.3 Using `range()`

```python
lst = list(range(5))
print(lst)
```

**Output:**
```
[0, 1, 2, 3, 4]
```

---

## 3. Indexing & Slicing

```python
lst = [10, 20, 30, 40, 50]
print(lst[0])
print(lst[-1])
print(lst[1:4])
```

**Output:**
```
10
50
[20, 30, 40]
```

---

## 4. List Mutability (VERY IMPORTANT)

```python
lst = [1, 2, 3]
lst[0] = 99
print(lst)
```

**Output:**
```
[99, 2, 3]
```

✔ Same list object modified

---

## 5. Adding Elements to List

### 5.1 `append()`

```python
lst = [1, 2]
lst.append(3)
print(lst)
```

**Output:**
```
[1, 2, 3]
```

---

### 5.2 `extend()`

```python
lst = [1, 2]
lst.extend([3, 4])
print(lst)
```

**Output:**
```
[1, 2, 3, 4]
```

---

### 5.3 `insert()`

```python
lst = [1, 3]
lst.insert(1, 2)
print(lst)
```

**Output:**
```
[1, 2, 3]
```

---

## 6. Removing Elements

### 6.1 `remove()`

```python
lst = [1, 2, 3]
lst.remove(2)
print(lst)
```

**Output:**
```
[1, 3]
```

---

### 6.2 `pop()`

```python
lst = [1, 2, 3]
print(lst.pop())
print(lst)
```

**Output:**
```
3
[1, 2]
```

---

### 6.3 `clear()`

```python
lst = [1, 2]
lst.clear()
print(lst)
```

**Output:**
```
[]
```

---

## 7. Searching & Counting

```python
lst = [1, 2, 2, 3]
print(lst.index(2))
print(lst.count(2))
```

**Output:**
```
1
2
```

---

## 8. Sorting & Reversing

### 8.1 `sort()` (in-place)

```python
lst = [3, 1, 2]
lst.sort()
print(lst)
```

**Output:**
```
[1, 2, 3]
```

---

### 8.2 `sorted()` (new list)

```python
lst = [3, 1, 2]
new_lst = sorted(lst)
print(new_lst)
print(lst)
```

**Output:**
```
[1, 2, 3]
[3, 1, 2]
```

---

### 8.3 Reverse

```python
lst = [1, 2, 3]
lst.reverse()
print(lst)
```

**Output:**
```
[3, 2, 1]
```

---

## 9. Copying Lists (VERY IMPORTANT)

### 9.1 Assignment (NOT a copy)

```python
a = [1, 2]
b = a
a.append(3)
print(b)
```

**Output:**
```
[1, 2, 3]
```

---

### 9.2 Shallow Copy

```python
a = [1, 2]
b = a.copy()
a.append(3)
print(a)
print(b)
```

**Output:**
```
[1, 2, 3]
[1, 2]
```

---

### 9.3 Deep Copy

```python
import copy
a = [[1, 2], [3, 4]]
b = copy.deepcopy(a)
a[0][0] = 99
print(a)
print(b)
```

**Output:**
```
[[99, 2], [3, 4]]
[[1, 2], [3, 4]]
```

---

## 10. List Comprehensions (VERY IMPORTANT)

```python
squares = [x*x for x in range(5)]
print(squares)
```

**Output:**
```
[0, 1, 4, 9, 16]
```

With condition:

```python
evens = [x for x in range(10) if x % 2 == 0]
print(evens)
```

**Output:**
```
[0, 2, 4, 6, 8]
```

---

## 11. Nested Lists

```python
matrix = [[1, 2], [3, 4]]
print(matrix[1][0])
```

**Output:**
```
3
```

---

## 12. Membership & Iteration

```python
lst = [1, 2, 3]
print(2 in lst)
for x in lst:
    print(x)
```

**Output:**
```
True
1
2
3
```

---

## 13. Performance Tips (INTERVIEW GOLD)

- `append()` → O(1)
- `insert(0, x)` → O(n)
- `pop()` → O(1)
- `pop(0)` → O(n)

---

## 14. Common Interview Traps

❌ Modifying list while iterating
❌ Confusing `append` vs `extend`
❌ Shallow copy bugs

---

## 15. List vs Tuple (Quick)

| Feature | List | Tuple |
|------|------|------|
| Mutable | Yes | No |
| Speed | Slower | Faster |
| Use case | Dynamic data | Fixed data |

---

## 16. Mental Model (MUST REMEMBER)

```
List = Dynamic array
Stores references
Mutable container
```

---

## Final Takeaway

> **Lists are mutable, ordered containers designed for dynamic collections and are one of Python’s most powerful built-in data structures.**

---

✅ End of Lists Notes

