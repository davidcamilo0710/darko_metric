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

try:
    driver.find_element(By.XPATH, "//a[text()='Daily Player Per-Game Projections']").click()
    time.sleep(2)
    download_button = driver.find_element(By.ID, "download_daily")
    download_link = download_button.get_attribute('href')
    csv_data = driver.execute_script(f"return fetch('{download_link}').then(response => response.text());")
    df = pd.read_csv(StringIO(csv_data))
    # Imprimir información básica sobre el DataFrame
    print("Información general:")
    print(df.head(5))
finally:
    # Cierra el navegador al finalizar
    driver.quit()
