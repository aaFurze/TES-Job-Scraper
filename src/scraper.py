import re
import requests
import json


def get_jobs_json() -> dict:

    request = _get_response_object()

    if request.status_code == 200:
        return json.loads(request.text)
    else:
        raise requests.HTTPError(f"Could not find webpage (status code: {request.status_code}")


def _get_response_object() -> requests.models.Response:
    # NOTE: Make sure to include a & symbol at the end of the url for it to retrive the correct results properly.
    api_link_specific = "https://www.tes.com/api/jobs/browser/search-v3?siteCountry=gb&&locations=United%20Kingdom%3AEngland%3AYorkshire%20and%20the%20Humber%3ALeeds&keywords=&workplaces=Secondary&positions=Teaching%20and%20Lecturing&subjects=Science&"
    request = requests.get(api_link_specific.strip(), headers={"referer": "https://www.tes.com/jobs/browse/"})
    return request