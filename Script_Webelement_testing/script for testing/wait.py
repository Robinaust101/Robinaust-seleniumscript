from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


"""
#Other script for wait.
import time
time.sleep(Sec value)
"""
driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
driver.get("https://demo.opencart.com/")
  # 30 seconds

my_account = driver.find_element(By.LINK_TEXT, 'My Account')
# Implicit Wait / Soft wait
driver.implicitly_wait(10)
my_account.click()
login = driver.find_element(By.LINK_TEXT, 'Login')
login.click()

# email = driver.find_element(By.ID, "input-email")
# email.clear()
# email.send_keys("testemail@gmail.com")

# Explicit wait / hard wait
email = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, "input-email")))
email.clear()
email.send_keys("testemail@gmail.com")

password = driver.find_element(By.ID, "input-password")
password.clear()
password.send_keys("123456")


login_btn = driver.find_element(By.XPATH, '//*[@id="content"]/div/div[2]/div/form/input')
login_btn.click()

driver.close()