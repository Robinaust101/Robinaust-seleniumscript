from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By


driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))


driver.get("https://demo.opencart.com/")

# Step 3: Click MyAccount
my_account = driver.find_element(By.LINK_TEXT, 'My Account')
my_account.click()

# Step 4: Click on Login
login = driver.find_element(By.LINK_TEXT, 'Login')
login.click()

# Step 5: Enter/Type Email
email = driver.find_element(By.ID, "input-email")

# Email attribute
print("ID of Email attribute is: " + email.get_attribute("id"))

# Get CSS value
print("Height of Email is: " + email.value_of_css_property("height"))
# Test CSS value
expected_height = "34px"
actual_height = email.value_of_css_property("height")
if expected_height == actual_height:
    print("Test passed.Height matched.")
else:
    print("Test failed.Actual height is: " + actual_height)

email.clear()
email.send_keys("testemail@gmail.com")

# Step 6: Enter/Type password
password_is_display = driver.find_element(By.ID, "input-password").is_displayed()
print(password_is_display)
password_is_enable = driver.find_element(By.ID, "input-password").is_enabled()
print(password_is_enable)

password = driver.find_element(By.ID, "input-password")
password.clear()
password.send_keys("123456")

# Step 7: Click Login button
login_btn = driver.find_element(By.XPATH, '//*[@id="content"]/div/div[2]/div/form/input')
login_btn.click()


driver.close()