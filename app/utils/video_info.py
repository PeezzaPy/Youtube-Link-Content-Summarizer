from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api import TranscriptsDisabled
from googleapiclient.discovery import build
from .json_handler import *
import re

# Parse and get the video ID
def get_video_id(url):
    # Identifier for youtube video url
    if "youtube.com/watch?v=" in url:
        start_pos = url.find("youtube.com/watch?v=")
        end_pos = url.find("&")
        if end_pos == -1:
            end_pos = len(url)
        video_id = url[start_pos + len("youtube.com/watch?v="):end_pos]
    elif "youtu.be" in url:
        start_pos = url.find("youtu.be/")
        end_pos = url.find("?")
        if end_pos == -1:
            end_pos = len(url)
        video_id = url[start_pos + len("youtu.be/"):end_pos]

    if start_pos == -1 or end_pos == -1:
        print("Not a valid youtube video link")
        return None

    return video_id


# Get transcript only from dict object
def get_transcript(video_id):
    all_text = ""   # store all text from transcript
    try:
        transcript = YouTubeTranscriptApi.get_transcript(video_id)

        # Parse the text only
        for item in transcript:
            all_text += item['text'] + " "

        # Remove new line (due to video subtitles positioning)
        all_text = all_text.replace("\n", " ")

        return all_text
    except TranscriptsDisabled:
        return None


# Preprocess string from transcript
def clean_text(text):
    # Remove special characters
    text = re.sub(r'\W', ' ', text)

    # Remove single characters left as a result of removing special characters
    text = re.sub(r'\s+[a-zA-Z]\s+', ' ', text)

    # Remove single characters from the start
    text = re.sub(r'\^[a-zA-Z]\s+', ' ', text)

    # Substitute multiple spaces with single space
    text = re.sub(r'\s+', ' ', text, flags=re.I)
    
    # Convert to lowercase
    text = text.lower()

    return text


# Get video info
def get_video_info(video_id):
    # Load api key
    api_key = get_api_key()
    youtube = build('youtube', 'v3', developerKey=api_key)
    
    request = youtube.videos().list(
        part="snippet",
        id=video_id
    )
    response = request.execute()

    id = response['items'][0]['id']
    title = response['items'][0]['snippet']['title']
    publish_date = response['items'][0]['snippet']['publishedAt']
    make_yt_info_json(response, id)
    
    print_video_info(title, publish_date)

    return title, publish_date


# Logging data
def print_video_info(title, publish_date):
    print(f"Title: {title}")
    print(f"Published Date: {publish_date}")