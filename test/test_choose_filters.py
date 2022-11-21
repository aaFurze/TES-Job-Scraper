import unittest
from src.choose_filters import UserPreferenceStrings


class TestUserPreferenceStrings(unittest.TestCase):
    def test_clean_user_input(self):
        self.assertEqual(UserPreferenceStrings.clean_user_input("  TEST STRING          "), "test string")
    
    def test_clean_user_input_numeric_float(self):
        self.assertEqual(UserPreferenceStrings.clean_user_input_numeric(" 56.43sd   "), 56.43)

    def test_clean_user_input_numeric_int(self):
        self.assertEqual(UserPreferenceStrings.clean_user_input_numeric(" as5656f   "), 5656)
    
    def test_clean_user_input_numeric_base_case(self):
        self.assertEqual(UserPreferenceStrings.clean_user_input_numeric(" ."), 3)
    
    def test__generate_text_list(self):
        self.assertGreater(UserPreferenceStrings._generate_text_list("Title", ["Option 1", "Option 2"]).find("1. Option 1        "),
        -1)
