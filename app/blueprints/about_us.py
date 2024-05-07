from flask import Blueprint, render_template

# Create a blueprint for the home page
about_us = Blueprint('about_us', __name__)

@about_us.route('/about-us')
def about_us_page():
    return render_template('about_us.html')