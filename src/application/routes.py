from flask import make_response, render_template, redirect
from flask import current_app as app
from .services.import_stations import import_stations
from .services.journey_service import journey_service
from .repositories.city_bike_repository import citybike_repo

@app.route("/add-stations", methods=["GET"])
def add_stations():
    import_stations()
    return redirect("/stations")

@app.route("/add-journeys", methods=["GET"])
def add_journeys():
    files = ["2021-05.csv", "2021-06.csv", "2021-07.csv"]
    for file in files:
        journey_service.import_journeys(file)
    return redirect("/journeys")

@app.route("/journeys", methods=["GET"])
def journeys():
    journeys = journey_service.show_journeys()
    return render_template("journeys.html", journeys=journeys)

@app.route("/station/<int:id>", methods=["GET"])
def station(id):
    station = journey_service.get_station_data(id)
    return render_template("station.html", **station)

@app.route("/stations", methods=["GET"])
def stations():
    stations = citybike_repo.get_all_stations()
    return render_template("index.html", stations=stations)

@app.route("/", methods=["GET"])
def index():
    return redirect("/stations")     
