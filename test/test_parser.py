from asyncio.format_helpers import extract_stack
from types import NoneType
import unittest

from src.parser import get_job_data_df, _create_empty_df, _extract_job_data, _populate_df_with_job_data


class TestDataframeCreation(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.df = _create_empty_df()

    def test_df_created(self):
        self.assertTrue(__class__.df is not None)
    
    def test_df_column_names(self):
        self.assertIn("employer_name", __class__.df.columns)
    
    def test_column_count(self):
        self.assertEqual(len(__class__.df.columns), 9)
    

class TestDataFramePopulating(unittest.TestCase):

    moc_row_1 = {"jobId": "12345", "title": "Teacher", "displayContractTerms": "Maternity",
     "displayJobStartDate": "As soon as possible", "advert": {"displayEndDateShort": "July 4th 2011"},
         "employerName": "St. Johns Academy ltd.", "displayLocation": "Kerry",
          "displaySalary": None, "jobPageCanonicalUrl": "https://fastapi.tiangolo.com/"}
    moc_row_2 = {"jobId": "1234", "title": "Teaching role", "displayContractTerms": "Permanent",
     "displayJobStartDate": "15th October 2016", "advert": {"displayEndDateShort": "November 5th 1605"},
         "employerName": "Mr Jones", "displayLocation": "Birmingham",
          "displaySalary": "£25,000-$3,5,0,0,0", "jobPageCanonicalUrl": "https://pytorch.org/docs/stable/index.html"}

    @classmethod
    def setUpClass(cls) -> None:
        df = _create_empty_df()
        cls.df = _populate_df_with_job_data(df, [__class__.moc_row_1, __class__.moc_row_2])

    def test_number_of_df_rows(self):
        self.assertEqual(len(__class__.df.index), 2)
    
    def test_insertion_order(self):
        self.assertEqual(__class__.df.iloc[0]["job_id"], "12345")
    
    def test_all_rows_populated(self):
        self.assertNotEqual(__class__.df.iloc[0]["job_id"], None)
        self.assertNotEqual(__class__.df.iloc[1]["job_id"], None)

    def test_extracting_data_order(self):
        extracted_data = _extract_job_data([__class__.moc_row_1])
        self.assertEqual(extracted_data[0][1], "Teacher")
    
    def test_extracting_data_count(self):
        extracted_data = _extract_job_data([__class__.moc_row_2])
        self.assertEqual(len(extracted_data), 1)
    