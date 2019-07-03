from selenium import webdriver
from android_base import AndroidBase
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class AndroidDriver():

    def __init__(self):
        AndroidBase.__init__(self)
        self.android = AndroidBase.android
        self.wait = WebDriverWait(self.android, 300)
        self.touch = AndroidBase.actions

    def get_device_id(self):
        self.wait.until(EC.element_to_be_clickable((By.ID, "com.dgppl.selector.beta:id/numberDevice")))
        return str(self.android.find_element_by_id("com.dgppl.selector.beta:id/numberDevice").text.split(' ', 2)[2])

    def change_update_period(self, period):
        self.android.find_element_by_id('com.dgppl.selector.beta:id/logoIcon').click()
        time.sleep(1)
        self.android.find_element_by_id('com.dgppl.selector.beta:id/settingsBtn').click()
        time.sleep(1)
        if period == '2w':
            self.android.find_element_by_id('com.dgppl.selector.beta:id/settingsDialogTwoWeeksCheck').click()
        elif period == '1m':
            self.android.find_element_by_id('com.dgppl.selector.beta:id/settingsDialogMonthCheck').click()
        elif period == '3m':
            self.android.find_element_by_id('com.dgppl.selector.beta:id/settingsDialogQuarterCheck').click()
        elif period == '6m':
            self.android.find_element_by_id('com.dgppl.selector.beta:id/settingsDialogYearHalfCheck').click()
        elif period == '1y':
            self.android.find_element_by_id('com.dgppl.selector.beta:id/settingsDialogYearCheck').click()
        elif period == 'all':
            self.android.find_element_by_id('com.dgppl.selector.beta:id/settingsDialogAllTimeCheck').click()
        self.android.find_element_by_id('com.dgppl.selector.beta:id/settingsCloseBtn').click()
        time.sleep(1)

    def update(self, period=None):
        if period != None:
            self.android.find_element_by_id('com.dgppl.selector.beta:id/logoIcon').click()
            time.sleep(1)
            self.android.find_element_by_id('com.dgppl.selector.beta:id/settingsBtn').click()
            time.sleep(1)
            if period == '2w':
                self.android.find_element_by_id('com.dgppl.selector.beta:id/settingsDialogTwoWeeksCheck').click()
                self.android.find_element_by_id('com.dgppl.selector.beta:id/settingsCloseBtn').click()
                time.sleep(1)
            elif period == '1m':
                self.android.find_element_by_id('com.dgppl.selector.beta:id/settingsDialogMonthCheck').click()
                self.android.find_element_by_id('com.dgppl.selector.beta:id/settingsCloseBtn').click()
                time.sleep(1)
            elif period == '3m':
                self.android.find_element_by_id('com.dgppl.selector.beta:id/settingsDialogQuarterCheck').click()
                self.android.find_element_by_id('com.dgppl.selector.beta:id/settingsCloseBtn').click()
                time.sleep(1)
            elif period == '6m':
                self.android.find_element_by_id('com.dgppl.selector.beta:id/settingsDialogYearHalfCheck').click()
                self.android.find_element_by_id('com.dgppl.selector.beta:id/settingsCloseBtn').click()
                time.sleep(1)
            elif period == '1y':
                self.android.find_element_by_id('com.dgppl.selector.beta:id/settingsDialogYearCheck').click()
                self.android.find_element_by_id('com.dgppl.selector.beta:id/settingsCloseBtn').click()
                time.sleep(1)
            elif period == 'all':
                self.android.find_element_by_id('com.dgppl.selector.beta:id/settingsDialogAllTimeCheck').click()
                self.android.find_element_by_id('com.dgppl.selector.beta:id/settingsCloseBtn').click()
                time.sleep(1)
        self.android.find_element_by_id('com.dgppl.selector.beta:id/startSyncBtn').click()
        self.wait.until(EC.presence_of_element_located((By.ID, "com.dgppl.selector.beta:id/startSyncBtn")))

    def select_org(self, organization):
        for element in self.android.find_elements_by_xpath('//android.widget.TextView'):
            if organization == element.text:
                element.click()
                break

    def select_week(self, report_date):
        self.wait.until(EC.presence_of_element_located((By.ID, "com.dgppl.selector.beta:id/valueNextWeek")))
        self.android.find_element_by_id('com.dgppl.selector.beta:id/valueNextWeek').click()

        while self.android.find_element_by_id('com.dgppl.selector.beta:id/date').text != report_date:
            self.android.find_element_by_id('com.dgppl.selector.beta:id/valuePrevWeek').click()
        self.android.find_element_by_id('com.dgppl.selector.beta:id/date').click()

    def check_report(self):
        time.sleep(1)
        self.android.find_element_by_xpath('//android.widget.FrameLayout[3]//android.view.ViewGroup[1]/android.widget.TextView[2]').click()
        m=[]
        for element in self.android.find_elements_by_xpath('//android.widget.FrameLayout[2]/android.view.ViewGroup/android.widget.FrameLayout[1]//android.view.ViewGroup/android.widget.TextView[2]'):
            element.click()
            self.touch.press(x=1800, y=1200).move_to(x=1800, y=700).release().perform()
            m.append(element.text)
        self.touch.press(x=350, y=1080).move_to(x=350, y=900).release().perform()
        time.sleep(1)
        for element in self.android.find_elements_by_xpath('//android.widget.FrameLayout[2]/android.view.ViewGroup/android.widget.FrameLayout[1]//android.view.ViewGroup/android.widget.TextView[2]'):
            if element.text not in m:
                element.click()
                self.touch.press(x=1800, y=1200).move_to(x=1800, y=700).release().perform()


