from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.action_chains import ActionChains


driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))

driver.get("https://www.browserstack.com/test-on-the-right-mobile-devices")

driver.execute_script("window.scrollBy(0,500)", "")

pdf = driver.find_element(By.XPATH, '//*[@id="test_on_the_right_mobile_devices"]/main/section[1]/div[2]/div/div/div/div[1]/div[2]/div[2]/div[1]/a')

pdf.click()


