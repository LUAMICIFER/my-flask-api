import os
import time
import pickle
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import requests
from bs4 import BeautifulSoup
os.environ['PATH'] += r"/home/advik/python/selenium/chromedriver_linux64 (1)"
driver = webdriver.Firefox()
driver.get("https://www.linkedin.com/")
driver.maximize_window()
button1 = driver.find_element(By.XPATH,'/html/body/main/section[1]/div/div/a').click()
