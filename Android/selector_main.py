from base import SelectorBasePage
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver

class SelectorMain():

    def __init__(self):
        SelectorBasePage.__init__(self)
        self.driver = SelectorBasePage.driver
        self.wait = WebDriverWait(self.driver, 30)

    def login(self):
        self.driver.maximize_window()
        self.driver.get('https://selector.srvdev.ru/')
        self.wait.until(EC.presence_of_element_located((By.XPATH, '//*[@name="login"]')))
        login = 'АТиньков'
        password = '486250$Sel'
        self.driver.find_element_by_xpath('//*[@name="login"]').send_keys(login)
        self.driver.find_element_by_xpath('//*[@name="password"]').send_keys(password)
        self.driver.find_element_by_xpath('//*[@type="submit"]').click()
        self.wait.until(EC.presence_of_element_located((By.XPATH, '//*[@class="navbar-brand"]')))

    def activate_device(self, device_id, role):
        for element in self.driver.find_elements_by_xpath('//*[@class="nav navbar-nav"]/li'):
            if element.text == "Администрирование":
                element.click()
        self.wait.until(EC.presence_of_element_located((By.XPATH, '//*[@class="dropdown open"][@ng-show="vm.menuItemsVisibility.showAdminSettings"]')))
        for element in self.driver.find_elements_by_xpath('//*[@class="dropdown open"][@ng-show="vm.menuItemsVisibility.showAdminSettings"]//li'):
            if element.text == "Устройства":
                element.click()
        self.wait.until(EC.presence_of_element_located((By.XPATH,'//*[text()="Очистить"]')))
        self.driver.find_element_by_xpath('//*[text()="Очистить"]').click()
        time.sleep(3)
        self.driver.find_element_by_id('filter_fingerprint').send_keys(device_id)
        self.driver.find_element_by_xpath("//*[text()='Найти']").click()
        time.sleep(2)
        self.wait.until(EC.presence_of_element_located((By.XPATH,'//div[@ds-table="vm.table"]')))
        self.driver.find_element_by_xpath('//span[@title="Редактировать"]').click()
        time.sleep(3)
        self.driver.find_element_by_xpath('//*[@id="page-top"]/div[3]/div[2]/div/div/div/div/div[3]/div/div/div/div[8]/div/div/div/div/div[2]/div/div').click()
        self.wait.until(EC.presence_of_element_located((By.XPATH, '//div[@class="btn-group open"]')))
        for element in self.driver.find_elements_by_xpath('//div[@class="btn-group open"]/ul/li'):
            if role in element.text:
                element.click()
        self.wait.until(EC.presence_of_element_located((By.XPATH, '//button[@title="Администраторы"]')))
        self.driver.find_element_by_xpath('//button[@title="Администраторы"]').click()
        self.driver.find_element_by_xpath('// *[contains(text(), "Подтвержден?")]').click()

    def get_device_api_key(self):
        return self.driver.find_element_by_xpath('//*[@id="field_apiKey"]').text

    def save_device_settings(self):
        self.driver.find_element_by_xpath('//button[contains(text(), "Применить")]').click()
        time.sleep(2)

    def open_report_data(self):
        self.wait.until(EC.element_to_be_clickable ((By.XPATH, '//*[@id="topbar"]//a[@href="/upload/reports"]')))
        for element in self.driver.find_elements_by_xpath('//*[@id="topbar"]/ul[@class="nav navbar-nav"]/li'):
            if element.text == "Загрузка данных":
                element.click()
        self.wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="topbar"]//a[@href="/upload/reports"]')))
        self.driver.find_element_by_xpath('//*[@id="topbar"]//a[@href="/upload/reports"]').click()

    def select_organization(self, report_name):
        self.wait.until(EC.presence_of_element_located((By.XPATH, '//button[@class="btn btn-default"]')))
        self.driver.find_element_by_xpath('//button[@class="btn btn-default"]').click()
        time.sleep(3)
        self.driver.find_element_by_xpath('//button[@class="multiselect dropdown-toggle btn btn-default form-control ng-isolate-scope"]').click()
        for element in self.driver.find_elements_by_xpath('//ul[@class="multiselect-container dropdown-menu"]/li'):
            if report_name in element.text:
                element.click()
        self.driver.find_element_by_xpath('//button[text()="Найти"]').click()
        time.sleep(1)
        self.wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="container"]//tr[1]//a[contains(text(), "'+str(report_name)+'")]')))

    def select_report_period(self):
        row=1
        for element in self.driver.find_elements_by_xpath('//tbody[@class="ng-scope"]/tr'):
            if self.driver.find_element_by_xpath('//table/tbody/tr[' + str(row) + ']/td[8]/div/span').text != '0':
                if self.driver.find_element_by_xpath('//table/tbody/tr[' + str(row) + ']/td[9]/div/span').text == '0':
                    self.driver.find_element_by_xpath('//tbody[@class="ng-scope"]/tr[' + str(row) + ']/td[2]/div/a').click()
                    break
                else:
                    row += 1
            else:
                self.driver.find_element_by_xpath('//tbody[@class="ng-scope"]/tr[' + str(row) + ']/td[2]/div/a').click()
                break

    def switch_to_report_window(self):
        time.sleep(1)
        self.driver.switch_to.window(self.driver.window_handles[1])
        self.wait.until(EC.presence_of_element_located((By.XPATH, '//h1[text()="Данные по инфоблокам для отчета  "]')))

    # def get_report_date(self):
    #     self.wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="container"]//strong[@ng-class="vm.getGroupRowClass()"]')))
    #     target = self.driver.find_element_by_xpath('//*[@id="container"]//strong[@ng-class="vm.getGroupRowClass()"]')
    #     actions = ActionChains(self.driver)
    #     actions.move_to_element(target)
    #     actions.perform()
    #     date = self.driver.find_element_by_xpath('//*[@id="container"]//strong[@ng-class="vm.getGroupRowClass()"]').text.split('период ', 2)[1]
    #     start_date = date.split('-', 1)[0][:-5]
    #     end_date = date.split('-', 1)[1][1:]
    #     period = start_date + '- ' + end_date
    #     report_period = period.replace('.06.', ' июн. ')
    #     return report_period

    def convert_date(self):
        self.wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="container"]//strong[@ng-class="vm.getGroupRowClass()"]')))
        target = self.driver.find_element_by_xpath('//*[@id="container"]//strong[@ng-class="vm.getGroupRowClass()"]')
        actions = ActionChains(self.driver)
        actions.move_to_element(target)
        actions.perform()
        month = [['01','янв.'],['02','февр.'],['03','мар.'],['04','апр.'],['05','мая'],['06','июн.'],['07','июл.'],['08','авг.'],['09','сент.'],['10','окт.'],['11','нояб.'],['12','дек.']]
        date = self.driver.find_element_by_xpath('//*[@id="container"]//strong[@ng-class="vm.getGroupRowClass()"]').text.split('период ', 2)[1]
        start_date = date.split('-', 1)[0][:-5]
        new_start_date = start_date.split('.',2)
        for i in range(12):
            if new_start_date[1] == month[i][0]:
                new_start_date[1] = month[i][1]
                start_date = ' '.join(new_start_date)[:-1]
        end_date = date.split('-', 1)[1][1:]
        new_end_date = end_date.split('.', 2)
        for i in range(12):
            if new_end_date[1] == month[i][0]:
                new_end_date[1] = month[i][1]
                end_date = ' '.join(new_end_date)
        period = start_date + ' - ' + end_date
        return period

    def get_report_id(self):
        id = self.driver.current_url.split('infoblocks/', 1)[1]
        report_str = '''{
  "reportId": "'''+str(id)+'''",
  '''
        return report_str

    def confirm_report(self):
        #(// *[ @ id = "container"] // tr / td[9] / div / span / i) xpath для признака предоставлен для инфоблока
        #driver.find_elements_by_xpath('//*[@id="container"]//tr[@ng-class="vm.getRowClass(item)"]') список всех инфоблоков
        #('// *[ @ id = "container"] // tr['+str(y)+'] // div / input') - чекбокс инфоблока с порядковым номером равным y
        self.driver.switch_to.window(self.driver.window_handles[1])
        self.wait.until(EC.presence_of_element_located((By.XPATH, '//h1[text()="Данные по инфоблокам для отчета  "]')))
        self.driver.refresh()
        self.wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="container"]//span[text()="100"]')))
        self.driver.find_element_by_xpath('//*[@id="container"]//span[text()="100"]').click()
        time.sleep(5)
        y=1
        for element in self.driver.find_elements_by_xpath('//*[@id="container"]//tr[@ng-class="vm.getRowClass(item)"]'):
            try:
                if bool(self.driver.find_element_by_xpath('// *[ @ id = "container"] // tr[' + str(y) + '] / td[9] / div / span / i')) == True:
                    try:
                        if bool(self.driver.find_element_by_xpath('// *[ @ id = "container"] // tr[' + str(y) + '] / td[11] / div / span / i')) == True:
                            y += 1
                    except:
                        self.driver.find_element_by_xpath('// *[ @ id = "container"] // tr[' + str(y) + '] // div / input').click()
                        y += 1
            except:
                y += 1
        self.driver.find_element_by_xpath('//*[@id="container"]//button[@title="Подтвердить от поставщика"]').click()
        self.wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="page-top"]//button[text()="Подтвердить"]')))
        self.driver.find_element_by_xpath('//*[@id="page-top"]//button[text()="Подтвердить"]').click()
        time.sleep(2)
        y = 1
        for element in self.driver.find_elements_by_xpath('//*[@id="container"]//tr[@ng-class="vm.getRowClass(item)"]'):
            try:
                if bool(self.driver.find_element_by_xpath('// *[ @ id = "container"] // tr[' + str(y) + '] / td[9] / div / span / i')) == True:
                    self.driver.find_element_by_xpath('// *[ @ id = "container"] // tr[' + str(y) + '] // div / input').click()
                    y += 1
            except:
                y += 1
        time.sleep(2)
        self.driver.find_element_by_xpath('// *[ @ id = "page-top"] // button[ @ title = "Подтвердить от ДТиРДТИ"]').click()
        self.wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="page-top"]//button[text()="Подтвердить отчёт"]')))
        self.driver.find_element_by_xpath('//*[@id="page-top"]//button[text()="Подтвердить отчёт"]').click()


