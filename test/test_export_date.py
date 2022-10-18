import unittest
import datetime

from src.export_data import _get_current_timestamp


class TestTimeStampGeneration(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.current_time = datetime.datetime.now()
        cls.test_timestamp = _get_current_timestamp()

    def test_timestamp_length(self):
        self.assertEqual(len(__class__.test_timestamp), 15)
    
    def test_year(self):
        self.assertEqual(self.current_time.strftime("%Y"), self.test_timestamp[:4])
    
    def test_month(self):
        self.assertEqual(self.current_time.strftime("%m"), self.test_timestamp[4:6])
    
    def test_day(self):
        self.assertEqual(self.current_time.strftime("%d"), self.test_timestamp[6:8])
    
    def test_hour(self):
        self.assertEqual(self.current_time.strftime("%H"), self.test_timestamp[9:11])
    
    def test_minute(self):
        self.assertEqual(self.current_time.strftime("%M"), self.test_timestamp[11:13])
