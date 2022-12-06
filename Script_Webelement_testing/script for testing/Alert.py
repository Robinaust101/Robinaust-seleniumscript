from selenium import webdriver

from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))

driver.get("https://the-internet.herokuapp.com/javascript_alerts")

# Normal Alert
Normal_alert = driver.find_element(By.XPATH, '//*[@id="content"]/div/ul/li[1]/button')
Normal_alert.click()
title_normalAlert = driver.switch_to.alert.text
print('Normal Alert Title is: ' + title_normalAlert)
driver.switch_to.alert.accept()  # Ok

# Confirmation Alert
Normal_alert = driver.find_element(By.XPATH, '//*[@id="content"]/div/ul/li[2]/button')
Normal_alert.click()
title_confirmAlert = driver.switch_to.alert.text
print('Confirm Alert Title is: ' + title_confirmAlert)
driver.switch_to.alert.dismiss()  # Cancel

# Prompt Alert
Normal_alert = driver.find_element(By.XPATH, '//*[@id="content"]/div/ul/li[3]/button')
Normal_alert.click()
title_promptAlert = driver.switch_to.alert.text
print('Prompt Alert Title is: ' + title_promptAlert)
driver.switch_to.alert.send_keys('Test Automation')
driver.switch_to.alert.accept()  # Ok