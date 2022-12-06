from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
import time

#from selenium.webdriver.support.ui import Select
#from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support.select import Select


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

death_reg = driver.find_element(By.XPATH, '//*[@id="main-menu-navigation"]/li[2]/ul/li[3]/a/span')
death_reg.click()

#Start Drop-Down :
Emp_code = driver.find_element(By.XPATH, '//*[@id="emp_code"]/div/div[1]/input')
Emp_code.click()
time.sleep(2)

Emp_code.send_keys("210001")
time.sleep(2)

Emp_code.send_keys(Keys.ENTER)
time.sleep(2)