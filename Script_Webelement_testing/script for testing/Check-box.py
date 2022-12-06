from selenium import webdriver
# from selenium.webdriver.common import keys
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import Select
import time

# import datetime


# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support.select import Select


driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))

driver.get("http://123.200.20.20:5300/")

user_name = driver.find_element(By.XPATH, '//*[@id="exampleInputPassword1"]')
user_name.send_keys("admin")

password = driver.find_element(By.NAME, "p_user_pass")
password.send_keys("cns2022")

login = driver.find_element(By.XPATH, "/html/body/div[2]/div/section/div/div/div/form/div[3]/div[1]/button")
login.click()
time.sleep(2)

pmis = driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/div[2]/div[2]/section/div/div/div/div/div['
                                     '2]/div/div/p/div[1]/div[1]/a/div/div[2]/span')
pmis.click()
time.sleep(2)

Approval = driver.find_element(By.XPATH, '//*[@id="main-menu-navigation"]/li[2]/ul/li[10]/a')
Approval.click()

Family_approval = driver.find_element(By.XPATH, '//*[@id="main-menu-navigation"]/li[2]/ul/li[10]/ul/li[6]/a/span')
Family_approval.click()
time.sleep(2)

#Check box select & deselect :
Check_box = driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/div[2]/div[2]/section/div/div/div[2]/div/div[2]/form/div[1]/div/div[2]/table/tbody/tr[2]/td[6]/div/a[2]/i')
Check_box.click()
time.sleep(2)