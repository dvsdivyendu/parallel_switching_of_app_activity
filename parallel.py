import time
from appium import webdriver
from appium.options.common import AppiumOptions

from appium.webdriver.appium_service import AppiumService
from appium.webdriver.common.appiumby import AppiumBy

from selenium.common import NoSuchElementException
from appium.webdriver.appium_service import AppiumService

def get_driver(deviceId, sysPort):
    desired_caps = {
        "platformName": "Android",
        "automationName": "UiAutomator2",
        "appPackage": "com.whatsapp",
        "deviceName": sysPort,  # Use sysPort as deviceName, assuming it contains the device name
        "udid": deviceId,
        "appActivity": "com.whatsapp.Main",
        "noReset": True  # Use boolean value instead of string
    }
    url = 'http://127.0.0.1:4723/wd/hub'
    appium_options = AppiumOptions().load_capabilities(desired_caps)
    driver = webdriver.Remote(url, options=appium_options)
    return driver

def jump(driver):
    # Jump to Google Messages
    driver.start_activity('com.google.android.apps.messaging', 'com.google.android.apps.messaging.ui.ConversationListActivity')
    time.sleep(5)
    # Jump to WhatsApp
    driver.start_activity('com.whatsapp', 'com.whatsapp.HomeActivity')
    time.sleep(5)
    # Jump back to Google Messages
    driver.start_activity('com.google.android.apps.messaging', 'com.google.android.apps.messaging.ui.ConversationListActivity')
    time.sleep(5)

def test_deviceTest():
    d1 = get_driver('202303311533480', '8200')
    d2 = get_driver('K7272070800016', '8201')
    jump(d1)
    jump(d2)


if __name__ == "__main__":
    appium_service = AppiumService()
    appium_service.start(args=['--address', '127.0.0.1', '--port', '4723', '--base-path', '/wd/hub'])
    test_deviceTest()
    appium_service.stop()
