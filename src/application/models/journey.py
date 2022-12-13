from .. import db

class Journey(db.Model):
    __tablename__ = 'journeys'

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    departure_station = db.Column(
        db.Integer,
        db.ForeignKey('stations.station_id'),
        unique=False,
        nullable=False
    )

    return_station = db.Column(
        db.Integer,
        db.ForeignKey('stations.station_id'),
        unique=False,
        nullable=False
    )

    departure_time = db.Column(
        db.DateTime,
        unique=False,
        nullable=False
    )

    return_time = db.Column(
        db.DateTime,
        unique=False,
        nullable=False
    )

    distance = db.Column(
        db.Integer,
        unique=False,
        nullable=False
    )

    duration = db.Column(
        db.Integer,
        unique=False,
        nullable=False
    )

    def __init__(self, departure_station, return_station,
                departure_time, return_time, distance, duration):
        self.departure_station = departure_station
        self.return_station = return_station
        self.departure_time = departure_time
        self.return_time = return_time
        self.distance = distance
        self.duration = duration