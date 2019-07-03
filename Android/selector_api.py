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

    def load_report(self, report_id):
        #self.madi_report_data = {
# {
#   "reportId": "5721d4e9-747a-4ea6-b097-67fef8420aac",
#   "infoblocks": [
#     {
#       "infoblockId": "039d9cfb-ff66-4fbd-8bfd-ffbeb5f6235b",
#       "infoblockValues": [
#         [
#           "1 квартал 2017",
#           "39076.0",
#           "6837.0",
#           "",
#           "57.0"
#         ],
#         [
#           "2 квартал 2017",
#           "37138.0",
#           "4781.0",
#           "{\"value\":\"-2056\",\"dataType\":{\"value\":\"number\", \"trend\": \"↓\"}}",
#           "60.0"
#         ],
#         [
#           "3 квартал 2017",
#           "30616.0",
#           "3217.0",
#           "{\"value\":\"-1564\",\"dataType\":{\"value\":\"number\", \"trend\": \"↓\"}}",
#           "60.0"
#         ],
#         [
#           "4 квартал 2017",
#           "31576.0",
#           "2552.0",
#           "{\"value\":\"-665\",\"dataType\":{\"value\":\"number\", \"trend\": \"↓\"}}",
#           "60.0"
#         ],
#         [
#           "1 квартал 2019",
#           "23487.0",
#           "2666.0",
#           "{\"value\":\"114\",\"dataType\":{\"value\":\"number\", \"trend\": \"↓\"}}",
#           "57.0"
#         ]
#       ]
#     },
#     {
#       "infoblockId": "c4a69258-648b-4ac1-b913-3e5c401dafb5",
#       "infoblockValues": [
#         [
#           "с 26.02.2018 по 04.03.2018",
#           "60.0",
#           "3113.0",
#           "2882.0",
#           "628.0",
#           "231.0",
#           "2825.0"
#         ],
#         [
#           "",
#           "",
#           "{\"value\":\"-0.009\",\"dataType\":{\"value\":\"percent\", \"trend\": \"↓\", \"mark\": \"%\" }}",
#           "{\"value\":\"-0.009\",\"dataType\":{\"value\":\"percent\", \"trend\": \"↓\", \"mark\": \"%\" }}",
#           "",
#           "{\"value\":\"-0.009\",\"dataType\":{\"value\":\"percent\", \"trend\": \"↓\", \"mark\": \"%\" }}",
#           ""
#         ],
#         [
#           "с 19.02.2018 по 25.02.2018",
#           "60.0",
#           "3140.0",
#           "2907.0",
#           "664.0",
#           "233.0",
#           "2885.0"
#         ],
#         [
#           "Аналогичная неделя 2017 года",
#           "60.0",
#           "3999.0",
#           "3417.0",
#           "906.0",
#           "582.0",
#           "3405.0"
#         ],
#         [
#           "Итого за 2018 год",
#           "57.0",
#           "25553.0",
#           "23487.0",
#           "5888.0",
#           "2066.0",
#           "23171.0"
#         ],
#         [
#           "",
#           "",
#           "{\"value\":\"-0.168\",\"dataType\":{\"value\":\"percent\", \"trend\": \"↓\", \"mark\": \"%\" }}",
#           "{\"value\":\"-0.093\",\"dataType\":{\"value\":\"percent\", \"trend\": \"↓\", \"mark\": \"%\" }}",
#           "",
#           "{\"value\":\"0.572\",\"dataType\":{\"value\":\"percent\", \"trend\": \"↑\", \"mark\": \"%\" }}",
#           ""
#         ],
#         [
#           "Аналогичный период 2017 года",
#           "56.0",
#           "30731.0",
#           "25907.0",
#           "8280.0",
#           "4824.0",
#           "26310.0"
#         ],
#         [
#           "Итого за весь период работы МАДИ",
#           "---",
#           "586091.0",
#           "523060.0",
#           "48475.0",
#           "63031.0",
#           "518782.0"
#         ]
#       ]
#     },
#     {
#       "infoblockId": "cac20336-f7c0-4fc3-983f-c32c64e3718a",
#       "infoblockValues": [
#         [
#           "Отсутствует событие",
#           "2915",
#           "{\"value\":\"0.224\",\"dataType\":{\"value\":\"percent\", \"trend\":\"↑\", \"mark\": \"$\" }}"
#         ],
#         [
#           "Неудовлетворительное качество фото",
#           "2811",
#           "{\"value\":\"-0.216\",\"dataType\":{\"value\":\"percent\", \"trend\":\"↓\", \"mark\": \"%\" }}"
#         ],
#         [
#           "Отсутствует состав",
#           "2798",
#           "{\"value\":\"0.215\",\"dataType\":{\"value\":\"percent\",\"trend\":\"↑\", \"mark\": \"%\" }}"
#         ],
#         [
#           "Переквалифицировано",
#           "2681",
#           "{\"value\":\"-0.206\",\"dataType\":{\"value\":\"percent\", \"trend\":\"↓\" , \"mark\": \"%\" }}"
#         ],
#         [
#           "ТС изменило место стоянки",
#           "1249",
#           "{\"value\":\"0.096\",\"dataType\":{\"value\":\"percent\", \"trend\":\"↑\" , \"mark\": \"%\" }}"
#         ],
#         [
#           "Дорожные службы",
#           "208",
#           "{\"value\":\"-0.016\",\"dataType\":{\"value\":\"percent\", \"trend\":\"↓\" , \"mark\": \"%\" }}"
#         ],
#         [
#           "Маршрутное ТС",
#           "143",
#           "{\"value\":\"0.011\",\"dataType\":{\"value\":\"percent\" ,\"trend\":\"↑\" , \"mark\": \"%\" }}"
#         ],
#         [
#           "Некорректный адрес места нарушения",
#           "143",
#           "{\"value\":\"-0.011\",\"dataType\":{\"value\":\"percent\", \"trend\":\"↓\", \"mark\": \"%\" }}"
#         ],
#         [
#           "Иное",
#           "52",
#           "{\"value\":\"0.004\",\"dataType\":{\"value\":\"percent\", \"trend\":\"↑\" , \"mark\": \"%\" }}"
#         ]
#       ]
#     },
#     {
#       "infoblockId": "d51b4bac-15d0-4dc7-869e-4b2fce4b4fe7",
#       "infoblockValues": [
#         [
#           "с 19.02.2018 по 25.02.2018",
#           "53.0",
#           "127.0",
#           "4.0",
#           ""
#         ],
#         [
#           "с 26.02.2018 по 04.03.2018",
#           "114.0",
#           "62.0",
#           "33.0",
#           "{\"value\":\"-0.512\",\"dataType\":{\"value\":\"percent\", \"trend\": \"↓\", \"mark\": \"%\" }}"
#         ]
#       ]
#     },
#     {
#       "infoblockId": "8bbf807a-ce15-47f8-9e34-8052d21b057f",
#       "infoblockValues": [
#         [
#           "АПК \"ПаркРайт\"",
#           "7057.0",
#           "77.0",
#           "{\"value\":\"0.011\",\"dataType\":{\"value\":\"percent\", \"mark\": \"%\"}}"
#         ],
#         [
#           "АПК \"ПаркРайт\" на НГПТ",
#           "233.0",
#           "1.0",
#           "{\"value\":\"0.004\",\"dataType\":{\"value\":\"percent\", \"mark\": \"%\"}}"
#         ],
#         [
#           "ПАК \"ПМ\"",
#           "4944.0",
#           "52.0",
#           "{\"value\":\"0.011\",\"dataType\":{\"value\":\"percent\", \"mark\": \"%\"}}"
#         ],
#         [
#           "АПК \"Мобильный инспектор\"",
#           "2830.0",
#           "12.0",
#           "{\"value\":\"0.004\",\"dataType\":{\"value\":\"percent\", \"mark\": \"%\"}}"
#         ],
#         [
#           "АПК \"ПаркНет\"",
#           "554.0",
#           "0.0",
#           "0.0"
#         ],
#         [
#           "АПК \"Ситивизор\"",
#           "0.0",
#           "0.0",
#           ""
#         ],
#         [
#           "Стрелка +",
#           "883.0",
#           "42.0",
#           "{\"value\":\"0.048\",\"dataType\":{\"value\":\"percent\", \"mark\": \"%\"}}"
#         ],
#         [
#           "Стрелка 360",
#           "39.0",
#           "0.0",
#           "0.0"
#         ],
#         [
#           "АПК \"ПаркНет-М\"",
#           "517.0",
#           "1.0",
#           "{\"value\":\"0.002\",\"dataType\":{\"value\":\"percent\", \"mark\": \"%\"}}"
#         ]
#       ]
#     },
#     {
#       "infoblockId": "c72adda9-11f8-4498-b9dd-44aab14e8449",
#       "infoblockValues": [
#         [
#           "Аналогичный период 2017 года",
#           "79184.0",
#           "",
#           "43843.0",
#           "",
#           "24193.0",
#           ""
#         ],
#         [
#           "С 01.01.2018 по 04.03.2018",
#           "54336.0",
#           "{\"value\":\"-0.314\",\"dataType\":{\"value\":\"percent\", \"trend\": \"↓\", \"mark\": \"%\" }}",
#           "46138.0",
#           "{\"value\":\"0.052\",\"dataType\":{\"value\":\"percent\", \"trend\": \"↑\", \"mark\": \"%\" }}",
#           "20130.0",
#           "{\"value\":\"-0.168\",\"dataType\":{\"value\":\"percent\", \"trend\": \"↓\", \"mark\": \"%\" }}"
#         ]
#       ]
#     }
#   ]
# }}
#        self.madi_report_data = self.madi_report_data[1:]
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
        file = open('madi_json.txt', 'r', encoding='utf8').read()
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