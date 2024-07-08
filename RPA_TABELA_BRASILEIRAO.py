from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import pandas as pd

Service = Service()
options = webdriver.ChromeOptions()
browser = webdriver.Chrome(service=Service,options=options)

# Entrando no site
browser.get('https://ge.globo.com/futebol/brasileirao-serie-a/')

t = browser.find_element(By.XPATH,'//*[@id="classificacao__wrapper"]/article/section[1]/div').get_attribute('outerHTML')
df = pd.read_html(t)
print(df)