from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


driver = webdriver.Chrome(executable_path=r'./chromedriver.exe')
 
url = "https://www.google.com/"
driver.get(url)

# Localize a barra de pesquisa e insira o termo desejado
termo_de_pesquisa = "Livros pdf de programação"
search_box = driver.find_element(By.NAME, "q")
search_box.send_keys(termo_de_pesquisa)

# Pressione Enter para iniciar a pesquisa
search_box.submit()

time.sleep(10)

# Colete os links dos resultados da pesquisa usando xpath
result_links = driver.find_elements(By.XPATH, "//h3/following::a")
results = driver.find_elements(By.CLASS_NAME, "tF2Cxc")

# Exiba os links encontrados
for result in results:
    title = result.find_element(By.TAG_NAME, "h3").text
    link = result.find_element(By.TAG_NAME, "a").get_attribute("href")
    print(f"Titulo: {title}\nLink: {link}\n")

# Feche o navegador quando terminar

time.sleep(10)
driver.quit()

