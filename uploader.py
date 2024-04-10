import vimeo
import sys
from tkinter import *
from tkinter import ttk

# Create the API client
client = vimeo.VimeoClient(
    token='c93bc5b483b3e7db712c7924d1b39464',
    key='bc833cfdbd7c734a2a5b47053686914cf1c34b59',
    secret='a0cxBXh+bk51oFqxVwT5g7iN+BTY3u3MaREHh2ZrkHrLTRxpXQulQjk8QgSHqQUt6EnxvQ+ly2vctss0JA0jfuWRYCB7OoE1a/IDC5UfWWwV0rCwjvqafeIE9RtdO8ly'
)

def upload():
    # Make the API call to vimeo
    response = client.post("/videos/933067303/chapters",
                       data = {
                           "title": "Timecode Test 2",
                           "timecode": 2
                       })

    print(response.json())


# Create UI
root = Tk()
root.title("Youtube to Vimeo Chapter Titles")

frame = ttk.Frame(root, padding="10 10 10 10")
frame.grid(column=0, row=0)

# Widgets
videoID_label = ttk.Label(frame, text="Video ID:")
video_id = StringVar()
videoID_field = ttk.Entry(frame, textvariable=video_id, width=14)

chapterTitles_txt = Text(frame, width=40, height=20)

convert_timestamps = BooleanVar()
convertTimestamps_check = ttk.Checkbutton(frame, text="Convert Timestamps (for Worship vs Teaching Only)", 
                                          variable=convert_timestamps, onvalue=True, offvalue=False)

convert_btn = ttk.Button(frame, text="Upload", command=upload)

# Layout
videoID_label.grid(column=0, row=0)
videoID_field.grid(column=0, row=1)
chapterTitles_txt.grid(column=0, row=2)
convertTimestamps_check.grid(column=0, row=3)
convert_btn.grid(column=0, row=4)

root.mainloop()