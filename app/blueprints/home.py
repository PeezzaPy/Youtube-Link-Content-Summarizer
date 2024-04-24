from flask import Blueprint, render_template
from ..utils.transcript import get_transcript

# Create a blueprint for the home page
home = Blueprint('home', __name__)

@home.route('/')
def home_page():
    # video_id = "rFltDd3Iab4"
    # transcript = get_transcript(video_id=video_id)
    return render_template('home.html')