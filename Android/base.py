from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class SelectorBasePage():

        driver = webdriver.Chrome('C:\chromedriver\chromedriver.exe')
        wait = WebDriverWait(driver, 600)
        driver.maximize_window()
        driver.get('https://selector.srvdev.ru/')
        wait.until(EC.presence_of_element_located((By.XPATH, '//*[@name="login"]')))
        login = 'АТиньков'
        password = '486250$Sel'
        driver.find_element_by_xpath('//*[@name="login"]').send_keys(login)
        driver.find_element_by_xpath('//*[@name="password"]').send_keys(password)
        driver.find_element_by_xpath('//*[@type="submit"]').click()
        wait.until(EC.presence_of_element_located((By.XPATH, '//*[@class="navbar-brand"]')))
