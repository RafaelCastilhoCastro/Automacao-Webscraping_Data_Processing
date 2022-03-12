from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import pandas

# Opens new browser window, get prices and closes window
browser1 = webdriver.Chrome()

browser1.get("https://www.google.com/")
browser1.find_element(By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys("cotação dolar", Keys.ENTER)
dolar_price = browser1.find_element(By. XPATH, '//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]').get_attribute('data-value')

browser1.get("https://www.google.com/")
browser1.find_element(By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys("cotação euro", Keys.ENTER)
euro_price = browser1.find_element(By. XPATH, '//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]').get_attribute('data-value')

browser1.get("https://www.melhorcambio.com/ouro-hoje")
gold_price = browser1.find_element(By. XPATH, '//*[@id="comercial"]').get_attribute('value')
browser1.quit()

gold_price = gold_price.replace(",", ".")

# Importing DB & update prices
table1 = pandas.read_excel(r'Python\Automation - Webscraping & Data processing\produtos.xlsx')
table1.loc[table1["Moeda"] == "Dólar", "Cotação"] = float(dolar_price)
table1.loc[table1["Moeda"] == "Euro", "Cotação"] = float(euro_price)
table1.loc[table1["Moeda"] == "Ouro", "Cotação"] = float(gold_price)

# Updating purchase & retail prices
table1['Preço de Compra'] = table1['Preço Original'] * table1['Cotação']
table1['Preço de Venda'] = table1['Preço de Compra'] * table1['Margem']

# Exporting DB
table1.to_excel("Python/Automation - Webscraping & Data processing/produtos2.xlsx", index=False)
