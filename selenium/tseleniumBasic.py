from selenium import webdriver

# INSTANCIAÇÃO
#drive = webdriver.Chrome()

# ABRIR O GLOOGLE NESSA URL
#drive.get('https://pandas.pydata.org/docs/user_guide/index.html')
#caixa_de_entrada = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, ':2k')))

# ============================================================ OUTRO CÓDIGO CÓPIADO =========================================================

#from selenium import webdriver
#from selenium.webdriver.common.by import By
#from selenium.webdriver.support.ui import WebDriverWait
#from selenium.webdriver.support import expected_conditions as EC
#
# Iniciar o navegador
#driver = webdriver.Chrome()
#
# Acessar o Gmail
#driver.get('https://mail.google.com/mail/?authuser=0&ogbl')
#
# Aguardar até que a caixa de entrada esteja presente (timeout de 10 segundos)
#caixa_de_entrada = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, ':2k')))
#
# Manter o navegador aberto - remova essa linha caso deseje fechar o navegador após essa etapa
#input("Pressione Enter para fechar o navegador...")
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as wdw
from selenium.webdriver.support import expected_conditions as ec

# INSTANCIAÇÃO
driver = webdriver.Chrome()

# ABRIR O GLOOGLE NESSA URL
driver.get('file:///home/erick/Modelos/programas/javascript/indexSelenium.html')

# ESPERAR ATÉ QUE O ELEMENTO "Getting Started" ESTEJA VISÍVEL (timeout de 10 segundos)
try:
    elemento = wdw(driver, 10).until(ec.visibility_of_element_located((By.PARTIAL_LINK_TEXT, "Getting Started")))
   
except TimeoutError:
    print("Elemento 'Getting Started' não foi encontrado após o tempo de espera.")

# Manter o navegador aberto - remova essa linha caso deseje fechar o navegador após essa etapa
input("Pressione Enter para fechar o navegador...")

# Fechar o navegador
driver.quit()

