from flask import request, make_response
from flask import current_app as app
from . import db
from .services.import_stations import import_stations

@app.route('/', methods=['GET'])
def stations():
    # """Create a station via query string parameters."""
    # name = request.args.get('name')
    # if name:
    #     new_station = Station(
    #         name_fi=name
    #     )
    #     db.session.add(new_station)  # Adds new User record to database
    #     db.session.commit()  # Commits all changes
    # return make_response(f"{name} successfully created!")
    import_stations()
    return make_response("hurraa!")