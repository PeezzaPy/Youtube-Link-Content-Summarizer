from flask import Blueprint, render_template, request

about = Blueprint('about', __name__)

@about.route('/about')
def about_page():
    return render_template('about.html')