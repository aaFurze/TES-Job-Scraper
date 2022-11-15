from typing import List, Union
import pandas as pd


def get_job_data_df(raw_data: List[dict]) -> pd.DataFrame:
    empty_df = _create_empty_df()
    df = _populate_df_with_job_data(empty_df, raw_data)
    return df


def _create_empty_df() -> pd.DataFrame:
    column_names = ["job_id", "job_title", "tenure", "start_date", "application_deadline", "employer_name", "location", "salary", "url"]
    return pd.DataFrame(columns=column_names)


def _populate_df_with_job_data(df: pd.DataFrame, raw_jobs_data: List[dict]) -> pd.DataFrame:
    data = _extract_job_data(raw_jobs_data)
    for row in data:
        df.loc[len(df)] = row
    return df

def _extract_job_data(raw_jobs_data: list) -> List[list]:

    KEYS_CHECKING = ["jobId", "title", "displayContractTerms", "displayJobStartDate", ["advert", "displayEndDateShort"],
     "employerName", "displayLocation", "displaySalary", "jobPageCanonicalUrl"]

    output = []
    for job in raw_jobs_data:
        job = _ensure_job_has_keys(job, KEYS_CHECKING)
        # This is a hacky solution. Replace with generalised check (do this operation for all keys requesting).
        row = [
            job["jobId"], job["title"], job["displayContractTerms"], job["displayJobStartDate"], 
        job["advert"]["displayEndDateShort"], job["employerName"], job["displayLocation"],
         job["displaySalary"], job["jobPageCanonicalUrl"]
            ]
        output.append(row)
    return output
    

def _ensure_job_has_keys(job: dict, keys_checking: List[Union[str, List[str]]]) -> dict:
    job_keys = list(job.keys())
    
    for key in keys_checking:
        if type(key) is list:
            if key[0] not in job_keys:
                job[key[0]] = {key[1]: None}
            else:
                job[key[0]] = _ensure_job_has_keys(job[key[0]], key[1:])
        else:
            if key not in job_keys:
                job[key] = None
    
    return job
