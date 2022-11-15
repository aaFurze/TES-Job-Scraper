import unittest
import asyncio

from src.scrapers import get_jobs_json, _get_response_object, httpx
from src.choose_filters import FilterCreator

class TestGetJobsJson(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        dummy_filter = FilterCreator(None)
        dummy_filter.lat = 50.24
        dummy_filter.long = -5.6
        dummy_filter.distance = 3
        dummy_filter.workplaces = []
        dummy_filter.positions = []
        dummy_filter.subjects = []
        dummy_filter.no_pages = 3 


        cls.response_object_output = asyncio.run(_get_response_object(dummy_filter))
        cls.get_jobs_output = get_jobs_json(dummy_filter)


    def test_get_response_object_returns_list(self):
        self.assertIsInstance(self.response_object_output, list)

    def test_reponse_object_output_contains_item(self):
        self.assertGreater(len(self.response_object_output), 0)
    
    def test_response_object_output_contains_reponse(self):
        self.assertIsInstance(self.response_object_output[0], httpx.Response)  
    
    def test_status_code(self):
        self.assertEqual(self.response_object_output[0].status_code, 200)

    def test_get_jobs_json_returns_list(self):
        self.assertIsInstance(self.get_jobs_output, list)
    
    def test_get_jobs_json_contains_dict(self):
        self.assertIsInstance(self.get_jobs_output[0], dict)

    def test_get_jobs_output_dict_has_title(self):
        self.assertIn("title", list(self.get_jobs_output[0].keys()))

