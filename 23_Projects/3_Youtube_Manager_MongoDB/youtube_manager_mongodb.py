import os
from dotenv import load_dotenv
from pymongo import MongoClient
from bson import ObjectId

# Load .env file
load_dotenv()

# Get Mongo URI from environment
mongo_uri = os.getenv("MONGO_URI")

# Connect to MongoDB
client = MongoClient(mongo_uri, tlsAllowInvalidCertificates=True)
# tlsAllowInvalidCertificates=True - Not a good way to handle ssl

db = client["PyYouTube"]
videos_collection = db["videos"]


def list_videos():
    for video in videos_collection.find():
        print(f"ID: {video['_id']}, Name: {video['name']}, Time: {video['time']}")


def add_video(name, time):
    videos_collection.insert_one({"name": name, "time": time})


def update_video(video_id, name, time):
    videos_collection.update_one(
        {"_id": ObjectId(video_id)}, {"$set": {"name": name, "time": time}}
    )


def delete_video(video_id):
    videos_collection.delete_one({"_id": ObjectId(video_id)})


# 🚀 Main application loop
def main():
    while True:
        print("\n🎥 YouTube Manager App (MongoDB Powered)")
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


if __name__ == "__main__":
    main()
