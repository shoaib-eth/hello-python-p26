import sqlite3

# 📦 Database connection
conn = sqlite3.connect("youtube_manager.db")
cursor = conn.cursor()

# 🗄️ Create table if it doesn't exist
cursor.execute("""
CREATE TABLE IF NOT EXISTS videos (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    time TEXT NOT NULL
)
""")


# 📋 List all videos
def list_videos():
    print("\n📺 Your YouTube Videos:")
    print("-" * 30)
    cursor.execute("SELECT * FROM videos")
    for row in cursor.fetchall():
        print(f"ID: {row[0]} | 🎬 Name: {row[1]} | ⏱️ Time: {row[2]}")
    print("-" * 30)


# ➕ Add a new video
def add_video(name, time):
    cursor.execute("INSERT INTO videos (name, time) VALUES (?, ?)", (name, time))
    conn.commit()
    print("✅ Video added successfully!")


# ✏️ Update an existing video
def update_video(video_id, name, time):
    cursor.execute(
        "UPDATE videos SET name = ?, time = ? WHERE id = ?", (name, time, video_id)
    )
    conn.commit()
    print("🔄 Video updated successfully!")


# ❌ Delete a video
def delete_video(video_id):
    cursor.execute("DELETE FROM videos WHERE id = ?", (video_id,))
    conn.commit()
    print("🗑️ Video deleted successfully!")


# 🚀 Main application loop
def main():
    while True:
        print("\n🎥 YouTube Manager App (SQLite Powered)")
        print("====================================")
        print("1️⃣  List Videos")
        print("2️⃣  Add Video")
        print("3️⃣  Update Video")
        print("4️⃣  Delete Video")
        print("5️⃣  Exit")
        print("====================================")

        choice = input("👉 Enter your choice: ")

        if choice == "1":
            list_videos()

        elif choice == "2":
            name = input("🎬 Enter video name: ")
            time = input("⏱️ Enter video time: ")
            add_video(name, time)

        elif choice == "3":
            video_id = input("🆔 Enter video ID to update: ")
            name = input("✏️ Enter new video name: ")
            time = input("⏱️ Enter new video time: ")
            update_video(video_id, name, time)

        elif choice == "4":
            video_id = input("🗑️ Enter video ID to delete: ")
            delete_video(video_id)

        elif choice == "5":
            print("👋 Exiting the application. Bye bye!")
            break

        else:
            print("❌ Invalid choice. Please try again!")

    # 🔒 Close database connection
    conn.close()


# 🏁 Entry point
if __name__ == "__main__":
    main()
