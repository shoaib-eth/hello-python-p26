# Python Language — YouTube Manager Project

## Step-by-Step FLOW DIAGRAM (Execution Explained Visually)

> **How to use this document** 📖
>
> This is a **visual + logical flow diagram written in text form**.
>
> You should read it **top to bottom**, exactly the way Python executes the program.
>
> Think of this as a **mental flowchart for interviews and debugging** 🧠✨

---

## 🏁 STEP 0 — Program Starts (Python Interpreter Level)

```
Python Interpreter
   ↓
Reads the file top to bottom
```

- All `import` statements are executed
- All `def` functions are **defined in memory**
- No function runs yet ❌

---

## 🚪 STEP 1 — Program Entry Point Check

```python
if __name__ == "__main__":
    main()
```

### Flow Diagram

```
Is file run directly?
   ↓ YES
Call main()
   ↓ NO
Program stops here
```

👉 This ensures controlled execution.

---

## ⚙️ STEP 2 — Entering `main()` Function

```python
def main():
    videos = load_data()
```

### Flow Diagram

```
main()
  ↓
call load_data()
```

- Application bootstrapping starts
- First responsibility: **load persistent data**

---

## 📂 STEP 3 — `load_data()` Execution

```python
try:
    open file → load JSON
except FileNotFoundError:
    return []
```

### Flow Diagram

```
Try opening youtube.txt
   ↓
File exists? ── YES ──▶ Load JSON → return list
   │
   NO
   ↓
Return empty list []
```

📦 Result:

```
videos = []  or  [ {video}, {video}, ... ]
```

👉 Control returns to `main()`

---

## ❤️ STEP 4 — Entering Main Menu Loop

```python
while True:
```

### Flow Diagram

```
Start Menu Loop
   ↓
(Menu repeats forever)
```

- Program now waits for **user interaction**
- This is the heart of the application

---

## 🎥 STEP 5 — Display Menu & Take User Input

```python
choice = input("Enter your choice")
```

### Flow Diagram

```
Display menu
   ↓
Wait for user input
   ↓
Store input in choice
```

👉 Program pauses here until user responds.

---

## 🚦 STEP 6 — Decision Controller (`match-case`)

```python
match choice:
```

### Flow Diagram

```
User choice
   ↓
match-case dispatcher
   ↓
Route to correct function
```

This works like a **traffic signal system 🚦**.

---

## 📺 STEP 7 — Choice "1": List All Videos

### User Input

```
1
```

### Flow Diagram

```
choice == "1"
   ↓
call list_all_videos(videos)
   ↓
print videos using enumerate
   ↓
return to menu loop
```

- Read-only operation
- No data modification

---

## ➕ STEP 8 — Choice "2": Add New Video

### User Input

```
2
```

### Flow Diagram

```
choice == "2"
   ↓
call add_video(videos)
   ↓
Take user input (name, time)
   ↓
Append to videos list
   ↓
Save list to file
   ↓
Return to menu
```

📦 Memory change:

```
videos → grows by one element
```

---

## ✏️ STEP 9 — Choice "3": Update Video

### User Input

```
3
```

### Flow Diagram

```
choice == "3"
   ↓
call update_video(videos)
   ↓
List all videos
   ↓
Ask user for index
   ↓
Validate index
   ↓
Replace video data
   ↓
Save updated list
   ↓
Return to menu
```

Important logic:

```
User index (1-based)
   ↓
Convert to list index (index - 1)
```

---

## 🗑 STEP 🔟 — Choice "4": Delete Video

### User Input

```
4
```

### Flow Diagram

```
choice == "4"
   ↓
call delete_video(videos)
   ↓
List videos
   ↓
Ask index to delete
   ↓
Validate index
   ↓
Delete from list
   ↓
Save list to file
   ↓
Return to menu
```

📦 Memory change:

```
videos → shrinks by one element
```

---

## 🚪 STEP 1️⃣1️⃣ — Choice "5": Exit Program

### User Input

```
5
```

### Flow Diagram

```
choice == "5"
   ↓
break loop
   ↓
exit main()
   ↓
program ends
```

✔ All files closed ✔ No resources leaked

---

## 🔁 STEP 1️⃣2️⃣ — Invalid Input Handling

### User Input

```
Anything else
```

### Flow Diagram

```
Invalid choice
   ↓
Show warning
   ↓
Return to menu
```

Program never crashes 💪

---

## 🧠 FINAL MASTER FLOW (ONE SCREEN VIEW)

```
START
  ↓
__main__ check
  ↓
main()
  ↓
load_data()
  ↓
MENU LOOP
  ↓
User Input
  ↓
match-case
  ↓
CRUD Function
  ↓
Save (if needed)
  ↓
Back to MENU
  ↓
EXIT
```

---

## 🎯 Interview Gold Explanation

> "The program uses a loop-driven controller architecture where user input is routed via match-case to specific CRUD functions, operating on an in-memory list that is synchronized with persistent JSON storage."

🔥 Perfect explanation.

---

✨ END — YouTube Manager Flow Diagram Notes

