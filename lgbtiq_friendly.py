import pandas as pd
from datetime import date


def calculate_lgbt_metric(scrape_session: dict):
    """
    input: city ve url içeren dictionary alır.
    output: lgbt_friendly_jobs sayısını içeren dictionary verir.
    """
    today = date.today()

    return_dict = {}
    city = scrape_session['city']
    desc_df = pd.read_csv(f'./job_descriptions/{city}/{today}.csv')
    titles_series = pd.Series(desc_df["title"])

    lgbt_friendly_phrases = ['all genders', 'm/f/x', 'm/w/d', 'f/m/div', 
                             'w/m/x', 'f/m/x', 'w/d/m', 'm|w|d', 'd/f/m', 
                             'f/m/d', 'w/m/d', 'm/w/x', 'm/f/d', 'w/m/div', 
                             'd/m/w', 'm/w/*']

    number_of_lgbtiq_friendly_jobs = 0
    for title in titles_series:
        for phrase in lgbt_friendly_phrases:
            if phrase in title:
                number_of_lgbtiq_friendly_jobs += 1
                break
    return_dict['lgbt_friendly_jobs'] = number_of_lgbtiq_friendly_jobs
    return return_dict



