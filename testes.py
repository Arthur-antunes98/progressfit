from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.maximize_window()

url_login = 'file:///C:/Users/Yago Victor/Documents/fork_progressfit/progressfit/login.html'
driver.get(url_login)

print(f"Caminho da página: {driver.current_url}\n Nome da página: {driver.title}")
time.sleep(1)

#sendkey, clear e is_enabled
campo_email = driver.find_element(By.ID, "email")
campo_senha = driver.find_element(By.ID, "password")
#checa se o input do email está habilitado
if campo_email.is_enabled() and campo_senha.is_enabled():
    print("Os campos de e-mail e senha estão habilitados para digitação.")
    campo_email.send_keys("Jarley@progressfit.com")
    campo_senha.send_keys("123teste")
else:
    print("O campo de e-mail está desativado. Não é possível digitar.")

time.sleep(1)
campo_email.clear()
campo_senha.clear()
time.sleep(1)

campo_email = driver.find_element(By.ID, "email")
campo_email.send_keys("Yago@progressfit.com")

campo_senha = driver.find_element(By.ID, "password")
campo_senha.send_keys("123teste")

#get_attribute, currunt_url
UserEmail = campo_email.get_attribute("value")
print(f"INFORMAÇÃO DE LOGIN:\n Email: {UserEmail}")

time.sleep(1)

driver.find_element(By.ID, "btn").click()
print(f"Caminho da página: {driver.current_url}\n Nome da página: {driver.title}")

campo_protocolos = driver.find_element(By.CLASS_NAME, "cards")
if campo_protocolos:
    print("Os protocolos estão visiveis na tela home")
else: 
    print("Ocorreu algum erro na exibição dos protocolos")

time.sleep(3)


# --- Teste 2: get_attribute() ---
# valor_digitado = campo_email.get_attribute("value")
# print("Valor digitado no campo usuário:", valor_digitado)


# # --- Teste 4: send_keys() + Enter ---
# campo_usuario.send_keys("standard_user")
# campo_senha = driver.find_element(By.ID, "password")
# campo_senha.send_keys("secret_sauce")
# campo_senha.send_keys(Keys.ENTER)

# time.sleep(5)

# # --- Teste 5: current_url ---
# print("URL atual:", driver.current_url)

# # --- Teste adicional: is_displayed() ---
# botao_menu = driver.find_element(By.ID, "react-burger-menu-btn")
# print("Botão de menu visível?", botao_menu.is_displayed())

# Fecha o navegador
driver.quit()
