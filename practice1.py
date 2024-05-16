from appium.options.common import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy
from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time

# Define the desired capabilities dictionary in the global scope
desired_caps = {
    "platformName": "Android",
    "automationName": "UiAutomator2",
    "appPackage": "com.google.android.apps.messaging",
    "appActivity": "com.google.android.apps.messaging.ui.ConversationListActivity"
}


# Define the function to create and return the driver instance
def get_driver():
    url = 'http://127.0.0.1:4723'
    appium_options = AppiumOptions().load_capabilities(desired_caps)
    driver = webdriver.Remote(url, options=appium_options)
    return driver


# Define the list of contacts to search
contacts = ['9621490984','Dvs', 'Abhay', 'Arjun', 'Bulu', 'kiran']

# Iterate over each contact and perform search
for contact in contacts:
    driver = get_driver()
    btn1 = driver.find_element(AppiumBy.ID,
                               "com.google.android.apps.messaging:id/welcome_gaia_auto_sign_in_next_button")
    btn1.click()
    time.sleep(5)
    btn2 = driver.find_element(AppiumBy.ID, "com.google.android.apps.messaging:id/welcome_fragment_spam_next_button")
    btn2.click()
    time.sleep(5)
    search = driver.find_element(AppiumBy.ID, "com.google.android.apps.messaging:id/action_zero_state_search")
    search.click()
    time.sleep(5)
    search_box = driver.find_element(AppiumBy.CLASS_NAME, "android.widget.EditText")
    search_box.send_keys(contact)
    time.sleep(5)
    driver.press_keycode(66)

    try:
        # Wait for the conversation title or contact details to appear
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((AppiumBy.ID, 'com.google.android.apps.messaging:id/conversation_title')))
        t = driver.find_element(AppiumBy.ID, 'com.google.android.apps.messaging:id/conversation_title')
        cd = t.text
        print(cd)

        # Check if the contact name or number is found in the title
        if contact in cd:
            print('Contact searched')
        else:
            print('Duplicate Contact')
    except TimeoutException:
        print(f"Contact '{contact}' not found. Skipping...")
    finally:
        # Close the driver after each search iteration
        driver.quit()
