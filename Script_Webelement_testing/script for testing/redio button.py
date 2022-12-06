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

Search_emp = driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div[3]/ul/li[2]/ul/li[2]/a/span')
Search_emp.click()
time.sleep(2)

#Redio button handle
redio = driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/div[2]/div[2]/section/div/div/form/div/div/div/div/div[8]/div/div/div/div[1]/label')
redio.click()
time.sleep(3)

no = driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/div[2]/div[2]/section/div/div/form/div/div/div/div/div[8]/div/div/div/div[2]/label')
no.click()
time.sleep(2)

driver.find_element(By.ID, 'basic_sub_btn').click()

emp_id = driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/div[2]/div[2]/section/div/div/div/div/div/div[2]/div/div/ul/li[1]/a')




