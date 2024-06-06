from flask import Flask
from .blueprints.get_started import get_started
from .blueprints.summary import summary
from .blueprints.about import about
from .blueprints.home import home

# Register app route
def create_app():
    app = Flask(__name__)
    app.secret_key = 'secret-key'
    app.register_blueprint(home)
    app.register_blueprint(about)
    app.register_blueprint(get_started)
    app.register_blueprint(summary)

    return app