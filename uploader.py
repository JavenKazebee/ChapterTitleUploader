import vimeo
import sys
from tkinter import *

# Create the API client
client = vimeo.VimeoClient(
    token='c93bc5b483b3e7db712c7924d1b39464',
    key='bc833cfdbd7c734a2a5b47053686914cf1c34b59',
    secret='a0cxBXh+bk51oFqxVwT5g7iN+BTY3u3MaREHh2ZrkHrLTRxpXQulQjk8QgSHqQUt6EnxvQ+ly2vctss0JA0jfuWRYCB7OoE1a/IDC5UfWWwV0rCwjvqafeIE9RtdO8ly'
)


# Create UI
root = Tk()




print(f"Video ID: {video_ID}")
print(f"Chapter Titles: {yt_timecodes}")


# Make the API call to vimeo
# response = client.post("/videos/933067303/chapters",
#                        data = {
#                            "title": "Timecode Test 2",
#                            "timecode": 2
#                        })

# print(response.json())