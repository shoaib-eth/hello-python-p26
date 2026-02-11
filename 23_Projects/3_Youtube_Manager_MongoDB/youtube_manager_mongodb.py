import os
from dotenv import load_dotenv
from pymongo import MongoClient
from bson import ObjectId

# 🌿 Load Environment Variables
load_dotenv()

# 🔑 Fetch MongoDB URI from .env file
mongo_uri = os.getenv("MONGO_URI")


# 🌐 Connect to MongoDB
client = MongoClient(
    mongo_uri, tlsAllowInvalidCertificates=True  # ⚠️ Not recommended for production
)

db = client["PyYouTube"]
videos_collection = db["videos"]


# 📋 LIST ALL VIDEOS
def list_videos():
    print("\n📜 Available Videos:\n" + "-" * 40)

    for video in videos_collection.find():
        print(f"""
🆔 ID   : {video['_id']}
🎬 Name : {video['name']}
⏱️  Time : {video['time']}
----------------------------------------
""")


# ➕ ADD NEW VIDEO
def add_video(name, time):
    videos_collection.insert_one({"name": name, "time": time})
    print("✅ Video added successfully!")


# ✏️ UPDATE VIDEO
def update_video(video_id, name, time):
    videos_collection.update_one(
        {"_id": ObjectId(video_id)}, {"$set": {"name": name, "time": time}}
    )
    print("🔄 Video updated successfully!")


# 🗑️ DELETE VIDEO
def delete_video(video_id):
    videos_collection.delete_one({"_id": ObjectId(video_id)})
    print("🗑️ Video deleted successfully!")


# 🚀 MAIN APPLICATION LOOP
def main():
    while True:
        print("\n" + "=" * 50)
        print("🎥       YouTube Manager App       🎥")
        print("📦         MongoDB Powered         📦")
        print("=" * 50)
        print("1️⃣  List Videos")
        print("2️⃣  Add Video")
        print("3️⃣  Update Video")
        print("4️⃣  Delete Video")
        print("5️⃣  Exit")
        print("=" * 50)

        choice = input("👉 Enter your choice: ").strip()

        if choice == "1":
            list_videos()

        elif choice == "2":
            name = input("🎬 Enter video name: ")
            time = input("⏱️  Enter video time: ")
            add_video(name, time)

        elif choice == "3":
            video_id = input("🆔 Enter video ID to update: ")
            name = input("✏️ Enter new video name: ")
            time = input("⏱️  Enter new video time: ")
            update_video(video_id, name, time)

        elif choice == "4":
            video_id = input("🗑️ Enter video ID to delete: ")
            delete_video(video_id)

        elif choice == "5":
            print("\n👋 Exiting the application... Bye bye 🚀")
            break

        else:
            print("❌ Invalid choice. Please try again!")


# 🏁 ENTRY POINT
if __name__ == "__main__":
    main()
