from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# from .models.station import Station
# from .models.journey import Journey

def init_app():
    """Initialize the application"""
    app = Flask(__name__)

    app.config.from_pyfile('config.py')
    db.init_app(app)

    with app.app_context():
        from . import routes
        db.create_all()
        return app

