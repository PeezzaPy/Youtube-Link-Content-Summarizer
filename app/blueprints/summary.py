from flask import Blueprint, render_template, request
from ..utils.video_info import *
from ..utils.summarizer_bart import * 
from ..utils.summarizer import * 

# Create a blueprint for the home page
summary = Blueprint('summary', __name__)

@summary.route('/summary', methods=['POST', 'GET'])
def summary_page():
    # Log routing
    log_routing(request)

    summary = ''        # empty list to store the summary state
    if request.method == 'POST': 
        link = request.form.get('yt-link')
        if link:
            video_id = get_video_id(link)
            video_title, publish_date, thumbnail, channel, views = get_video_info(video_id)
            transcript = get_transcript(video_id)

            if transcript:    
                summary = summarize_transcript(transcript)
            else:
                summary += 'TRANSCRIPT NOT AVAILABLE'
        else:
            summary += 'INPUT MUST NOT BE EMPTY'

    return render_template('summary.html', summary=summary, thumbnail=thumbnail, video_title=video_title, video_date=publish_date, channel=channel, views=views)


def log_routing(request):
    print("Route: ", request.path)
    print("Method: ", request.method)