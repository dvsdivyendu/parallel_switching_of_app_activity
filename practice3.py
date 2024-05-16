import time

from appium import webdriver
from appium.options.common import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy
from selenium.common import NoSuchElementException
from appium.webdriver.appium_service import AppiumService
appium_service=AppiumService()
appium_service.start(args=['--address', '127.0.0.1', '--port', '4723', '--base-path', '/wd/hub'])

desired_caps = {
    "platformName": "Android",
    "automationName": "UiAutomator2",
    "appPackage": "com.whatsapp",
    "appActivity": "com.whatsapp.Main",
    "noReset": "true"

}
def get_driver():
    url = 'http://127.0.0.1:4723/wd/hub'
    appium_options = AppiumOptions().load_capabilities(desired_caps)
    driver = webdriver.Remote(url, options=appium_options)
    return driver

driver = get_driver()
driver.execute_script('mobile: startActivity',{'component': f'com.google.android.apps.messaging/com.google.android.apps.messaging.ui.ConversationListActivity'})
time.sleep(5)
driver.execute_script('mobile: startActivity',{'component': f'com.whatsapp/com.whatsapp.HomeActivity'})
time.sleep(5)
driver.execute_script('mobile: startActivity',{'component': f'com.google.android.apps.messaging/com.google.android.apps.messaging.ui.ConversationListActivity'})
appium_service.stop()


