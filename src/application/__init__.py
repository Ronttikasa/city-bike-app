from flask import Flask

def init_app():
    """Initialize the application"""
    app = Flask(__name__)

    with app.app_context():
        from . import routes
        return app

