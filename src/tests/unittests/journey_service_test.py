import unittest
from unittest.mock import Mock
from ...application.services.journey_service import JourneyService

class TestJourneyService(unittest.TestCase):
    def setUp(self):
        self.repo = Mock()
        self.svc = JourneyService(self.repo)

    def test_get_journeys(self):
        self.repo.get_journeys.return_value = {}
        limit, offset = 50, 100
        result = self.svc.get_journeys(limit, offset)
        self.assertEqual(result, {})
        self.repo.get_journeys.assert_called_with(limit, offset)

    def test_get_stations(self):
        self.repo.get_stations.return_value = {}
        limit, offset = 10, 0
        result = self.svc.get_stations(limit, offset)
        self.assertEqual(result, {})
        self.repo.get_stations.assert_called_with(limit, offset)

    def test_station_data(self):
        station = [50, "Kuusisaari"]
        departures = 1200
        returns = 1100
        ret_stations = ["top", "5", "return", "station", "names"]
        dep_stations = ["top", "5", "departure", "station", "names"]
        self.repo.get_station_info.return_value = station
        self.repo.get_number_of_departing_journeys.return_value = departures
        self.repo.get_number_of_returning_journeys.return_value = returns
        self.repo.get_top_return_stations.return_value = ret_stations
        self.repo.get_top_departure_stations.return_value = dep_stations

        result = self.svc.get_station_data(50)
        self.repo.get_station_info.assert_called_with(50)
        self.assertEqual(result["returns"], returns)