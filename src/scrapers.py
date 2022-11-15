import requests
import json
import httpx
import asyncio

from .construct_url import ConstructURL

from typing import List, Protocol


class JobFilters(Protocol):
    lat: float
    long: float
    distance: int
    workplaces: List[str]
    positions: List[str]
    subjects: List[str]
    no_pages: int


def get_jobs_json(filters: JobFilters) -> List[dict]:

    requests = asyncio.run(_get_response_object(filters))

    json_objects = []

    for request in requests:
        if request.status_code == 200:
            json_objects.append(json.loads(request.text))
        else:
            raise httpx.HTTPError(f"Could not find webpage (status code: {request.status_code}")
    
    output = []

    for obj in json_objects:
        output += obj["searchResult"]["jobs"]["items"]

    return output


async def _get_response_object(filters: JobFilters) -> List[httpx.Response]:
    # NOTE: Make sure to include a & symbol at the end of the url for it to retrive the correct results properly.
    output = []
    start_url = ConstructURL(filters.lat, filters.long, filters.distance, filters.workplaces, filters.positions,
             filters.subjects, 1).url
    print(start_url)
    first_page_request = httpx.get(start_url, headers={"referer": "https://www.tes.com/jobs/browse/"})

    if first_page_request.status_code == 200:
        output.append(first_page_request)
        max_pages_possible = _get_num_pages(first_page_request.text)
        if max_pages_possible < filters.no_pages:
            filters.no_pages = max_pages_possible
    
    if filters.no_pages == 1: return output

    async with httpx.AsyncClient() as client:
        for i in range(1, filters.no_pages):
            url = ConstructURL(filters.lat, filters.long, filters.distance, filters.workplaces, filters.positions,
             filters.subjects, i + 1).url
            print(f"url: {url}")
            new_request = await client.get(url, headers={"referer": "https://www.tes.com/jobs/browse/"})
            if new_request.status_code == 200:
                output.append(new_request)

    return output


def _get_num_pages(first_page: str) -> int:
    content = json.loads(first_page)
    return content["searchResult"]["jobs"]["metadata"]["pagination"]["totalpages"]

def get_location_json(location: str):
    url_start = "https://www.tes.com/api/autocomplete/location?q="
    url_end = "&g=gb&l=5"

    url = url_start + location + url_end
    request = requests.get(url)

    if request.status_code == 200:
        return json.loads(request.text)
    else:
        raise requests.HTTPError(f"Could not find location webpage (status code: {request.status_code}")
