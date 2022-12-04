import difflib
from typing import List, Union

from .scrapers import get_location_data_json


valid_distances = [3, 5, 10, 15, 20, 30, 50, 70, 100, 500]
valid_workplaces = ["Secondary", "Primary", "Special Education", "Further Education", "Independent Senior"]
valid_positions = ["Teaching and Lecturing", "Leadership", "Non-Teaching/Support"]
valid_subjects = ["Science", "Mathematics", "English", "Special Needs", "Physical Education", "Information Technology",
    "Design and Technology", "Modern Languages", "Physics", "Chemistry", "Biology", "Art and Design",
    "Food Technolgy/Hospitality and Catering", "Music", "Performing Arts", "Computer Science"]



class UserPreferenceStrings:
    def __init__(self) -> None:
        self.location: str
        self.distance: str
        self.workplaces: str
        self.positions: str
        self.subjects: str
        self.no_pages: str

    def prompt_for_user_preferences(self):
        self.location = self.clean_user_input(input("Enter the county, city or town which you would like to find jobs around.\n"))
        self.distance = self.clean_user_input_numeric(input(self._generate_text_list("""Select the radius (in miles) around which you would like to search for jobs (Select from the values specified below).""", valid_distances)))
        self.workplaces = self.clean_user_input(input(self._generate_text_list("""Select the workplace numbers that you would like to search for jobs for. Separate choices with commas (,)""", valid_workplaces)))
        self.positions = self.clean_user_input(input(self._generate_text_list("""Select the position numbers you would like to search jobs for. Separate choices with commas (,)""", valid_positions)))
        self.subjects = self.clean_user_input(input(self._generate_text_list("""Select the subjects you would like to search for jobs for. Separate choices with commas (,)""", valid_subjects)))
        self.no_pages = self.clean_user_input_numeric(input("Enter the maximum number of pages of results you would like to scrape (page size is 20, default number of pages is 3)\n"))
    
    @staticmethod
    def clean_user_input(val: str) -> str:
        val = val.lower().strip()
        return val

    @staticmethod
    def clean_user_input_numeric(val: str) -> Union[int, float]:
        val = val.strip()
        num_str = ""

        for char in val:
            if char.isnumeric() or char == ".":
                num_str += char
        
        # Makes TES Scraper default to searching in a radius of 10 miles, and retrieve a maximum of 60 job postings (3 pages results).
        if len(num_str) == 0 or num_str == ".": return 3

        if num_str.find("."):
            return float(num_str)
        return int(num_str)
    

    @staticmethod
    def _generate_text_list(prompt_body: str, choices: list) -> str:
        """
        Used to generate a padded string for the user prompt options.
        If a choice is too long, it will cause the following prompt (if it is on the same line) to be out of kilter compared to 
        other options.    
        """

        output = prompt_body

        for i, choice in enumerate(choices):
            if i % 2 == 0:
                 output += "\n"
            else:
                output += "".ljust(max(40 - (len(str(choices[i - 1])) + 2 + len(str(i))), 4))
            output += f"{i + 1}. {choice}"
        return output + "\n"
        


class FilterCreator:
    def __init__(self, user_preferences_input: UserPreferenceStrings, setup_on_init: bool = False) -> None:
        self.user_preferences_input = user_preferences_input
        self.lat: float
        self.long: float
        self.distance: int
        self.workplaces: List[str]
        self.positions: List[str]
        self.subjects: List[str]

        if setup_on_init: self.create_filter_values(**self.user_preferences_input.__dict__)


    # Call to setup the filter.
    def create_filter_values(self, location: str, distance: str, positions: str, workplaces: str, subjects: str, no_pages: str):
        self.lat, self.long = self.get_location_coordinates(location)
        self.distance = self.get_distance_value(distance)
        self.positions = self._get_values_from_list(positions, valid_positions)
        self.workplaces = self._get_values_from_list(workplaces, valid_workplaces)
        self.subjects = self._get_values_from_list(subjects, valid_subjects)
        self.no_pages = self._get_no_pages_value(no_pages)
    
    def get_location_coordinates(self, location: str) -> List[float]:
        locations_data = get_location_data_json(location)
        closest_match = None
        highscore = 0
        for location_data in locations_data:
            if location_data["country"] != "GB": continue
            match = difflib.SequenceMatcher(None , location_data["name"].lower(), location)
            match_score = match.ratio()
            if location_data["name"].find(location) == 0: match_score *= 1.25

            if match_score > highscore: 
                closest_match = location_data
                highscore = match_score
            
            if match_score >= 0.99: break
        
        if not closest_match: return None
        latlon = closest_match["latlon"]
        return latlon[0], latlon[1]
    
    def get_distance_value(self, distance: int) -> int:
        if distance > 10: return 10
        if distance < 0: return 0
        return int(distance)
    
    @staticmethod
    def _get_values_from_list(input_values: str, check_against_values: List[str]) -> List[str]:
        values = [val.strip() for val in input_values.split(",")]

        output = []

        for pos_num in values:
            if not pos_num.isnumeric():
                continue
            pos_index = int(pos_num) - 1
            
            if pos_index >= len(check_against_values) or pos_index < 0: continue

            output.append(check_against_values[pos_index])
        
        if len(output) == 0: return None
        return output     


    @staticmethod
    def _get_no_pages_value(value: Union[float, int]) -> int:
        if value < 1:
            return 5
        return int(value)
