import time

from appium.options.common import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy
from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, StaleElementReferenceException

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
contacts = ['Bulu', 'kiran']

# Iterate over each contact and perform search
for contact in contacts:
    driver = get_driver()
    try:
        btn1 = WebDriverWait(driver, 10).until(EC.presence_of_element_located(
            (AppiumBy.ID, "com.google.android.apps.messaging:id/welcome_gaia_auto_sign_in_next_button")))
        btn1.click()

        btn2 = WebDriverWait(driver, 10).until(EC.presence_of_element_located(
            (AppiumBy.ID, "com.google.android.apps.messaging:id/welcome_fragment_spam_next_button")))
        btn2.click()

        # Handle popups if present
        try:
            popup = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((AppiumBy.ID,
                                                'com.google.android.apps.messaging:id/messages_title')))
            # Perform action to handle popup
            popup.click()  # Example action, replace with your action to handle the popup
        except TimeoutException:
            pass  # Continue execution if popup not found

        search = WebDriverWait(driver, 10).until(EC.presence_of_element_located(
            (AppiumBy.ID, "com.google.android.apps.messaging:id/action_zero_state_search")))
        search.click()

        search_box = WebDriverWait(driver, 10).until(EC.presence_of_element_located(
            (AppiumBy.CLASS_NAME, "android.widget.EditText")))
        search_box.send_keys(contact)

        driver.press_keycode(66)

        try:
            # Check if the element is present before trying to click
            try:
                element = WebDriverWait(driver, 10).until(EC.presence_of_element_located(
                    (AppiumBy.XPATH,
                     "(//*[@id='com.google.android.apps.messaging:id/zero_state_search_box_dropdown_item'])[1]")))
                element.click()
                print('Duplicate Contact')
            except TimeoutException:
                pass  # Continue execution if element not found

            try:
                element = WebDriverWait(driver, 10).until(EC.presence_of_element_located(
                    (AppiumBy.ID, 'android:id/button1')))
                element.click()
                # Wait for the conversation title or contact details to appear
                t = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located(
                        (AppiumBy.ID, 'com.google.android.apps.messaging:id/conversation_title')))
                cd = t.text
                print(cd)

                # Check if the contact name or number is found in the title
                if contact in cd:
                    print('Contact searched')

            except (TimeoutException, StaleElementReferenceException):
                print(f"Contact '{contact}' not found. Skipping...")
        finally:
            # Close the driver after each search iteration
            driver.quit()
    except Exception as e:
        print(f"Error occurred while processing contact '{contact}': {str(e)}")
