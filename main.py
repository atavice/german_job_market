import time
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By

baseurl = 'https://www.linkedin.com/jobs/search?keywords=working%2Bstudent&location=Munich&trk=guest_homepage-basic_jobs-search-bar_search-submit&currentJobId=3313824749&position=1&pageNum=0'

mydriver = webdriver.Chrome('./chromedriver')
mydriver.get(baseurl)
time.sleep(5)
mydriver.quit()
