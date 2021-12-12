from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

# Тест кейс 6
# Проверка
driver.get('https://rambler.ru')

vhod_na_pochtu = driver.find_element(By.XPATH, '//*[@id="main"]/div[1]/div/div/div[2]/div[2]/button').click()

registration = driver.find_element(By.XPATH, '//*[@id="login"]').click().send_keys("yan")
