import json

FILE_NAME = "youtube.json"

def load_data():
    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_data(videos):
    with open(FILE_NAME, "w") as file:
        json.dump(videos, file)

def list_all_videos(videos):
    if not videos:
        print("No videos yet.")
        return
     
    print("\n" + "*" * 40)

    for index, video in enumerate(videos, start=1):
        print(f"{index}. Name: {video['name']} | Duration: {video['time']}")

    print("*" * 40)

def add_video(videos):
    name = input("Enter video name: ")
    time = input("Enter video time: ")
    videos.append({"name": name, "time": time})
    save_data(videos)
    print("Video added.")

def video_number(videos):
    """Ask the user for a video number; return its list index or None if invalid."""
    list_all_videos(videos)
    if not videos:
        return None
    try:
        number = int(input("Enter the video number: "))
    except ValueError:
        print("Please enter a number.")
        return None
    if 1 <= number <= len(videos):
        return number - 1
    print("Invalid video number.")
    return None

def update_video(videos):
    index = video_number(videos)
    if index is None:
        return
    name = input("Enter the new video name: ")
    time = input("Enter the new video time: ")
    videos[index] = {"name": name, "time": time}
    save_data(videos)
    print("Video updated.")

def delete_video(videos):
    index = video_number(videos)
    if index is None:
        return
    removed = videos.pop(index)
    save_data(videos)
    print(f"Deleted '{removed['name']}'.")

def main():

    videos = load_data()

    while True:
        print("\n Youtube Manager | Choose an Option ")
        print("1. List all youtube videos")
        print("2. Add a youtube video")
        print("3. Update a youtube video details")
        print("4. Delete a youtube video")
        print("5. Exit an App")

        choice = input("Enter your choice: ")

        match choice:
            case '1':
                list_all_videos(videos)
            case '2':
                add_video(videos)
            case '3':
                update_video(videos)
            case '4':
                delete_video(videos)
            case '5':
                break
            case _:
                print("Invalid Choice")

if __name__ == "__main__":
    main()