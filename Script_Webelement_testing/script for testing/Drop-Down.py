from selenium import webdriver

from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
#from selenium.webdriver.support.select import Select
#import time


driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))

driver.get("http://123.200.20.20:5300/pmis#/search-employee")

user_name = driver.find_element(By.XPATH, '//*[@id="exampleInputPassword1"]')
user_name.send_keys("admin")

password = driver.find_element(By.NAME, "p_user_pass")
password.send_keys("cns2022")

login = driver.find_element(By.XPATH, "/html/body/div[2]/div/section/div/div/div/form/div[3]/div[1]/button")

login.click()

pmis = driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/div[2]/div[2]/section/div/div/div/div/div['
                                     '2]/div/div/p/div[1]/div[1]/a/div/div[2]/span')

pmis.click()

search_emp = driver.find_element(By.XPATH, '//*[@id="main-menu-navigation"]/li[2]/ul/li[7]/a/span')
search_emp.click()

status = driver.find_element(By.XPATH, '//*[@id="death_nature"]')
statusDD = Select(status)

for opt in statusDD.options:
    print(opt.text)

statusDD.select_by_visible_text('Homicide')

