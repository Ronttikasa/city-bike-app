from . import db

class Station(db.Model):
    __tablename__ = 'stations'

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    fi_name = db.Column(
        db.String(64),
        unique=True,
        nullable=False
    )

    def __init__(self, fi_name):
        self.fi_name = fi_name
    

