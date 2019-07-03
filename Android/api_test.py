from selenium import webdriver
from appium import webdriver
import time
from selector_main import SelectorMain
from selector_api import SelectorApi
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

capabilities = {
    "platformName": "Android",
    "platformVersion": "9",
    "app": "C:\\Users\\atinkov\\Downloads\\selector_1.0.0_betaRelease82.apk",
    "deviceName": "Android SDK built for x86",
    "appWaitActivity": "com.dgppl.selector.ui.activity.auth.AuthActivity",
    "appWaitPackage": "com.dgppl.selector.beta",
    "newCommandTimeout": "600"
}

app = webdriver.Remote("http://localhost:4723/wd/hub", capabilities)

organization = "МАДИ"

wait = WebDriverWait(app, 600)

wait.until(EC.presence_of_element_located((By.ID, "com.dgppl.selector.beta:id/numberDevice")))

device_id = str(app.find_element_by_id("com.dgppl.selector.beta:id/numberDevice").get_attribute("text").split(' ', 2)[2])
print(device_id)

main_page = SelectorMain()

main_page.login()

main_page.activate_device(device_id, 'HUAWEI, CMR-W09, 28', 'Администраторы')

device_api = main_page.get_device_api_key()
print(device_api)

main_page.save_device_settings()

wait.until(EC.presence_of_element_located((By.ID, "com.dgppl.selector.beta:id/logoTitle")))

assert app.find_element_by_id('com.dgppl.selector.beta:id/logoTitle')

main_page.load_report_open(organization)

main_page.select_report_period()

main_page.switch_to_report_window()

main_page.switch_to_report_window()

report_id = main_page.get_report_id()
print(report_id)

report_date = main_page.convert_date()
print(report_date)

api_page = SelectorApi()

api_page.open_page()

api_page.load_report(report_id)

main_page.confirm_report()

app.find_element_by_id('com.dgppl.selector.beta:id/startSyncBtn').click()

wait.until(EC.presence_of_element_located((By.ID, "com.dgppl.selector.beta:id/startSyncBtn")))

for element in app.find_elements_by_xpath('//android.widget.TextView'):
    if organization == element.text:
        element.click()
        break

wait.until(EC.presence_of_element_located((By.ID, "com.dgppl.selector.beta:id/valueNextWeek")))
app.find_element_by_id('com.dgppl.selector.beta:id/valueNextWeek').click()

while app.find_element_by_id('com.dgppl.selector.beta:id/date').text != report_date:
    app.find_element_by_id('com.dgppl.selector.beta:id/valuePrevWeek').click()

app.find_element_by_id('com.dgppl.selector.beta:id/date').click()


