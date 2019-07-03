from selenium import webdriver
from appium import webdriver
import time
from selector_main import SelectorMain
from selector_api import SelectorApi
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class AppDriver():

    def __init__(self):

        self.capabilities = {
            "platformName": "Android",
            "platformVersion": "9",
            "app": "C:\\Users\\atinkov\\Downloads\\selector_1.0.0_betaRelease82.apk",
            "deviceName": "NNF6R19121001251",
            "appWaitActivity": "com.dgppl.selector.ui.activity.main.MainActivity",
            "appWaitPackage": "com.dgppl.selector.beta",
            "newCommandTimeout": "900000",
            "skipDeviceInitialization": "true",
            "noReset": "true"
        }
        self.wait = WebDriverWait(self.app, 600)

    def open(self):
        self.app = webdriver.Remote("http://localhost:4723/wd/hub", self.capabilities)


    def get_device_id(self):
        device_id = str(self.app.find_element_by_id("com.dgppl.selector.beta:id/numberDevice").text.split(' ', 2)[2])
        print(device_id)

    def update(self):
        self.app.find_element_by_id('com.dgppl.selector.beta:id/startSyncBtn').click()
        self.wait.until(EC.presence_of_element_located((By.ID, "com.dgppl.selector.beta:id/startSyncBtn")))