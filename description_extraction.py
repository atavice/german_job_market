import os
import time
import platform
import bs4 as bs
import pandas as pd
from datetime import date
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

DRIVER_PATH = "./chromedrivermac"

def extract_job_descriptions(scrape_session: dict):
    """
    input: city ve url içeren bir dictionary alır.
    output: scraped_jobs içeren bir dictionary verir.
    """
    return_dict = {}

    script_starting_time = datetime.now()

    chrome_options = webdriver.ChromeOptions()    
    options = ["--window-size=1920x1080", "--ignore-certificate-errors", '--headless', '--no-sandbox', '--disable-dev-shm-usage']

    for option in options:
        chrome_options.add_argument(option)
    
    mydriver = webdriver.Chrome(DRIVER_PATH, options = chrome_options)

    today = date.today()
    city = scrape_session['city']
    links_df = pd.read_csv(f'./job_links/{city}/{today}.csv')

    links = links_df[links_df.columns[0]].values.tolist()

    traversed_jobs = 0
    scraped_jobs = 0
    driver_close_counter = 0
    job_titles = []
    job_descriptions = []
    job_locations = []
    for link in links:
    
        traversed_jobs += 1
        driver_close_counter += 1
        
        mydriver.get(link)

        time.sleep(3)

        HTML_code = mydriver.page_source
        soup = bs.BeautifulSoup(HTML_code, 'html.parser')
        desc_list = soup.find_all('div', {'class': 'show-more-less-html__markup'})
        title_list = soup.find_all('h1', {'class': 'top-card-layout__title'})
        location_list = soup.find_all('span', {'class': 'topcard__flavor topcard__flavor--bullet'})
        if (len(desc_list) != 0 and len(title_list) !=0 and len(location_list) != 0):
            scraped_jobs += 1
            job_titles.append(title_list[0].get_text())
            job_descriptions.append(desc_list[0].get_text())
            job_locations.append(location_list[0].get_text())
        else:
            job_titles.append("Fail")
            job_descriptions.append("Fail")
            job_locations.append("Fail")

        if(driver_close_counter%3 == 0):
            mydriver.close()
            mydriver = webdriver.Chrome(DRIVER_PATH, options = chrome_options)

        print(f"Scraped jobs: {str(scraped_jobs)}\nTraversed jobs: {str(traversed_jobs)}\nRatio: {scraped_jobs/traversed_jobs}")

    print(f"Link sayısı: {len(links)}\nListe uzunluğu: {len(job_descriptions)}")
    return_dict["scraped_jobs"] = scraped_jobs

    descriptions_df = pd.DataFrame({'link': links, 
                                    'title': job_titles, 
                                    'description': job_descriptions,
                                    'location': job_locations})

    descriptions_df.to_csv(f'./job_descriptions/{city}/{today}.csv', index=False)

    script_processing_time = datetime.now() - script_starting_time
    print(f"Script processing time: {script_processing_time}")

    return return_dict