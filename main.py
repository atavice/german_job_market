import time
from math import ceil

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import platform 
import pyautogui
import bs4 as bs

DRIVER_PATH = "./chromedriver"
BASE_URL = "https://www.linkedin.com"
EXTENTION_URL = "/jobs/search?keywords=Working%20Student&location=M%C3%BCnih%2C%20Bavyera%2C%20Almanya&locationId=&geoId=100477049&f_TPR=r86400&distance=25&position=1&pageNum=0"
NUM_OF_JOBS_PER_REFRESH = 25

mydriver = webdriver.Chrome(DRIVER_PATH)
mydriver.get(BASE_URL + EXTENTION_URL)

HTML_code = mydriver.page_source
soup = bs.BeautifulSoup(HTML_code, 'html.parser')

meta_contents_have_job_number = []

for meta in soup.find_all('meta'):
    if 'content' in meta.attrs:
        if ('yeni)' in meta['content']) or ('new)' in meta['content']) :
            meta_contents_have_job_number.append(meta['content'])
       
preprocessed_content = meta_contents_have_job_number[0].split('(')
further_preprocessed_content = preprocessed_content[1].split(' ')
number_of_jobs = int(further_preprocessed_content[0])
num_of_scroll_down = ceil(number_of_jobs/NUM_OF_JOBS_PER_REFRESH) - 1

for _ in range(num_of_scroll_down):
    time.sleep(1.5)
    mydriver.find_element(by=By.TAG_NAME, value="body").send_keys(Keys.END)
    

time.sleep(5)
mydriver.quit()
