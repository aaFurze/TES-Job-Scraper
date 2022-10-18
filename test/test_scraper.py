import unittest

from src.scraper import get_jobs_json, _get_response_object

class TestGetJobsJson(unittest.TestCase):
    def test_url_ending(self):
        self.assertEqual(_get_response_object().url[-1], "&")
    
    def test_status_code(self):
        self.assertEqual(_get_response_object().status_code, 200)

    def test_is_dict(self):
        self.assertIsInstance(get_jobs_json(), dict)
