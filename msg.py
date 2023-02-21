from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time


website = 'https://web.whatsapp.com/'
numero_telefono = ''  
mensage = "Test"

driver = webdriver.Chrome()
driver.get(website)
driver.maximize_window()
time.sleep(30)  

buscar_telefono = driver.find_element(by='xpath', value='//div[@title="Search input textbox"]')
buscar_telefono.send_keys(numero_telefono)
time.sleep(2)

contactos = driver.find_elements(by='xpath', value='//div[@aria-label="Search results."]//div[@data-testid="cell-frame-container"]')
numero_contact = contactos[-1]  # selecciona ultimo elemento de la lista (este elemento representa el primer elemento en la lista de busqueda de whatsapp)
numero_contact.click()
time.sleep(2)

# enviar mensaje
caja_mensaje = driver.find_element(by='xpath', value='//div[@title="Type a message"]')
caja_mensaje.send_keys(mensage)
time.sleep(1)  # esperar hasta que el icono de microfono cambie al icono "enviar mensaje"

boton_enviar = driver.find_element(by='xpath', value='//button/span[@data-testid="send"]')
boton_enviar.click()
time.sleep(5)  # esperar hasta que el mensaje sea enviado

driver.quit()
