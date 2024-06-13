from flask import Blueprint, render_template, session, request
from ..utils.summarizer_bart import * 
from ..utils.text_process import *
from ..utils.video_info import *
import pyperclip
import os

# Create a blueprint for the home page
summary = Blueprint('summary', __name__)

# Global variables
downloads_folder = os.path.expanduser('~\\Downloads\\')     # get the downloads folder path
transcript = ''

@summary.route('/summary', methods=['POST', 'GET'])
def summary_page():
    global transcript

    # initialize
    transcript = '' 
    transcript_summary = ''
    video_id = ''
    video_title = ''
    publish_date = ''
    thumbnail = ''
    channel = ''
    views = ''
    data = {
        'summary': '',
        'thumbnail': '',
        'video_title': '',
        'video_date': '',
        'channel': '',
        'views': ''
    }

    # Log routing
    log_routing(request)

    if request.method == 'POST': 
        transcript = ''
        session.pop('data', None)
        link = request.form.get('yt-link')
        if link:
            video_id = get_video_id(link)

            if video_id == 'Invalid URL':
                transcript_summary += 'INVALID YOUTUBE URL'
                video_title, publish_date, thumbnail, channel, views = '', '', '', '', ''
            else:
                video_title, publish_date, thumbnail, channel, views = get_video_info(video_id)
                
                print(f"PUBLISHED DATE: {publish_date}")
                
                transcript = get_transcript(video_id)
                
                if transcript:    
                    transcript_summary = summarize_transcript(transcript)
                else:
                    transcript_summary += 'TRANSCRIPT NOT AVAILABLE'
        else:
            transcript_summary += 'INPUT MUST NOT BE EMPTY'

        if publish_date == '':
            data = {
                'summary': transcript_summary,
                'thumbnail': thumbnail,
                'video_title': video_title,
                'video_date': publish_date,
                'channel': channel,
                'views': views
            }
        else: 
            data = {
                'summary': transcript_summary,
                'thumbnail': thumbnail,
                'video_title': video_title,
                'video_date': publish_date.strftime('%Y-%m-%d'),
                'channel': channel,
                'views': views
            }

        # print("Data: ", data)

        session['data'] = data  # save data in session

    elif request.method == 'GET':
        data = session.get('data', {})  # retrieve data from session

    return render_template('summary.html', **data)



def get_unique_filename(path, filename):
    counter = 1
    filename_parts = os.path.splitext(filename)             # Separate the extension from the filename
    while os.path.exists(os.path.join(path, filename)):
        filename = f"{filename_parts[0]}({counter}){filename_parts[1]}"          # Append counter to filename
        counter += 1
    print(filename)
    return filename


# @summary.route('/summary/download_transcript')
# def download_transcript():
#     if transcript:
#         filename = get_unique_filename(downloads_folder, 'transcript.txt')
#         with open(os.path.join(downloads_folder, filename), 'w') as f:
#             f.write(str(transcript))
#         return 'Transcript downloaded successfully!'
#     else:
#         return 'Transcript not available for download'


@summary.route('/summary/download_summary')
def download_summary():
    data = session.get('data', {})  # retrieve data from session
    transcript_summary = data.get('summary', '')  # retrieve transcript_summary from data
    if transcript_summary:
        filename = get_unique_filename(downloads_folder, 'summary.txt')
        with open(os.path.join(downloads_folder, filename), 'w') as f:
            f.write(str(transcript_summary))
        return 'Summary downloaded successfully!'
    else:
        return 'Summary not available for download'


@summary.route('/summary/copy_summary')
def copy_summary():
    data = session.get('data', {})  # retrieve data from session
    transcript_summary = data.get('summary', '')  # retrieve transcript_summary from data
    if transcript_summary:
        pyperclip.copy(transcript_summary)
        return 'Summary copied successfully!'
    else:
        return 'Summary not available for copy to clipboard'

def log_routing(request):
    print("Route: ", request.path)
    print("Method: ", request.method)