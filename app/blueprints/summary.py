from flask import Blueprint, render_template, request
from ..utils.video_info import *
from ..utils.summarizer import * 

# Create a blueprint for the home page
summary = Blueprint('summary', __name__)

@summary.route('/summary', methods=['POST', 'GET'])
def summary_page():
    # Log routing
    log_routing(request)

    summary = []        # empty list to store the summary state
    if request.method == 'POST': 
        link = request.form.get('yt-link')
        if link:
            video_id = get_video_id(link)
            title, publish_date = get_video_info(video_id)
            transcript = get_transcript(video_id)

            if transcript:    
                # NLP for summarization
                word_list = token(transcript)
                print(f"Word List: {word_list}")
                sent_list = sent_token(transcript)
                print(f"Sentence List: {sent_list}")
                filtered_words = remove_stopwords(word_list)
                print(f"Filtered Words: {filtered_words}")
                word_frequency = word_freq(filtered_words)
                word_frequency = max_freq(word_frequency)
                print(f"Word Frequency: {word_frequency}")
                sent_scores = sentence_scores(sent_list, word_frequency)
                print(f"Sentence Scores: {sent_scores}")
                summary = get_summary(sent_scores)
                print(f"Summary: {summary}")
            else:
                summary.append('TRANSCRIPT NOT AVAILABLE')
        else:
            summary.append('INPUT MUST NOT BE EMPTY')

    return render_template('summary.html', summary=summary)


def log_routing(request):
    print("Route: ", request.path)
    print("Method: ", request.method)