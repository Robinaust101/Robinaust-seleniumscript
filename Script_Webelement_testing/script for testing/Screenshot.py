from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
import time


driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))

driver.get("https://apple.com")


#Window size
driver.get_screenshot_as_file("D:\Screenshot\Fullpage.png")


#Full Screen .

time.sleep(5)

driver.save_full_page_screenshot("D:\Screenshot\Fullpage.png")

driver.close()

