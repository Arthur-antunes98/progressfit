from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Inicializa o navegador
driver = webdriver.Chrome()

url_inicial = 'file:///C:/Users/Yago Victor/Documents/fork_progressfit/progressfit/login.html'
driver.get("url_incial")

time.sleep(5)

#sendkeys e clear()
campo_email = driver.find_element(By.ID, "email")
campo_email.send_keys("teste@progressfit.com")

campo_senha = driver.find_element(By.ID, "password")
campo_senha.send_keys("123teste")


campo_email.clear()
campo_senha.clear()

#--------------------------------------------------------

# --- Teste 2: get_attribute() ---
valor_digitado = campo_usuario.get_attribute("value")
print("Valor digitado no campo usuário:", valor_digitado)


# --- Teste 4: send_keys() + Enter ---
campo_usuario.send_keys("standard_user")
campo_senha = driver.find_element(By.ID, "password")
campo_senha.send_keys("secret_sauce")
campo_senha.send_keys(Keys.ENTER)

time.sleep(5)

# --- Teste 5: current_url ---
print("URL atual:", driver.current_url)

# --- Teste adicional: is_displayed() ---
botao_menu = driver.find_element(By.ID, "react-burger-menu-btn")
print("Botão de menu visível?", botao_menu.is_displayed())

# Fecha o navegador
driver.quit()
