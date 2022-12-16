from .. import db

class CityBikeRepository:
    """A class for interacting with the database"""

    def __init__(self, database=db):
        self.db = database

    def get_all_stations(self):
        sql = """SELECT "FID", "ID", "Nimi", "Osoite", "Kaupunki" FROM stations"""
        return self.db.session.execute(sql).fetchall()

citybike_repo = CityBikeRepository()

        