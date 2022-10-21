import os
import time
import platform
import chromedriver_autoinstaller

import bs4 as bs
import pandas as pd
from datetime import date

from math import ceil
from selenium import webdriver
from pyvirtualdisplay import Display
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

DRIVER_PATH = "./chromedriver"
BASE_URL = "https://www.linkedin.com"
EXTENTION_URL = "/jobs/search?keywords=Working%20Student&location=M%C3%BCnih%2C%20Bavyera%2C%20Almanya&locationId=&geoId=100477049&f_TPR=r86400&distance=25&position=1&pageNum=0"
NUM_OF_JOBS_PER_REFRESH = 25

display = Display(visible=0, size=(800, 800))  
display.start()

chromedriver_autoinstaller.install()
chrome_options = webdriver.ChromeOptions()    
 
options = ["--window-size=1200,1200", "--ignore-certificate-errors"]

for option in options:
    chrome_options.add_argument(option)

    
mydriver = webdriver.Chrome(options = chrome_options)
# mydriver = webdriver.Chrome(DRIVER_PATH)



mydriver.get(BASE_URL + EXTENTION_URL)

HTML_code = mydriver.page_source
soup = bs.BeautifulSoup(HTML_code, 'html.parser')

meta_contents_have_job_number = []

for meta in soup.find_all('meta'):
    if 'content' in meta.attrs:
        #Checks both turkish and english site content
        if ('yeni)' in meta['content']) or ('new)' in meta['content']) :
            meta_contents_have_job_number.append(meta['content'])

#Strips out the job number from its meta data    
preprocessed_content = meta_contents_have_job_number[0].split('(')
further_preprocessed_content = preprocessed_content[1].split(' ')
number_of_jobs = int(further_preprocessed_content[0])

num_of_scroll_down = ceil(number_of_jobs/NUM_OF_JOBS_PER_REFRESH) + 2

for _ in range(num_of_scroll_down):
    time.sleep(0.5)
    mydriver.find_element(by=By.TAG_NAME, value="body").send_keys(Keys.END)
    time.sleep(0.5)
    mydriver.find_element(by=By.TAG_NAME, value="body").send_keys(Keys.HOME)
    time.sleep(0.5)
    mydriver.find_element(by=By.TAG_NAME, value="body").send_keys(Keys.END)
    mydriver.find_element(by=By.TAG_NAME, value="body").send_keys(Keys.END)
    time.sleep(0.5)

time.sleep(5)

#Soup it again to catch recently rendered jobs
HTML_code = mydriver.page_source
soup = bs.BeautifulSoup(HTML_code, 'html.parser')

links = []
for link in soup.find_all('a', {'class': 'base-card__full-link absolute top-0 right-0 bottom-0 left-0 p-0 z-[2]'}):
    links.append(link.get('href'))

today = date.today()

if platform.system == 'Darwin':
    os.makedirs('./job_links', exist_ok=True)

df = pd.DataFrame(links)
df.to_csv(f'./job_links/{today}.csv', header=None, index=False)

mydriver.quit()
display.stop()


