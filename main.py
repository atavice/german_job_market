import time
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


DRIVER_PATH = "./chromedriver"
BASE_URL = "https://www.linkedin.com"
EXTENTION_URL = "/jobs/search?keywords=Working%20Student&location=M%C3%BCnih%2C%20Bavyera%2C%20Almanya&locationId=&geoId=100477049&f_TPR=r86400&distance=25&position=1&pageNum=0"

mydriver = webdriver.Chrome(DRIVER_PATH)
mydriver.get(BASE_URL + EXTENTION_URL)

time.sleep(1)
mydriver.find_element(by=By.TAG_NAME, value="body").send_keys(Keys.END)
time.sleep(1)
mydriver.find_element(by=By.TAG_NAME, value="body").send_keys(Keys.END)
time.sleep(1)
mydriver.find_element(by=By.TAG_NAME, value="body").send_keys(Keys.END)



time.sleep(5)
mydriver.quit()
