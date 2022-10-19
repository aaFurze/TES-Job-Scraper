from tabnanny import check
from typing import Union, List


class ConstructURL:
    def __init__(self, lat: float, long: float, distance_val: int = 1, workplaces: Union[List[str], str] = None,
 positions: Union[List[str], str] = None, subjects: Union[List[str], str] = None):

        self.lat = lat
        self.long = long
        self.distance_val = distance_val

        self.workplaces = self._validate_list_value(workplaces)
        self.positions = self._validate_list_value(positions)
        self.subjects = self._validate_list_value(subjects)
        
        self.url = self.construct_url()
    

    def construct_url(self) -> str:
        url_start = "https://www.tes.com/api/jobs/browser/search-v3?siteCountry=gb&&"
        url_location = self._get_position_url(self.lat, self.long)
        url_distance = self._get_distance_url(self.distance_val)
        url_workplaces = self._get_url_part_from_list("workplaces", self.workplaces)
        url_positions = self._get_url_part_from_list("positions", self.positions)
        url_subjects = self._get_url_part_from_list("subjects", self.subjects)
        url = url_start + url_location + url_distance + url_workplaces + url_positions + url_subjects
        return url

    @staticmethod
    def _get_position_url(lat: float, long: float) -> str:
        return f"point={lat},{long}&"

    @staticmethod
    def _get_distance_url(distance_val: int) -> str:
        return f"maxdistance={distance_val}&"
    
    @staticmethod
    def _get_url_part_from_list(url_start: str, items: List[str]):
        if len(items) <= 0:
            return ""
        output = ""
        for val in items:
            output += f"{url_start}={val}&"

        return output
    

    def _validate_list_value(val: Union[List[str], str, None]) -> List[str]:
        if val is None:
            return []
        if type(val) is str:
            return [val]
        try: 
            check_iter = iter(val)
        except:
            raise ValueError(f"input val was not an iterable or a valid input type (object type = {val}")
        return val


example = """
https://www.tes.com/api/jobs/browser/search-v3?siteCountry=gb&&
displayLocation=Tadcaster&subjects=Science&
point=53.88474742131398,-1.2640495584698352&keywords=&maxdistance=5&
workplaces=Secondary&workplaces=Independent Senior&
positions=Teaching and Lecturing&positions=Teacher&subjects=Design and Technology
"""