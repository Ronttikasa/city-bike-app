from flask import Markup
from flask import current_app as app

@app.route("/")
def hello_world():
    return Markup("<i>Hello world!</i>")