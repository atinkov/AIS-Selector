from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction

class AndroidBase(object):

    capabilities = {
        "platformName": "Android",
        "platformVersion": "9",
        "app": "C:\\Users\\atinkov\\Downloads\\selector_1.0.0_betaRelease82.apk",
        "deviceName": "Android SDK built for x86",
        "appWaitActivity": "com.dgppl.selector.ui.activity.auth.AuthActivity",
        "appWaitPackage": "com.dgppl.selector.beta",
        "newCommandTimeout": "600"
    }
    android = webdriver.Remote("http://localhost:4723/wd/hub", capabilities)
    actions = TouchAction()