from .. import db

class CityBikeRepository:
    """A class for interacting with the database"""

    def __init__(self, database=db):
        self.db = database

    def get_all_stations(self):
        sql = """SELECT "FID", "ID", "Nimi", "Osoite", "Kaupunki" FROM stations"""
        return self.db.session.execute(sql).fetchall()

    def get_journeys(self):
        sql = """SELECT j."Departure", j."Return", s1."Nimi" AS "departure_station", s2."Nimi" AS "return_station", j."Distance", j."Duration"
            FROM journeys as j
            JOIN stations as s1 ON j."Departure station id"=s1."ID"
            JOIN stations as s2 ON j."Return station id"=s2."ID"
            LIMIT 10
            """
        return self.db.session.execute(sql).fetchall()

citybike_repo = CityBikeRepository()

        