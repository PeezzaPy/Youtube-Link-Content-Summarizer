from flask import Flask
from .blueprints.home import home
from .blueprints.get_started import get_started
from .blueprints.summary import summary

# Register app route
def create_app():
    app = Flask(__name__)
    app.register_blueprint(home)
    app.register_blueprint(get_started)
    app.register_blueprint(summary)

    return app