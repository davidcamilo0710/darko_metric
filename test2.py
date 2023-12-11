from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
import pandas as pd
from io import StringIO

url_darko = "https://apanalytics.shinyapps.io/DARKO//"

options = Options()
options.add_argument('--headless')
options.add_argument('--disable-gpu') 
driver = webdriver.Chrome(options=options)
driver.get(url_darko)
