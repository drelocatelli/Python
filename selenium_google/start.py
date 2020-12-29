from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os

# Configurações 
options = Options()
options.headless = True # não mostra navegador
browser = webdriver.Chrome(executable_path="./browser/chromedriver", options=options)
options = browser.maximize_window()

# Search
def search(what):
    try:
        browser.get('http://www.google.com.br/')
        input = browser.find_element_by_css_selector('#tsf > div:nth-child(2) > div.A8SBwf > div.RNNXgb > div > div.a4bIc > input')
        input.send_keys(what)
        btnSearch = browser.find_element_by_xpath('//*[@id="tsf"]/div[2]/div[1]/div[3]/center/input[1]').click()
        response = browser.find_element_by_xpath('//*[@id="kp-wp-tab-overview"]/div[1]/div/div/div/div[1]/div/div/div/div/span[1]')
        print('Aguardando pesquisa...')
        os.system('sleep 5')
        print(response.text)
    except TimeoutException:
        print('Erro de conexão, tente novamente.')

# Application Starts
request = input('Pesquisar Google: ')
search(request)


browser.quit()
