from flask import Flask
from .blueprints.about_us import about_us

def create_app():
    app = Flask(__name__)
    app.register_blueprint(about_us)
    return app