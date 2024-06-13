from flask import Blueprint, render_template, session

get_started = Blueprint('get_started', __name__)

@get_started.route("/get_started")
def get_started_page():
    return render_template('get_started.html')