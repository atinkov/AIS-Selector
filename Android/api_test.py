from selenium import webdriver
from appium import webdriver
import time
from android_driver import AndroidDriver
from selector_main import SelectorMain
from selector_api import SelectorApi
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

android = AndroidDriver()

device_id = android.get_devaice_id()
print(device_id)

main_page = SelectorMain()

main_page.login()

main_page.activate_device(device_id, 'HUAWEI, CMR-W09, 28', 'Администраторы')

device_api = main_page.get_device_api_key()
print(device_api)

main_page.save_device_settings()

main_page.open_report_data()

main_page.select_organization("МАДИ")

main_page.select_report_period()

main_page.switch_to_report_window()


report_id = main_page.get_report_id()
print(report_id)

report_date = main_page.convert_date()
print(report_date)

api_page = SelectorApi()

api_page.open_page()

api_page.load_report(report_id)

main_page.confirm_report()

android.update('3m')

android.select_org('МАДИ')

android.select_week(report_date)

android.check_report()


