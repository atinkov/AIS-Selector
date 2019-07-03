from selenium import webdriver
from appium import webdriver
import time
from selector_main import SelectorMain
from selector_api import SelectorApi
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from app_driver import AppDriver

app = AppDriver()

app.open()

app.get_device_id()
