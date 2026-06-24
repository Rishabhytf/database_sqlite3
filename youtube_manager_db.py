import sqlite3

conn = sqlite3.connect('youtube_videos.db')

cursor = conn.cursor()

cursor.execute('''
        CREATE TABLE IF NOT EXISTS  videos (
                    id INTEGER PRIMARY KEY,
                    name TEXT NOT NULL,
                    time TEXT NOT NULL
        
        )


''')

def list_videos():
    print("\n")
    print("*" * 70)
    cursor.execute("SELECT * FROM videos")
    for row in cursor.fetchall():
        print(row)
    print("*" * 70)
    print("All videos are listed Here")

def add_video(name, time):
    print("\n")
    print("*" * 70)
    cursor.execute("INSERT INTO videos (name, time) VALUES (?, ?)", (name, time))
    print("Video Added Successfully")
    print("*" * 70)
    conn.commit()

def update_video(video_id, new_name, new_time):
    print("\n")
    print("*" * 70)
    cursor.execute("UPDATE videos SET name = ?, time = ?  WHERE id = ?", (new_name, new_time, video_id))
    print("Video Updated Successfully")
    print("*" * 70)
    conn.commit()

def delete_video(video_id):
    print("\n")
    print("*" * 70)
    cursor.execute("DELETE FROM videos where id = ?",(video_id,))
    print("Video Deleted Successfully")
    print("*" * 70)
    conn.commit()

def main():
    while True:
        print("\n Youtube manager app with DB")
        print("1. List Videos: ")
        print("2. Add Videos: ")
        print("3. Update Video: ")
        print("4. Delete Video: ")
        print("5. Exit App")
        choice = input("Enter Your Choice: ") 

        if choice == '1':
            list_videos()
        elif choice == '2':
            name = input("Enter the Video Name: ")
            time = input("Enter the Video time: ")
            add_video(name, time)
        elif choice == '3':
            video_id = input("Enter the Video ID to Update: ")
            name = input("Enter the Video Name: ")
            time = input("Enter the Video time: ")
            update_video(video_id, name, time)
        elif choice == '4':
            video_id = input("Enter the Video ID to Delete: ")
            delete_video(video_id)
        elif choice == '5':
            print("*" * 70)
            print("You are Successfully Exited")
            print("*" * 70)
            break
        else:
            print("\n")
            print("*" * 70)
            print("* Invalid Choice *")
            print("*" * 70)
            print("Please Choose correct option")

    conn.close()
        






if __name__ == "__main__":
    main()