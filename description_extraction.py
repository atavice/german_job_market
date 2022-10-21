import time
import csv
import bs4 as bs
import pandas as pd
import numpy as np
from datetime import date, datetime
from math import ceil
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import platform
import os

DRIVER_PATH = "./chromedriver"
mydriver = webdriver.Chrome(DRIVER_PATH)
today = date.today()

links_df = pd.read_csv(f'./job_links/{today}.csv')

links = links_df[links_df.columns[0]].values.tolist()
print(links[0])
print('**********')

jobs = 0
successful = 0
count = 0
descriptions = []
for link in links:
    jobs += 1
    time.sleep(3)
    mydriver.get(link)
    HTML_code = mydriver.page_source
    soup = bs.BeautifulSoup(HTML_code, 'html.parser')
    desc_list = soup.find_all('div', {'class': 'show-more-less-html__markup'})
    if len(desc_list) != 0:
        successful += 1
        descriptions.append(desc_list[0].get_text())
    count += 1
    if(count == 3):
        mydriver.close()
        mydriver = webdriver.Chrome(DRIVER_PATH)
    print(str(successful)+"---"+str(jobs))
print(len(descriptions))

if platform.system() == 'Darwin':
    os.makedirs('./job_descriptions', exist_ok=True)

descriptions_df = pd.DataFrame(descriptions)
descriptions_df.to_csv(f'./job_descriptions/{today}.csv', header=None, index=False)

processing_time = time.time()
print(f'Processing time of the script: {processing_time}')

