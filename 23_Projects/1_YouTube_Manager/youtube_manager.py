import json


# 📂 Load videos data from file
def load_data():
    try:
        with open("youtube.txt", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        # ⚠️ File not found? Start fresh!
        return []


# 💾 Save videos data to file
def save_data_helper(videos):
    with open("youtube.txt", "w") as file:
        json.dump(videos, file)


# 📺 Show all saved videos
def list_all_videos(videos):
    print("\n")
    print("🎬" * 20 + " Your YouTube Videos " + "🎬" * 20)

    if not videos:
        print("😢 No videos found. Add some first!")
    else:
        for index, video in enumerate(videos, start=1):
            print(f"🔹 {index}. {video['name']} ⏱ Duration: {video['time']}")

    print("🎬" * 60)


# ➕ Add a new video
def add_video(videos):
    print("\n➕ Add New Video")
    name = input("📌 Enter video name: ")
    time = input("⏱ Enter video duration: ")

    videos.append({"name": name, "time": time})

    save_data_helper(videos)
    print("✅ Video added successfully!")


# ✏️ Update existing video
def update_video(videos):
    print("\n✏️ Update Video")
    list_all_videos(videos)

    index = int(input("👉 Enter the video number to update: "))

    if 1 <= index <= len(videos):
        name = input("📝 Update video name: ")
        time = input("⏱ Update video duration: ")

        videos[index - 1] = {"name": name, "time": time}

        save_data_helper(videos)
        print("✅ Video updated successfully!")
    else:
        print("❌ Invalid video number!")


# 🗑 Delete a video
def delete_video(videos):
    print("\n🗑 Delete Video")
    list_all_videos(videos)

    index = int(input("👉 Enter the video number to delete: "))

    if 1 <= index <= len(videos):
        del videos[index - 1]
        save_data_helper(videos)
        print("✅ Video deleted successfully!")
    else:
        print("❌ Invalid video number!")


# 🚀 Main application loop
def main():
    videos = load_data()

    while True:
        print("\n")
        print("🎥" * 15 + " YouTube Manager " + "🎥" * 15)
        print("1️⃣  List all videos")
        print("2️⃣  Add a video")
        print("3️⃣  Update a video")
        print("4️⃣  Delete a video")
        print("5️⃣  Exit 🚪")

        choice = input("👉 Enter your choice (1-5): ")

        match choice:
            case "1":
                list_all_videos(videos)
            case "2":
                add_video(videos)
            case "3":
                update_video(videos)
            case "4":
                delete_video(videos)
            case "5":
                print("👋 Exiting YouTube Manager. Bye bye!")
                break
            case _:
                print("⚠️ Invalid choice! Please enter 1 to 5.")


# 🏁 Program entry point
if __name__ == "__main__":
    main()
