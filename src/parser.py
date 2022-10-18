from typing import List
import pandas as pd


def get_job_data_df(raw_data: dict) -> pd.DataFrame:
    raw_jobs_data = raw_data["searchResult"]["jobs"]["items"]
    empty_df = _create_empty_df()
    df = _populate_df_with_job_data(empty_df, raw_jobs_data)
    return df


def _create_empty_df() -> pd.DataFrame:
    column_names = ["job_id", "job_title", "tenure", "start_date", "application_deadline", "employer_name", "location", "salary", "url"]
    return pd.DataFrame(columns=column_names)


def _populate_df_with_job_data(df: pd.DataFrame, raw_jobs_data: list) -> pd.DataFrame:
    data = _extract_job_data(raw_jobs_data)
    for row in data:
        df.loc[len(df)] = row
    return df

def _extract_job_data(raw_jobs_data: list) -> List[list]:
    output = []
    for job in raw_jobs_data:
        # This is a hacky solution. Replace with generalised check (do this operation for all keys requesting).
        if ("displaySalary" not in list(job.keys())):
            job["displaySalary"] = None
        row = [
            job["jobId"], job["title"], job["displayContractTerms"], job["displayJobStartDate"], 
        job["advert"]["displayEndDateShort"], job["employerName"], job["displayLocation"],
         job["displaySalary"], job["jobPageCanonicalUrl"]
            ]
        output.append(row)
    return output
    
