import os
import pandas as pd
from .. import db
from ..repositories.city_bike_repository import citybike_repo

class JourneyService:
    def __init__(self, repository=citybike_repo):
        self.repo = repository

    def import_journeys(self, filename):
        """Import journey data from csv file"""
        dirname = os.path.dirname(__file__)
        data_file_path = os.path.join(dirname, "..", "..", "..", "data", filename)
        df = pd.read_csv(data_file_path)

        if not df.empty:
            df.rename(
                columns={"Covered distance (m)": "Distance", "Duration (sec.)": "Duration"},
                inplace=True)
            df.drop(columns=["Departure station name", "Return station name"], inplace=True)

            index_filter = df[(df["Distance"] < 10) | (df["Duration"] < 10)].index
            df.drop(index_filter, inplace=True)

            df.to_sql(
                "journeys",
                db.engine,
                index=False,
                chunksize=10000,
                if_exists="append")
            return True
        return False

    def show_journeys(self):
        """Return the journeys in database.
        """
        return self.repo.get_journeys()

    def get_station_data(self, station_id):
        """Fetch station data.

        Returns:
           Object with station data 
        """

        result = {}
        result["station"] = self.repo.get_station_info(station_id)
        result["departures"] = self.repo.get_number_of_departing_journeys(station_id)
        result["returns"] = self.repo.get_number_of_returning_journeys(station_id)
        result["top5_return_stations"] = self.repo.get_top_return_stations(station_id)
        result["top5_departure_stations"] = self.repo.get_top_departure_stations(station_id)

        return result


journey_service = JourneyService()
