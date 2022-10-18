import datetime
import pandas as pd
import os


def save_file(df: pd.DataFrame) -> bool:
    timestamp = _get_current_timestamp()
    df.to_csv(f"{os.getcwd()}\\data/job_data_{timestamp}.csv", index=False)
    return True

def _get_current_timestamp() -> str:
    timestamp = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
    return timestamp
