import time

from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

urls = []
addresses = []
prices = []

response = requests.get(f"https://appbrewery.github.io/Zillow-Clone/")
print(response.status_code)

soup = BeautifulSoup(response.text, "html.parser")
address_tags = soup.findAll(name="address")
for address in address_tags:
    addresses.append(address.text.replace("\n", "")[32:-30].replace("|", ","))
price_tags = soup.findAll(name="span", class_="PropertyCardWrapper__StyledPriceLine")
for price in price_tags:
    prices.append(price.text[0:6])
for link in soup.findAll('a', href=True, class_="StyledPropertyCardDataArea-anchor"):
    urls.append(link['href'])

for x in range(len(addresses)):
    time.sleep(1)
    driver.get("https://forms.gle/xjvsyDBkwrgjXdUD6")
    time.sleep(1)
    address_input = driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    address_input.send_keys(addresses[x])
    price_input = driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    price_input.send_keys(prices[x])
    url_input = driver.find_element(By.XPATH,
                                      value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    url_input.send_keys(urls[x])
    submit_button = driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div')
    submit_button.click()
    time.sleep(3)