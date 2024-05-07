from youtube_transcript_api import YouTubeTranscriptApi

# Parse and get the video ID
def get_video_id(url):
    # Identifier for youtube video url
    if "https://www.youtube.com/watch?v=" in url:
        start_pos = url.find("https://www.youtube.com/watch?v=")
        end_pos = url.find("&ab_channel=")
        if start_pos == -1 or end_pos == -1:
            print("Not a valid youtube video link")
            return None
        video_id = url[start_pos + len("https://www.youtube.com/watch?v="):end_pos]
    elif "https://youtu.be/" in url:
        start_pos = url.find("https://youtu.be/")
        video_id = url[start_pos + len("https://youtu.be/"):]
    else:
        print("Not a valid youtube video link")
        return None

    print("Video ID: ", video_id)
    return video_id


# Get transcript only from dict object
def get_transcript(video_id):
    all_text = ""   # store all text from transcript
    transcript = YouTubeTranscriptApi.get_transcript(video_id)
    print(transcript)
    
    # Parse the text only
    for item in transcript:
        all_text += item['text'] + " "

    # Remove new line (due to video subtitles positioning)
    all_text = all_text.replace("\n", " ")

    print(all_text)

    return all_text
