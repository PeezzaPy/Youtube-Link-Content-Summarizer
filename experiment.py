from urllib.parse import urlparse

url = "https://www.youube.com/watch?v=wa6OuirfOsU&ab_channel=ENHYPEN"
# Parse the url
parsed_url = urlparse(url)

# Check if the URL is a valid youtube video link
if parsed_url.netloc not in ('www.youtube.com', 'youtube.com', 'youtu.be'):
    print('Not a valid YouTube URL')
else:
    print("valid URL")