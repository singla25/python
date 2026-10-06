import sqlite3

conn = sqlite3.connect('youtube_manager.db')
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS videos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        time TEXT NOT NULL
    )
''')

def list_all_videos():
    cursor.execute("SELECT * FROM videos")
    videos = cursor.fetchall()
    if not videos:
        print("No videos found.")
        return

    print("\n" + "-" * 50)
    print(f"{'ID':<5}{'Name':<30}{'Time':<15}")
    print("-" * 50)
    for video in videos:
        print(f"{video[0]:<5}{video[1]:<30}{video[2]:<15}")
    print("-" * 50)

def add_video():
    name = input("Enter video name: ")
    time = input("Enter video time: ")
    cursor.execute("INSERT INTO videos (name, time) VALUES (?, ?)", (name, time))
    conn.commit()
    print("Video added.")

def update_video():
    list_all_videos()          # show the table first, so user can see valid IDs
    video_id = input("Enter video ID to update: ")
    if not video_id.isdigit():
        print("Invalid ID. Must be a number.")
        return

    cursor.execute("SELECT * FROM videos WHERE id = ?", (int(video_id),))
    video = cursor.fetchone()
    if video is None:
        print(f"No video exists with ID {video_id}.")
        return

    print(f"Current -> Name: {video[1]}, Time: {video[2]}")
    name = input("Enter new video name: ")
    time = input("Enter new video time: ")
    cursor.execute("UPDATE videos SET name = ?, time = ? WHERE id = ?", (name, time, int(video_id)))
    conn.commit()
    print("Video updated.")

def delete_video():
    list_all_videos()          # show the table first, so user can see valid IDs
    video_id = input("Enter video ID to delete: ")
    if not video_id.isdigit():
        print("Invalid ID. Must be a number.")
        return
    cursor.execute("DELETE FROM videos WHERE id = ?", (int(video_id),))
    conn.commit()
    if cursor.rowcount == 0:
        print(f"No video found with ID {video_id}.")
    else:
        print("Video deleted.")

def main():
    try:
        while True:
            print("\n Youtube Manager App with DB | Choose an Option ")
            print("1. List Videos")
            print("2. Add Video")
            print("3. Update Video")
            print("4. Delete Video")
            print("5. Exit")

            choice = input("Enter your choice (1-5): ")

            if choice == '1':
                list_all_videos()
            elif choice == '2':
                add_video()
            elif choice == '3':
                update_video()
            elif choice == '4':
                delete_video()
            elif choice == '5':
                break
            else:
                print("Invalid choice. Please try again.")
    finally:
        conn.close()

if __name__ == "__main__":
    main()