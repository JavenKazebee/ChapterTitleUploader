import vimeo
from tkinter import *
from tkinter import ttk
from datetime import datetime, timedelta, time
from dotenv import load_dotenv
import os

load_dotenv()

# Create the API client
client = vimeo.VimeoClient(
    token=os.getenv("TOKEN"),
    key=os.getenv("KEY"),
    secret=os.getenv("SECRET")
)

def add_chapter_title(video_id, title, timecode):

    print(f"Add Chapter: {video_id}, {title}, {timecode}")
    # Make the API call to vimeo
    response = client.post(f"/videos/{video_id}/chapters",
                       data = {
                           "title": title,
                           "timecode": timecode
                       })


def upload():
    # Split the text into lines
    lines = chapterTitles_txt.get("1.0", "end").split("\n")
    # Get rid of extra trailing line
    lines.pop()

    diff_time = time(hour=0, minute=0, second=0)
    
    for index, line in enumerate(lines):
        print(f"Line: {line}")
        # Ignore first timestamp if we are converting (the "00:00 - Worship" timestamp)
        if (not convert_timestamps.get()) or (convert_timestamps.get() and index != 0):
            print("Passed Check")
            # Split the line into the timestamp section and the title section: timestamp - title
            sections = line.split("-")

            # Strip whitespace from sections (mainly spaces before/after)
            for i, section in enumerate(sections):
                sections[i] = section.strip()

            # Read and format the timestamp
            timestamp = 0
            format = ""
            if(sections[0].count(":") == 2):
                format = "%H:%M:%S"
            else:
                format = "%M:%S"

            timestamp = datetime.strptime(sections[0], format)

            # Set the difference between YT and Vimeo timestamps if we are converting timestamps
            if convert_timestamps.get() and index == 1:
                diff_time = timestamp

            # Apply the difference
            timestamp = timestamp - timedelta(minutes=diff_time.minute, seconds=diff_time.second)

            # Convert to seconds for vimeo
            timestamp = timestamp.hour * 3600 + timestamp.minute * 60 + timestamp.second

            add_chapter_title(video_id.get(), sections[1], timestamp)



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
convert_timestamps.set(False)
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