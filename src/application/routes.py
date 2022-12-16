from flask import request, make_response, render_template
from flask import current_app as app
from . import db
from .services.import_stations import import_stations
from .repositories.city_bike_repository import citybike_repo

@app.route('/', methods=['GET'])
def index():
    import_stations()
    stations = citybike_repo.get_all_stations()
    return render_template("index.html", stations=stations)