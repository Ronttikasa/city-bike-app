from flask import render_template, redirect, request
from flask import current_app as app
from .services.import_stations import import_stations
from .services.journey_service import journey_service

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
    page = int(request.args.get("page", 1))
    journeys_to_show = 50
    offset = (page - 1) * journeys_to_show
    journeys = journey_service.get_journeys(journeys_to_show, offset)
    return render_template("journeys.html", journeys=journeys, page=page)

@app.route("/station/<int:id>", methods=["GET"])
def station(id):
    station = journey_service.get_station_data(id)
    return render_template("station.html", **station)

@app.route("/stations", methods=["GET"])
def stations():
    page = int(request.args.get("page", 1))
    show = 50
    offset = (page - 1) * show
    stations = journey_service.get_stations(show, offset)
    return render_template("stations.html", stations=stations, page=page)

@app.route("/", methods=["GET"])
def index():
    return redirect("/stations")     
