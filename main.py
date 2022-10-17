import time
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By

DRIVER_PATH = "./chromedriver"
BASE_URL = "https://www.linkedin.com"
EXTENTION_URL = "/jobs/search?keywords=working%2Bstudent&location=Munich&trk=guest_homepage-basic_jobs-search-bar_search-submit&currentJobId=3313824749&position=1&pageNum=0"

mydriver = webdriver.Chrome(DRIVER_PATH)
mydriver.get(BASE_URL + EXTENTION_URL)
time.sleep(5)
mydriver.quit()
