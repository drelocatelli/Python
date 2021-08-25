from selenium import webdriver
from selenium.webdriver import ChromeOptions, Chrome
import os, time

# Configurações 
options = webdriver.ChromeOptions()
options.headless = True # não mostra navegador
path = os.getcwd()+"\chromedriver_win.exe"
path = path.replace("/", "\\")
options.add_experimental_option("detach", True)
# options.add_argument('--start-maximized')
options.add_argument("--window-position=0, 0");
browser = webdriver.Chrome(executable_path=path, options=options)


def take_screenshot(html):
    browser.get(html)

    time.sleep(3)
    browser.set_window_size(1920, 1080)
    browser.save_screenshot('./screenshots/telas/1920x1080.png')
    browser.set_window_size(1920, 2000)
    browser.save_screenshot('./screenshots/1920x2000.png')
    
    browser.set_window_size(1366, 640)
    browser.save_screenshot('./screenshots/telas/1366x640.png')
    browser.set_window_size(1366, 2000)
    browser.save_screenshot('./screenshots/1366x2000.png')

    browser.set_window_size(360, 640)
    browser.save_screenshot('./screenshots/telas/360x640.png')
    browser.set_window_size(360, 2000)
    browser.save_screenshot('./screenshots/360x2000.png')

    browser.set_window_size(414, 896)
    browser.save_screenshot('./screenshots/telas/414x896.png')
    browser.set_window_size(414, 2000)
    browser.save_screenshot('./screenshots/414x2000.png')


with open('path.txt', 'r') as fs:
    for f in fs:
        f = f.strip()
        take_screenshot(f)

browser.quit()
