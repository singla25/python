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
    name = input("Enter video name: ").strip()
    time = input("Enter video time: ").strip()
    if not name or not time:
        print("Name and time can't be empty.")
        return
    # ? placeholders keep user input safe from SQL injection
    cursor.execute("INSERT INTO videos (name, time) VALUES (?, ?)", (name, time))
    conn.commit()  # commit saves the change to the file
    print("Video added.")


def get_video():
    """Show videos, ask for an ID, return that video (or None)."""
    list_all_videos()
    try:
        video_id = int(input("Enter video ID: "))
    except ValueError:
        print("ID must be a number.")
        return None
    cursor.execute("SELECT * FROM videos WHERE id = ?", (video_id,))
    video = cursor.fetchone()
    if video is None:
        print(f"No video found with ID = {video_id}")
    return video


def update_video():
    video = get_video()
    if video is None:
        return
    print(f"Current -> Name: {video[1]}, Time: {video[2]}")
    name = input("Enter new video name: ")
    time = input("Enter new video time: ")
    cursor.execute("UPDATE videos SET name = ?, time = ? WHERE id = ?", (name, time, video[0]))
    conn.commit()
    print("Video updated.")


def delete_video():
    video = get_video()
    if video is None:
        return
    cursor.execute("DELETE FROM videos WHERE id = ?", (video[0],))
    conn.commit()
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