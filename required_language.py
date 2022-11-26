import pandas as pd
from datetime import date
import description_preprocessing

def calculate_required_lang_metric(scrape_session: dict) -> dict:
    """
    input: city ve url içeren dictionary alır
    output: iş için gerekli dillerin sayısını içeren dictionary verir.
    """

    today = date.today()
    return_dict = {}
    city = scrape_session['city']
    descriptions_df = pd.read_csv(f"./job_descriptions/{city}/{today}.csv")
    
    de_keywords = ['deutschke', 'deutsche ', 'deutsch ', 'deutsch-', 'german']

    preprocessed_description_list = description_preprocessing(descriptions_df)

    fail_no = 0
    german_required_no = 0
    german_not_required_no = 0

    for description in preprocessed_description_list:
        if 'fail' == description:
            fail_no += 1

        keyword_counter = 0
        for keyword in de_keywords:
            if keyword in description:
                keyword_counter += 1
                german_required_no += 1
                break
        if keyword_counter == 0:
            german_not_required_no += 1
        
    return_dict['de_required_no'] = german_required_no
    return_dict['de_not_required_no'] = german_not_required_no
    return_dict['fail_lang_required_no'] = fail_no

    return_dict

