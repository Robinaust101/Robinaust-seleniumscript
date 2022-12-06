from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

# options = webdriver.FirefoxOptions()
options = webdriver.firefoxOptions()
options.headless = True
driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()), options=options)

driver.get("https://apple.com")
print('Title is: ' + driver.title)

driver.get_screenshot_as_file("F:\Training\PeopleNTech\BITM Online 12\TestAutomationBITM12\ScreenshotFiles\Headless.jpg")

print("Headless test done.")
driver.close()