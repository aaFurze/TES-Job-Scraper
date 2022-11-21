from src.choose_filters import UserPreferenceStrings, FilterCreator
from src.scrapers import get_jobs_json
from src.parser import get_job_data_df
from src.export_data import save_file


def main():
    user_preferences = UserPreferenceStrings()
    user_preferences.prompt_for_user_preferences()
    tes_json = get_jobs_json(FilterCreator(user_preferences, setup_on_init=True))
    df = get_job_data_df(tes_json)
    save_file(df)


if __name__ == "__main__":
    main()