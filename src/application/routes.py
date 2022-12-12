from flask import Markup, request, make_response
from flask import current_app as app
from .models import db, Station

@app.route('/', methods=['GET'])
def stations():
    """Create a station via query string parameters."""
    name = request.args.get('name')
    if name:
        new_station = Station(
            fi_name=name
        )
        db.session.add(new_station)  # Adds new User record to database
        db.session.commit()  # Commits all changes
    return make_response(f"{name} successfully created!")