from flask import Flask
from .blueprints.get_started import get_started

# Register app route
def create_app():
    app = Flask(__name__)
    app.register_blueprint(get_started)
    return app