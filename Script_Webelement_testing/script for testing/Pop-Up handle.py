from selenium import webdriver

from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))

# Formula: protocols://username:password@url
driver.get("https://admin:admin@the-internet.herokuapp.com/basic_auth")

title_after_Login = driver.title
print(title_after_Login)

driver.close()