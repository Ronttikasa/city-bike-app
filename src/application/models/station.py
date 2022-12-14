from sqlalchemy import MetaData
from sqlalchemy.ext.automap import automap_base
from .. import db

metadata = MetaData()

metadata.reflect(db.engine)

Base = automap_base(metadata=metadata)
Base.prepare()

Station = Base.classes.stations

# class Station(db.Model):
#     __tablename__ = 'stations'

#     id = db.Column(
#         db.Integer,
#         primary_key=True
#     )

#     station_id = db.Column(
#         db.Integer,
#         unique=True,
#         nullable=False
#     )

#     name_fi = db.Column(
#         db.String(64),
#         unique=True,
#         nullable=False
#     )

#     name_se = db.Column(
#         db.String(64),
#         unique=True,
#         nullable=False
#     )

#     name_en = db.Column(
#         db.String(64),
#         unique=True,
#         nullable=False
#     )

#     address_fi = db.Column(
#         db.String(64),
#         unique=False,
#         nullable=False
#     )

#     address_se = db.Column(
#         db.String(64),
#         unique=False,
#         nullable=True
#     )

#     city_fi = db.Column(
#         db.String(32),
#         unique=False,
#         nullable=True
#     )

#     operator = db.Column(
#         db.String(64),
#         unique=False,
#         nullable=True
#     )

#     capacity = db.Column(
#         db.Integer,
#         unique=False,
#         nullable=False
#     )

#     longitude = db.Column(
#         db.Float,
#         unique=False,
#         nullable=False
#     )

#     latitude = db.Column(
#         db.Float,
#         unique=False,
#         nullable=False
#     )

#     def __init__(self, station_id, name_fi, name_se, name_en,
#                 address_fi, address_se, city_fi, operator,
#                 capacity, longitude, latitude):
#         self.station_id = station_id
#         self.name_fi = name_fi
#         self.name_se = name_se
#         self.name_en = name_en
#         self.address_fi = address_fi
#         self.address_se = address_se
#         self.city_fi = city_fi
#         self.operator = operator
#         self.capacity = capacity
#         self.longitude = longitude
#         self.latitude = latitude
    

