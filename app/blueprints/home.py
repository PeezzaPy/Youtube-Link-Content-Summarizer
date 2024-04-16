from flask import Blueprint, render_template

# Create a blueprint for the home page
home = Blueprint('home', __name__)

@home.route('/')
def home_page():
    my_name = "John Patrick"
    return render_template('home.html', username=my_name)