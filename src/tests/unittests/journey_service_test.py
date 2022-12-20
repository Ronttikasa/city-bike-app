import unittest
from unittest.mock import Mock
from ...application.services.journey_service import JourneyService

class TestJourneyService(unittest.TestCase):
    def setUp(self):
        self.repo = Mock()
        self.svc = JourneyService(self.repo)

    def test_show_journeys(self):
        self.repo.get_journeys.return_value = {}
        result = self.svc.show_journeys()
        self.assertEqual(result, {})