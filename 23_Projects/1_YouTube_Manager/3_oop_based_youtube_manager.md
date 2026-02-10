# Python Language — YouTube Manager Project (OOP / Class-Based Design)

> **Why this part is IMPORTANT** 🔥
>
> Functional version is good for learning.
>
> **OOP version is what interviewers & real projects expect.**
>
> In this document, we will:
> - Convert the project into a **class-based design**
> - Understand **why OOP fits naturally here**
> - Follow **execution flow with objects**
> - Visualize memory & responsibilities

---

## 1️⃣ Why OOP for This Project? (Big Picture)

Think about the project:

- We manage **videos** 📺
- We load/save **data** 📂
- We perform **operations** (add, update, delete)

👉 All of this belongs to **ONE logical entity**:

```
YouTubeManager
```

Instead of spreading logic across free functions, we **bundle data + behavior together**.

This is exactly what **OOP is meant for**.

---

## 2️⃣ High-Level OOP Architecture 🏗

```
YouTubeManager (class)
│
├── data
│   └── self.videos
│
├── load_data()
├── save_data()
├── list_videos()
├── add_video()
├── update_video()
├── delete_video()
├── show_menu()
└── run()
```

🎯 One class = one responsibility.

---

## 3️⃣ OOP Version — Complete Code 🧩

```python
import json


class YouTubeManager:
    def __init__(self, filename="youtube.txt"):
        self.filename = filename
        self.videos = self.load_data()

    # 📂 Load data from file
    def load_data(self):
        try:
            with open(self.filename, "r") as file:
                return json.load(file)
        except FileNotFoundError:
            return []

    # 💾 Save data to file
    def save_data(self):
        with open(self.filename, "w") as file:
            json.dump(self.videos, file)

    # 📺 List all videos
    def list_videos(self):
        print("\n🎬" * 10 + " Your Videos " + "🎬" * 10)
        if not self.videos:
            print("😢 No videos found")
        else:
            for i, video in enumerate(self.videos, start=1):
                print(f"{i}. {video['name']} ⏱ {video['time']}")

    # ➕ Add a video
    def add_video(self):
        name = input("📌 Enter video name: ")
        time = input("⏱ Enter duration: ")
        self.videos.append({"name": name, "time": time})
        self.save_data()
        print("✅ Video added")

    # ✏️ Update a video
    def update_video(self):
        self.list_videos()
        index = int(input("Enter video number to update: "))

        if 1 <= index <= len(self.videos):
            name = input("New name: ")
            time = input("New duration: ")
            self.videos[index - 1] = {"name": name, "time": time}
            self.save_data()
            print("✅ Video updated")
        else:
            print("❌ Invalid choice")

    # 🗑 Delete a video
    def delete_video(self):
        self.list_videos()
        index = int(input("Enter video number to delete: "))

        if 1 <= index <= len(self.videos):
            del self.videos[index - 1]
            self.save_data()
            print("✅ Video deleted")
        else:
            print("❌ Invalid choice")

    # 📋 Show menu
    def show_menu(self):
        print("\n🎥 YouTube Manager 🎥")
        print("1. List videos")
        print("2. Add video")
        print("3. Update video")
        print("4. Delete video")
        print("5. Exit")

    # 🚀 Run application
    def run(self):
        while True:
            self.show_menu()
            choice = input("Choose (1-5): ")

            match choice:
                case "1":
                    self.list_videos()
                case "2":
                    self.add_video()
                case "3":
                    self.update_video()
                case "4":
                    self.delete_video()
                case "5":
                    print("👋 Bye")
                    break
                case _:
                    print("⚠️ Invalid option")


if __name__ == "__main__":
    app = YouTubeManager()
    app.run()
```

---

## 4️⃣ Execution Flow in OOP Version 🔄

```
Program Start
  ↓
Create YouTubeManager object
  ↓
__init__() loads data
  ↓
run() starts menu loop
  ↓
User input
  ↓
Method call on SAME object
  ↓
Modify self.videos
  ↓
Save to file
  ↓
Back to menu
```

👉 **State lives inside the object**, not global variables.

---

## 5️⃣ Memory Visualization 🧠

```
app (YouTubeManager object)
│
├── filename → "youtube.txt"
├── videos → [ {video}, {video} ]
├── methods → shared via class
```

- `self.videos` is the single source of truth
- All methods operate on the same memory

---

## 6️⃣ Why This is Better Than Functional Version ✅

| Aspect | Functional | OOP |
|-----|-----------|-----|
| State handling | External list | Inside object |
| Structure | Scattered | Encapsulated |
| Reusability | Low | High |
| Interview value | Medium | High |
| Real-world fit | ❌ | ✅ |

---

## 🎯 Interview Answer (Perfect)

> "I refactored the project into a class-based design where the YouTubeManager object owns both the data and operations, ensuring encapsulation, cleaner state management, and easier extensibility."

🔥 Strong OOP explanation.

---

## ✅ What You Mastered Here

- Practical OOP design
- Encapsulation & state
- Object lifecycle
- Real CLI architecture

---

✨ END — YouTube Manager (OOP Design Notes)

