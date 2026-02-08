# Strings in Python – Complete Notes

These notes explain **Python Strings** from **absolute basics to deep internals**, covering:
- All string types
- Immutability & memory model
- Indexing, slicing
- **Almost all commonly used string methods**
- Each concept with **example code + output**

Strings are one of the **MOST IMPORTANT** topics for interviews, backend, and Data Science.

---

## 1. What is a String in Python?

A **string** is a sequence of **Unicode characters**.

```python
s = "hello"
print(type(s))
```

**Output:**
```
<class 'str'>
```

✔ Strings are **objects**
✔ Strings are **immutable**

---

## 2. Types of Strings in Python

### 2.1 Single-line Strings

```python
s1 = 'hello'
s2 = "hello"
print(s1, s2)
```

**Output:**
```
hello hello
```

---

### 2.2 Multi-line Strings (Triple Quotes)

```python
s = '''Hello
World'''
print(s)
```

**Output:**
```
Hello
World
```

---

### 2.3 Raw Strings (`r''`)

Used mainly for **regex & file paths**.

```python
path = r"C:\new\test"
print(path)
```

**Output:**
```
C:\new\test
```

---

### 2.4 Byte Strings (`bytes`)

```python
b = b'abc'
print(b)
print(type(b))
```

**Output:**
```
b'abc'
<class 'bytes'>
```

---

## 3. String Immutability (VERY IMPORTANT)

```python
s = "hello"
s[0] = 'H'
```

**Output:**
```
TypeError: 'str' object does not support item assignment
```

✔ Any modification creates a **new string object**

---

## 4. Indexing & Slicing

```python
s = "python"
print(s[0])
print(s[-1])
print(s[1:4])
```

**Output:**
```
p
n
yth
```

---

## 5. String Concatenation & Repetition

```python
print("py" + "thon")
print("ha" * 3)
```

**Output:**
```
python
hahaha
```

---

## 6. Membership Operators

```python
print('py' in 'python')
print('z' not in 'python')
```

**Output:**
```
True
True
```

---

## 7. String Formatting (VERY IMPORTANT)

### 7.1 f-Strings (Recommended)

```python
name = "Alice"
age = 20
print(f"My name is {name}, age {age}")
```

**Output:**
```
My name is Shoaib, age 22
```

---

### 7.2 `format()`

```python
print("{} scored {}".format("Alex", 90))
```

**Output:**
```
Alex scored 90
```

---

### 7.3 `%` Formatting (Old)

```python
print("%s is %d years old" % ("Bob", 30))
```

**Output:**
```
Bob is 30 years old
```

---

## 8. Common String Methods (WITH OUTPUT)

### Case Conversion

```python
s = "Python"
print(s.upper())
print(s.lower())
print(s.capitalize())
print(s.title())
```

**Output:**
```
PYTHON
python
Python
Python
```

---

### Checking Methods

```python
print("123".isdigit())
print("abc".isalpha())
print("abc123".isalnum())
print(" ".isspace())
```

**Output:**
```
True
True
True
True
```

---

### Search & Count

```python
s = "banana"
print(s.find('a'))
print(s.count('a'))
```

**Output:**
```
1
3
```

---

### Replace

```python
print("hello world".replace("world", "Python"))
```

**Output:**
```
hello Python
```

---

### Split & Join

```python
s = "a,b,c"
print(s.split(','))
print('-'.join(['a', 'b', 'c']))
```

**Output:**
```
['a', 'b', 'c']
a-b-c
```

---

### Strip Whitespace

```python
s = "  hello  "
print(s.strip())
print(s.lstrip())
print(s.rstrip())
```

**Output:**
```
hello
hello  
  hello
```

---

### Startswith / Endswith

```python
print("python".startswith("py"))
print("python".endswith("on"))
```

**Output:**
```
True
True
```

---

## 9. Encoding & Decoding

```python
s = "hello"
b = s.encode('utf-8')
print(b)
print(b.decode('utf-8'))
```

**Output:**
```
b'hello'
hello
```

---

## 10. Iterating Over String

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

## 11. String Comparison

```python
print("abc" == "abc")
print("abc" < "b")
```

**Output:**
```
True
True
```

Lexicographical (dictionary order)

---

## 12. Escape Characters

```python
print("Hello\nWorld")
print("She said \"Hi\"")
```

**Output:**
```
Hello
World
She said "Hi"
```

---

## 13. Performance Tip (IMPORTANT)

❌ Bad:
```python
s = ""
for i in range(3):
    s += "a"
```

✅ Good:
```python
parts = []
for i in range(3):
    parts.append("a")
print(''.join(parts))
```

**Output:**
```
aaa
```

---

## 14. Interning (Advanced)

```python
a = "hello"
b = "hello"
print(a is b)
```

**Output:**
```
True
```

Small strings may be cached

---

## 15. Interview Mental Model

```
Strings are:
- Immutable
- Unicode
- Sequence of characters
- Rich in methods
```

---

## Final Takeaway

> **Strings in Python are immutable Unicode objects with powerful built-in methods for text processing.**

## 🧠 One-line mastery statement

> **Python strings are immutable Unicode sequences with a rich set of built-in methods for text processing.**

---

✅ End of Strings Notes

