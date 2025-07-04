from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import pandas as pd 
import time 
from tqdm import tqdm 

options = webdriver.ChromeOptions()
options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36')
options.add_argument('--headless')  
options.add_argument('--disable-gpu')  
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)

driver = webdriver.Chrome(options=options)

url='https://www.clickbus.com.br'
print("🚀 Iniciando o scraping em https://www.clickbus.com.br...")
driver.get(url)

wait = WebDriverWait(driver, 20)

try:
    time.sleep(5)
    print("... 🍪 Aceitando cookies...")
    cookie_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[data-testid="privacy-policy-button"]')))
    cookie_button.click()
    print("✅ Cookies aceitos.")
except Exception as e:
    print(f"⚠️ Não foi possível lidar com o banner de cookies: {e}")

print("... 🚌 Preenchendo origem e destino...")
origin_field = wait.until(EC.element_to_be_clickable((By.ID, 'origin')))
origin_field.send_keys('Sao Paulo, SP - TODOS')
wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[data-testid="place-item-suggestion"]'))).click()


destination_field = wait.until(EC.element_to_be_clickable((By.ID, 'destination')))
destination_field.send_keys('Rio de Janeiro - RJ')

wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[data-testid="place-item-suggestion"]'))).click()
print("✅ Origem e destino preenchidos.")

print("... 📅 Selecionando a data...")

date_picker = wait.until(EC.element_to_be_clickable((By.ID, 'departure-date')))
date_picker.click()

available_day = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[data-testid="date-picker-calendar"] [role="button"]')))
available_day.click()
print("✅ Data selecionada.")

print("... 🔍 Buscando passagens...")
search_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[data-testid="search-box-button"]')))
search_button.click()

print("... ⏳ Aguardando resultados da busca...")

wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.search-item-main')))
print("✅ Resultados carregados.")

soup = BeautifulSoup(driver.page_source, 'html.parser')

cards = soup.find_all('div', class_='search-item-main')

results = []
print(f"📊 Encontrados {len(cards)} resultados. Extraindo dados...")

for card in tqdm(cards, desc="Extraindo passagens"):
    try:

        company = card.get('data-travel-company-name', 'N/A')
        
        departure_time_element = card.find('time', class_='departure-time')
        departure_time = departure_time_element.text.strip() if departure_time_element else 'N/A'

        arrival_time_element = card.find('time', class_='return-time')
        arrival_time = arrival_time_element.text.strip() if arrival_time_element else 'N/A'
        
        price_element = card.find('span', class_='price-value')
        price = price_element.text.strip() if price_element else 'N/A'
        
        results.append({
            'Empresa': company,
            'Partida': departure_time,
            'Chegada': arrival_time,
            'Preço': price
        })
    except AttributeError:
        continue  
        
df = pd.DataFrame(results)
print("\n📄 Amostra dos dados extraídos:")
print(df.head())

df.to_csv('passagens_sp_rj.csv', index=False, encoding='utf-8')
print("\n💾 Dados salvos com sucesso em passagens_sp_rj.csv")