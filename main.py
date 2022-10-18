from src.scraper import get_jobs_json
from src.parser import get_job_data_df
from src.export_data import save_file


def main():
    tes_json = get_jobs_json()
    df = get_job_data_df(tes_json)
    save_file(df)


if __name__ == "__main__":
    main()
