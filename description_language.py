import pandas as pd
from datetime import date
from langdetect import detect
import description_preprocessing

def calculate_desc_lang_metric(scrape_session: dict) -> dict:
    """
    input: city ve url içeren dictionary alır.
    output: işlerin açıklamalarının dilini içeren dictionary verir.
    """

    today = date.today()

    return_dict = {}
    city = scrape_session['city']
    descriptions_df = pd.read_csv(f"./job_descriptions/{city}/{today}.csv")
    
    preprocessed_description_list = description_preprocessing(descriptions_df)

    german_description_no = 0
    english_description_no = 0
    failed_to_scraped_no = 0

    for description in preprocessed_description_list:
        language = detect(description)
        if language == 'de':
            german_description_no += 1
        elif language == 'en':
            english_description_no += 1
        else:
            failed_to_scraped_no +=1
    
        return_dict['de_desc_no'] = german_description_no
        return_dict['en_desc_no'] = german_description_no
        return_dict['fail_desc_no'] = german_description_no
    
        return return_dict
