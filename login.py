from appium import webdriver
from appium.options.android import UiAutomator2Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time

options = UiAutomator2Options()
options.platform_name = "Android"
options.device_name = "A54-Mega"
options.app_package = "com.starwarsapp"
options.app_activity = "com.starwarsapp.MainActivity"
options.automation_name = "UiAutomator2"
options.no_reset = True  

# START DRIVER
driver = webdriver.Remote(
    "http://127.0.0.1:4723",  
    options=options
)

wait = WebDriverWait(driver, 15)

# EMAIL FIELD
email_field = wait.until(
    EC.presence_of_element_located(
        ("xpath", "//android.widget.EditText[@hint='E-mail address']")
    )
)
email_field.clear()
email_field.send_keys("user1@gmail.com")

# PASSWORD FIELD
password_field = wait.until(
    EC.presence_of_element_located(
        ("xpath", "//android.widget.EditText[@hint='Password']")
    )
)
password_field.clear()
password_field.send_keys("Mega2017.")

# LOGIN BUTTON
login_button = wait.until(
    EC.element_to_be_clickable(
        ("xpath", "//android.view.ViewGroup[@content-desc='LOGIN']")
    )
)
login_button.click()

# ===== ASSERTION LOGIN =====
try:
    home_element = wait.until(
        EC.presence_of_element_located(
            ("xpath", "//android.view.ViewGroup[@content-desc='Joined Group']")
        )
    )

    assert home_element.is_displayed()
    print("PASS | LOGIN SUCCESS: Home screen displayed")

except TimeoutException:
    print("FAIL | LOGIN FAILED: Home screen not found")
    raise
    
# driver.quit()
