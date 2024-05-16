import time
from appium import webdriver
from appium.options.common import AppiumOptions

def get_driver(deviceId, sysPort):
    desired_caps = {
        "platformName": "Android",
        "automationName": "UiAutomator2",
        "appPackage": "com.whatsapp",
        "systemPort": sysPort,
        "udid": deviceId,
        "appActivity": "com.whatsapp.Main",
        "noReset": True
    }
    url = "http://127.0.0.1:4723/wd/hub"  # URL should end with /wd/hub
    appium_options = AppiumOptions().load_capabilities(desired_caps)
    driver = webdriver.Remote(url, options=appium_options)
    return driver

def jump(driver):
    # Jump to Google Messages
    driver.execute_script('mobile: startActivity', {'component': f'com.google.android.apps.messaging/com.google.android.apps.messaging.main.MainActivity'})
    time.sleep(5)
    driver.execute_script('mobile: startActivity', {'component': f'com.whatsapp/com.whatsapp.HomeActivity'})
    time.sleep(5)
    driver.execute_script('mobile: startActivity', {'component': f'com.google.android.apps.messaging/com.google.android.apps.messaging.main.MainActivity'})
    print("pass")

def test_deviceTest():
    d1 = get_driver('K7272070800016', '8213')
    d2 = get_driver('202303311533480', '8214')
    jump(d1)
    jump(d2)
    d1.quit()
    d2.quit()



