from flask import render_template, redirect, request
from flask import current_app as app
from .services.journey_service import journey_service


@app.route("/journeys", methods=["GET"])
def journeys():
    """Show list of journeys 50 at a time.
    """
    page = int(request.args.get("page", 1))
    show = 50
    offset = (page - 1) * show
    journeys_to_show = journey_service.get_journeys(show, offset)
    return render_template("journeys.html", journeys=journeys_to_show, page=page)

@app.route("/station/<int:station_id>", methods=["GET"])
def show_station(station_id):
    """Show the single station view.
    """
    station = journey_service.get_station_data(station_id)
    return render_template("station.html", **station)

@app.route("/stations", methods=["GET"])
def stations():
    """Show list of stations 50 at a time.
    """
    page = int(request.args.get("page", 1))
    show = 50
    offset = (page - 1) * show
    stations_to_show = journey_service.get_stations(show, offset)
    return render_template("stations.html", stations=stations_to_show, page=page)

@app.route("/", methods=["GET"])
def index():
    """Trigger dataset import, redirects to stations view.
    """
    journey_service.import_stations()
    files = ["2021-05.csv", "2021-06.csv", "2021-07.csv"]
    journey_service.import_journeys(files)
    return redirect("/stations")
