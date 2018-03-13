# Dependencies
import json
import os

# Create file path
json_path = os.path.join('..', 'Resources', 'youtube_response.json')

# Open .json file
with open(json_path, 'r') as json_file:
    # Parse the json file using json.load()
    video_json = json.load(json_file)

# Isolate "data items" for easy reading
data = video_json["data"]
data_items = data["items"]

# Retrieve the video's title
title = data_items[0]["title"]
print("Title: ", title)

# Retrieve the video's rating
rating = data_items[0]["rating"]
print("Rating:", rating)

# Retrieve the link to the video's default thumbnail
default_thumbnail = data_items[0]["thumbnail"]["default"]
print("Thumbnail: ", default_thumbnail)

# Retrieve the number of views this video has
view_count = data_items[0]["viewCount"]
print("View count:", view_count)
