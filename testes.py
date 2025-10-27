
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Inicializa o navegador
driver = webdriver.Chrome()

# Abre a página (ex: sua tela local ou um site simples)
driver.get("https://www.saucedemo.com/")  # exemplo de login público para teste

time.sleep(2)

# --- Teste 1: send_keys() ---
campo_usuario = driver.find_element(By.ID, "user-name")
campo_usuario.send_keys("standard_user")

# --- Teste 2: get_attribute() ---
valor_digitado = campo_usuario.get_attribute("value")
print("Valor digitado no campo usuário:", valor_digitado)

# --- Teste 3: clear() ---
campo_usuario.clear()

# --- Teste 4: send_keys() + Enter ---
campo_usuario.send_keys("standard_user")
campo_senha = driver.find_element(By.ID, "password")
campo_senha.send_keys("secret_sauce")
campo_senha.send_keys(Keys.ENTER)

time.sleep(2)

# --- Teste 5: current_url ---
print("URL atual:", driver.current_url)

# --- Teste adicional: is_displayed() ---
botao_menu = driver.find_element(By.ID, "react-burger-menu-btn")
print("Botão de menu visível?", botao_menu.is_displayed())

# Fecha o navegador
driver.quit()
