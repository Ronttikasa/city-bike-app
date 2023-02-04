import os
import pandas as pd
from ..repositories.city_bike_repository import citybike_repo

class JourneyService:
    """Application logic class that handles the front-end requests.
    """
    def __init__(self, repository=citybike_repo):
        self.repo = repository

    def import_journeys(self, filenames):
        """Import journey data from csv files to database

        Args: list of filenames

        Returns: bool
        """
        if self.repo.table_exists("journeys"):
            return False

        for filename in filenames:
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

                self.repo.import_journeys(df)
        return True

    def import_stations(self):
        """Import station data from csv to database
        """
        if self.repo.table_exists("stations"):
            return False

        dirname = os.path.dirname(__file__)
        data_file_path = os.path.join(dirname, "..", "..", "..", "data",
        "Helsingin_ja_Espoon_kaupunkipyöräasemat_avoin.csv")

        df = pd.read_csv(data_file_path)
        df.loc[df["Kaupunki"] == " ", "Kaupunki"] = "Helsinki"

        if not df.empty:
            self.repo.import_stations(df)
        return True

    def get_journeys(self, limit, offset):
        """Fetch journeys from database.

        Args:
            limit (int): Number of journeys to get
            offset (int): Offset from start of db table

        Returns:
            List of objects containing the journey data
        """
        return self.repo.get_journeys(limit, offset)

    def get_stations(self, limit, offset):
        """Fetch stations from database.

        Args:
            limit (int): Number of stations to get
            offset (int): Offset from start of db table

        Returns:
            List of objects containing station data
        """
        return self.repo.get_stations(limit, offset)

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
