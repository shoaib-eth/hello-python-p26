# Python Language — YouTube Manager Project (SQLite3 Based)

> **How to read these notes** 📖
>
> These notes explain the project **line-by-line + flow-wise**, exactly how Python and SQLite work together at runtime.
>
> Think of this as:
> - CLI App Flow 🚦
> - Database Internals 🗄️
> - Memory + Disk Interaction 🧠💾


---

## 1️⃣ Big Picture — What This Project Is Doing 🎯

This project is a **CLI-based YouTube Manager** that:

- Stores data **persistently** using SQLite 🗄️
- Performs **CRUD operations** (Create, Read, Update, Delete)
- Uses **SQL + Python** together
- Avoids files like JSON and instead uses a **real database**

👉 This is a **HUGE upgrade** from the file-based version.

---

## 2️⃣ Import Phase — Loading SQLite Engine 🧠

```python
import sqlite3
```

### What happens internally

- Python loads the built-in `sqlite3` module
- This module is a **wrapper over SQLite C library**
- SQLite is **serverless** (no MySQL server running)

📌 SQLite DB = single `.db` file on disk

---

## 3️⃣ Database Connection — Bridge Between Python & DB 🔗

```python
conn = sqlite3.connect("youtube_manager.db")
cursor = conn.cursor()
```

### Line-by-line

#### `sqlite3.connect()`

- If file exists → opens it
- If file does NOT exist → creates it

```
youtube_manager.db
```

📦 This file stores:
- Tables
- Rows
- Indexes

---

#### `conn.cursor()`

- Cursor = **SQL command executor**
- Python does NOT run SQL directly
- Cursor acts like a **remote control** 🎮

```
Python → Cursor → SQLite Engine → DB File
```

---

## 4️⃣ Table Creation — Schema Definition 🗄️

```python
cursor.execute("""
CREATE TABLE IF NOT EXISTS videos (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    time TEXT NOT NULL
)
""")
```

### Why this runs first?

- Ensures DB is ready before user interaction
- Safe to run every time (idempotent)

---

### Column Breakdown 🧩

| Column | Type | Meaning |
|------|----|--------|
| id | INTEGER PRIMARY KEY | Auto-increment unique ID |
| name | TEXT | Video title |
| time | TEXT | Duration |

📌 `PRIMARY KEY` in SQLite = auto-increment rowid

---

## 5️⃣ SELECT Operation — Listing Videos 📋

```python
def list_videos():
```

### Flow

```python
cursor.execute("SELECT * FROM videos")
```

- SQL query sent to DB
- DB scans table
- Rows returned to cursor

```python
cursor.fetchall()
```

- Converts DB rows → Python list of tuples

📦 Example memory:
```
[(1, 'Python Intro', '10:00'), (2, 'Decorators', '15:30')]
```

---

### Printing Logic

```python
row[0] → id
row[1] → name
row[2] → time
```

📌 Order matches table schema

---

## 6️⃣ INSERT Operation — Adding a Video ➕

```python
def add_video(name, time):
```

```python
cursor.execute(
    "INSERT INTO videos (name, time) VALUES (?, ?)",
    (name, time)
)
```

### Why `?` placeholders?

- Prevents **SQL Injection** 🔒
- SQLite safely binds values

---

### Commit — VERY IMPORTANT 🔥

```python
conn.commit()
```

- Without commit → data stays in memory
- Commit flushes data to disk

📌 Interview line:
> "SQLite uses transactional commits; without commit, changes are rolled back."

---

## 7️⃣ UPDATE Operation — Modifying Data ✏️

```python
UPDATE videos SET name = ?, time = ? WHERE id = ?
```

### Execution Flow

```
User provides ID
   ↓
SQLite locates row
   ↓
Row values replaced
   ↓
Commit saves changes
```

📌 Only matching ID row is updated

---

## 8️⃣ DELETE Operation — Removing Data 🗑️

```python
DELETE FROM videos WHERE id = ?
```

### What happens internally

- SQLite finds row by primary key
- Row marked deleted
- Space reused later

📌 This is **permanent deletion**

---

## 9️⃣ Main Loop — Controller Logic 🚦

```python
def main():
    while True:
```

This loop:
- Displays menu
- Takes user input
- Routes execution

Same idea as previous version, but **storage backend changed**.

---

## 🔟 User Choice Flow (Runtime)

```
User Input
   ↓
if / elif controller
   ↓
Database operation
   ↓
commit (if write)
   ↓
Back to menu
```

---

## 1️⃣1️⃣ Exit & Cleanup 🔒

```python
conn.close()
```

### Why important?

- Releases file lock
- Flushes buffers
- Prevents DB corruption

📌 Interview favorite:
> "Always close DB connections explicitly."

---

## 1️⃣2️⃣ Program Entry Point 🏁

```python
if __name__ == "__main__":
    main()
```

- Prevents accidental execution
- Industry standard

---

## 🧠 Memory + Disk Visualization

```
User Input
   ↓
Python Function
   ↓
Cursor executes SQL
   ↓
SQLite Engine
   ↓
.youtube_manager.db (disk)
```

---

## ✅ File-Based vs SQLite Version (WHY THIS IS BETTER)

| Feature | JSON File | SQLite |
|------|----------|--------|
| Scalability | ❌ | ✅ |
| Concurrency | ❌ | ✅ |
| Data Integrity | ❌ | ✅ |
| Interview Value | Medium | High |
| Real World | Rare | Common |

---

## 🎯 Interview-Ready Explanation

> "This project uses SQLite as a persistent storage backend where Python interacts through cursors, executes parameterized SQL queries for CRUD operations, commits transactional changes, and ensures data integrity with proper connection management."

🔥 Strong professional answer.

---

✨ END — YouTube Manager (SQLite3 Deep-Dive Notes)

