import json

# # Create json format of youtube link video info
# def make_yt_info_json(response, video_id):
#     filename = f'json_yt_info/{video_id}.json'
#     with open(filename, 'w') as f:
#         json.dump(response, f, indent=4)

#     with open(filename, 'r') as f:
#         file_content = json.load(f)

#     if file_content == response:
#         print(f"Checksum passed {filename}")
#     else:
#         print(f"Checksum failed {filename}")


# Retrieve youtube api key
def get_api_key():
    with open('config.json') as f:
        data = json.load(f)
    return data['YOUTUBE_API_KEY']