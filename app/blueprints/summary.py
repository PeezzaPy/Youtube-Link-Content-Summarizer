from flask import Blueprint, render_template, request
from ..utils.transcript import *
from ..utils.summarizer import * 

# Create a blueprint for the home page
summary = Blueprint('summary', __name__)

@summary.route('/summary', methods=['POST', 'GET'])
def summarize_page():
    # Log routing
    log_routing(request)

    summary = []        # empty list to store the summary state
    if request.method == 'POST': 
        link = request.form.get('yt-link')
        print("Link: ", link)
        if link:
            video_id = get_video_id(link)
            print("Vi: ", video_id)
            transcript = get_transcript(video_id)
            summary = transcript
            # NLP for summarization
            '''word_list = token(transcript)
            print("Word List: ", word_list)
            sent_list = sent_token(transcript)
            print("Sent List: ", sent_list)
            filtered_words = remove_stopwords(word_list)
            print("Filtered Words: ", filtered_words)
            word_frequency = word_freq(filtered_words)
            print("Word Frequency: ", word_frequency)
            word_frequency = max_freq(word_frequency)
            print("Word Frequency: ", word_frequency)
            sent_scores = sentence_scores(sent_list, word_frequency)
            print("Sent Scores: ", sent_scores)
            summary = get_summary(sent_scores)
            print("Summary: ", summary)'''
            
        else:
            summary.append('INPUT MUST NOT BE EMPTY')

    return render_template('summary.html', summary=summary)


def log_routing(request):
    print("Route: ", request.path)
    print("Method: ", request.method)