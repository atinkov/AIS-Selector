from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

class SelectorApi():

    def __init__(self):
        self.driver = webdriver.Chrome('C:\chromedriver\chromedriver.exe')
        self.wait = WebDriverWait(self.driver, 600)


    def open_page(self):
        self.driver.get('https://selector.srvdev.ru/api/v1?apiKey=d46a137a-1825-441d-b99d-c441f1e2e788#!/')

    def load_report(self, report_id, organization):
        if organization == 'МАДИ':
            file = open('madi_json.txt', 'r', encoding='utf8').read()
        elif organization == 'АМПП':
            file = open('ampp_json.txt', 'r', encoding='utf8').read()

        self.wait.until(EC.presence_of_element_located((By.XPATH, '//a[@href="#!/Report_запросы"]')))
        self.driver.find_element_by_xpath('//a[@href="#!/Report_запросы"]').click()
        self.wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="Report_запросы_post_report_data"]/div[1]/ul')))
        time.sleep(1)
        self.driver.find_element_by_css_selector('#Report_запросы_post_report_data > div.heading > h3 > span.path > a').click()
        time.sleep(2)
        target = self.driver.find_element_by_xpath('//*[@id="Report_запросы_post_report_data_content"]//input[@value="Try it out!"]')
        actions = ActionChains(self.driver)
        actions.move_to_element(target)
        actions.perform()
        #for element in range(10):
        #    self.driver.find_element_by_tag_name('body').send_keys(Keys.ARROW_DOWN)
        time.sleep(2)
        self.driver.find_element_by_xpath('//*[@id="Report_запросы_post_report_data_content"]/form/table[1]/tbody/tr/td[2]/textarea').send_keys(report_id)
        self.driver.find_element_by_xpath('//*[@id="Report_запросы_post_report_data_content"]/form/table[1]/tbody/tr/td[2]/textarea').send_keys(file)
        #self.wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="Report_запросы_post_report_data_content"]//h4[text()="Response Body"]')))
        self.driver.find_element_by_xpath('//*[@id="Report_запросы_post_report_data_content"]//input[@value="Try it out!"]').click()
        self.wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="Report_запросы_post_report_data_content"]/div[3]/div[5]/pre')))
        target = self.driver.find_element_by_xpath('//*[@id="Report_запросы_post_report_data_content"]/div[3]/div[5]/pre')
        actions = ActionChains(self.driver)
        actions.move_to_element(target)
        actions.perform()
        assert self.driver.find_element_by_xpath('//*[@id="Report_запросы_post_report_data_content"]/div[3]/div[4]/pre').text=='200'

    def check_request_status(self):
        request_id = self.driver.find_element_by_xpath('//div[@class="block response_body json"]//span[@class="string"]').text.replace('"', '')
        self.driver.find_element_by_xpath('//li[@class="get operation"]//a[text()="/report/data/{id}"]').click()
        self.wait.until(EC.presence_of_element_located((By.XPATH, '//div[@id="Report_запросы_get_report_data_id_content"]//input[@class="parameter required"]')))
        self.driver.find_element_by_xpath('//div[@id="Report_запросы_get_report_data_id_content"]//input[@class="parameter required"]').send_keys(request_id)
        self.driver.find_element_by_xpath('//div[@id="Report_запросы_get_report_data_id_content"]//input[@class="submit"]').click()
        assert self.driver.find_element_by_xpath('//div[@id="Report_запросы_get_report_data_id_content"]//div[@class="block response_code"]').text == '200'
        response = '''{
          "status": 2,
          "responseCode": 200,
          "responseData": {
            "isSuccessfullyLoaded": true,
            "errorMessage": ""
          }
        }'''
        assert self.driver.find_element_by_xpath('//*[@id="Report_запросы_get_report_data_id_content"]//pre[@class="json"]').text == response