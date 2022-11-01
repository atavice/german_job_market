import pandas as pd
from datetime import date

today = date.today()
desc_df = pd.read_csv(f'./job_descriptions/{today}.csv')
print(desc_df)

titles_series = pd.Series(desc_df["title"])
print(titles_series)

lgbt_friendly_phrases = ['all genders', 'm/f/x', 'm/w/d', 'f/m/div', 'w/m/x', 'f/m/x', 'w/d/m', 'm|w|d', 'd/f/m', 'f/m/d', 'w/m/d', 'm/w/x', 'm/f/d', 'w/m/div', 'd/m/w', 'm/w/*']

number_of_lgbtiq_friendly_jobs = 0
for title in titles_series:
    for phrase in lgbt_friendly_phrases:
        if phrase in title:
            number_of_lgbtiq_friendly_jobs += 1
            break
        
print(number_of_lgbtiq_friendly_jobs)



