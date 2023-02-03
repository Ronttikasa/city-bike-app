from .. import db

class CityBikeRepository:
    """A class for interacting with the database"""

    def __init__(self, database=db):
        self.db = database

    def import_journeys(self, dataframe):
        """Import a pandas dataframe to the database.
        """
        dataframe.to_sql(
            "journeys",
            self.db.engine,
            index=False,
            chunksize=10000,
            if_exists="append")

    def import_stations(self, dataframe):
        """Import a pandas dataframe to the database
        """
        dataframe.to_sql(
            "stations",
            self.db.engine,
            index=False,
            if_exists="replace")

        sql = """ ALTER TABLE stations ADD PRIMARY KEY ("FID") """
        self.db.session.execute(sql)

    def get_stations(self, limit, offset):
        """Fetch stations from database.

        Args:
            limit: Number of stations to get
            offset: Offset from start of db table

        Returns:
            List of objects with fields FID, ID, Nimi, Osoite, Kaupunki
        """
        sql = """SELECT "FID", "ID", "Nimi", "Osoite", "Kaupunki"
            FROM stations
            LIMIT :limit
            OFFSET :offset"""
        return self.db.session.execute(sql, {"limit": limit, "offset": offset}).fetchall()

    def get_journeys(self, limit, offset):
        """Fetch all journeys in database.

        Args:
            limit: Number of journeys to get
            offset: Offset from start of db table

        Returns:
            List of objects with fields Departure, Return, departure_station, return_station, Distance, Duration
        """
        sql = """SELECT j."Departure", j."Return", j."Departure station id" AS "departure_id",
            s1."Nimi" AS "departure_station", j."Return station id" AS "return_id",
            s2."Nimi" AS "return_station", j."Distance", j."Duration"
            FROM journeys as j
            JOIN stations as s1 ON j."Departure station id"=s1."ID"
            JOIN stations as s2 ON j."Return station id"=s2."ID"
            LIMIT :limit
            OFFSET :offset
            """
        return self.db.session.execute(sql, {"limit": limit, "offset": offset}).fetchall()

    def get_station_info(self, station_id):
        """Fetch data for a single station view.
        """

        sql = """SELECT "FID", "ID", "Nimi", "Osoite", "Kaupunki" FROM stations WHERE "ID"=:id"""
        return self.db.session.execute(sql, {"id": station_id}).fetchone()

    def get_number_of_departing_journeys(self, station_id):
        """Count total number of journeys departing from the station
        """
        sql = """SELECT s."Nimi", COUNT(*), AVG(j."Distance")
            FROM stations AS s
            JOIN journeys AS j ON s."ID" = j."Departure station id"
            WHERE s."ID"=:id
            GROUP BY s."Nimi"
            """
        return self.db.session.execute(sql, {"id": station_id}).fetchone()

    def get_number_of_returning_journeys(self, station_id):
        """Count total number of journeys returning to the station
        """
        sql = """SELECT s."Nimi", COUNT(*), AVG(j."Distance")
            FROM stations AS s
            JOIN journeys AS j ON s."ID" = j."Return station id"
            WHERE s."ID"=:id
            GROUP BY s."Nimi"
            """
        return self.db.session.execute(sql, {"id": station_id}).fetchone()

    def get_top_return_stations(self, station_id):
        """Fetch top 5 return stations from given station.
        """
        sql = """SELECT s."Nimi", j."Return station id" AS return_station_id,
            s1."Nimi" AS return_station, count(j."Return station id")
            FROM stations AS s
            JOIN journeys AS j ON s."ID"=j."Departure station id"
            JOIN stations AS s1 ON j."Return station id"=s1."ID"
            WHERE s."ID"=:id
            GROUP BY s."Nimi", j."Return station id", s1."Nimi"
            ORDER BY count DESC
            LIMIT 5
            """
        return self.db.session.execute(sql, {"id": station_id}).fetchall()

    def get_top_departure_stations(self, station_id):
        """Fetch top 5 departure stations to given station.
        """
        sql = """SELECT s."Nimi", j."Departure station id" AS departure_station_id,
            s1."Nimi" AS departure_station, count(j."Departure station id")
            FROM stations AS s
            JOIN journeys AS j ON s."ID"=j."Return station id"
            JOIN stations AS s1 ON j."Departure station id"=s1."ID"
            WHERE s."ID"=:id
            GROUP BY s."Nimi", j."Departure station id", s1."Nimi"
            ORDER BY count DESC
            LIMIT 5
            """
        return self.db.session.execute(sql, {"id": station_id}).fetchall()



citybike_repo = CityBikeRepository()
