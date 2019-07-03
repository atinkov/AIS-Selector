from selenium import webdriver
from appium import webdriver
import time
from android_driver import AndroidDriver
from selector_main import SelectorMain
from selector_api import SelectorApi
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

capabilities = {
    "platformName": "Android",
    "platformVersion": "9",
    "app": "C:\\Users\\atinkov\\Downloads\\selector_1.0.0_betaRelease82.apk",
    "deviceName": "NNF6R19121001251",
    "appWaitActivity": "com.dgppl.selector.ui.activity.auth.AuthActivity",
    "appWaitPackage": "com.dgppl.selector.beta",
    "newCommandTimeout": "600"
}

app = webdriver.Remote("http://localhost:4723/wd/hub", capabilities)

organization = "АМПП"

wait = WebDriverWait(app, 60)

wait.until(EC.presence_of_element_located((By.ID, "com.dgppl.selector.beta:id/numberDevice")))

device_id = str(app.find_element_by_id("com.dgppl.selector.beta:id/numberDevice").get_attribute("text").split(' ', 2)[2])
print(device_id)

main_page = SelectorMain()

main_page.login()

main_page.activate_device(device_id, 'HUAWEI, CMR-W09, 28', 'Администраторы')

device_api = main_page.get_device_api_key()
print(device_api)

main_page.save_device_settings()

main_page.open_report_data()

main_page.select_organization(organization)

main_page.select_report_period()

main_page.switch_to_report_window()

report_id = main_page.get_report_id()
print(report_id)

report_date = main_page.convert_date()
print(report_date)

api_page = SelectorApi()

api_page.open_page()

api_page.load_report(report_id)

api_page.check_request_status()

main_page.confirm_report()

android = AndroidDriver()

android.open()

android.update('3m')

android.select_org(organization)

android.select_week(report_date)

android.check_report()


