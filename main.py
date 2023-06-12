from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager #para toda vez que meu google chrome atualizar
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

# identificar a versão do chrome atual e se necessario instalar uma a nova versão
service = Service(ChromeDriverManager().install())
op = webdriver.ChromeOptions()
op.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=service, options=op)
driver.maximize_window()

# Entrar e digitar no campo de pesquisa
driver.get('https://www.nytimes.com/')

button_search_field = driver.find_element(by=By.XPATH, value='/html/body/div[1]/div[2]/div/header/section[1]/div[1]/div[2]/button').click()
input_search_field = driver.find_element(By.CSS_SELECTOR, '.css-1j26cud')
input_search_field.send_keys("beyonce")
input_search_field.send_keys(Keys.ENTER)
text_topic = driver.find_element(By.CSS_SELECTOR, '.css-o0qk87').text
print(text_topic)
