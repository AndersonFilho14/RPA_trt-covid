from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import pandas as pd

Service = Service()
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=Service,options=options)

# Entrando no site
url = 'https://www.trt.net.tr/portuguese/covid19'
driver.get(url)

pais = ['China','Cuba','Laos','Vietnã','Venezuela']
#Pesquisar na lista o pais 
driver.find_element(By.XPATH,'//*[@id="filterField"]').send_keys("Brasil")

#Pegar as informações no do pais
#Transforma em lista
