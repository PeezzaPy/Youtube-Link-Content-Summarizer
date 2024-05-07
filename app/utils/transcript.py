from youtube_transcript_api import YouTubeTranscriptApi

# Parse and get the video ID
def get_video_id(url):
    # Identifier for youtube video url
    if "youtube.com/watch?v=" in url:
        start_pos = url.find("youtube.com/watch?v=")
        end_pos = url.find("&")
        video_id = url[start_pos + len("youtube.com/watch?v="):end_pos]
    elif "youtu.be" in url:
        start_pos = url.find("youtu.be/")
        end_pos = url.find("?")
        video_id = url[start_pos + len("youtu.be/"):end_pos]

    if start_pos == -1 or end_pos == -1:
        print("Not a valid youtube video link")
        return None

    return video_id


# Get transcript only from dict object
def get_transcript(video_id):
    all_text = ""   # store all text from transcript
    transcript = YouTubeTranscriptApi.get_transcript(video_id)
    
    # Parse the text only
    for item in transcript:
        all_text += item['text'] + " "

    # Remove new line (due to video subtitles positioning)
    all_text = all_text.replace("\n", " ")

    return all_text
