# Dependencies
import json
import os

# Create file path
json_path = os.path.join('..', 'Resources', 'youtube_response.json')

# Open .json file
with open(json_path, 'r') as json_file:
    # Parse the json file using json.load()
    video_json = json.load(json_file)
