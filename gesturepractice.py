import time

from appium import webdriver
from appium.options.common import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy
from selenium.common import NoSuchElementException

desired_caps = {
    "platformName": "Android",
    "automationName": "UiAutomator2",
    "appPackage": "com.whatsapp",
    "appActivity": "com.whatsapp.Main",
    "noReset": "true"

}
def get_driver():
    url = 'http://127.0.0.1:4723'
    appium_options = AppiumOptions().load_capabilities(desired_caps)
    driver = webdriver.Remote(url, options=appium_options)
    return driver

driver = get_driver()

driver.execute_script('mobile: startActivity',{'component': f'com.whatsapp/com.whatsapp.HomeActivity'})
time.sleep(5)
element = driver.find_element(AppiumBy.XPATH,'//android.widget.TextView[@resource-id="com.whatsapp:id/conversations_row_contact_name" and @text="Testgroup"]')
driver.scroll(origin_el=None,destination_el=element,duration=5)
element.click()



