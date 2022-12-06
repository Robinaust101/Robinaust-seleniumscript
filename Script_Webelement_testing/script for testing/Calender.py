from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import Select

# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support.select import Select


driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))

driver.get("http://123.200.20.20:5300/pmis#/search-employee")



# Date typical calender :

Calender = driver.find_element(By.XPATH, '//*[@id="death_date"]/div[1]/input')
Calender.click()
time.sleep(2)

Calender.send_keys("1-1-2022")


# Readonly Calendar:

#1.Current Month & date.
Calender = driver.find_element(By.XPATH, '//*[@id="__BVID__74"]/div/div[1]/div[1]/input')
Calender.click()
time.sleep(2)

#Full Xpath
date = driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/div[2]/div[2]/section/div/div/div[1]/div/div[2]/form/div[1]/div[12]/div/div/div[1]/div[2]/div/div[2]/table/tbody/tr[1]/td[3]')
date.click()



#2. Next or Previous month :

Calender = driver.find_element(By.XPATH,
                               '/html/body/div[2]/div[3]/div[2]/div[2]/section/div/div/div[1]/div/div[2]/form/div[1]/div[12]/div/div/div[1]/div[1]/input')
Calender.click()
time.sleep(2)

year = driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/div[2]/div[2]/section/div/div/div[1]/div/div[2]/form/div[1]/div[12]/div/div/div[1]/div[2]/div/div[1]/a[6]')
year.click()
time.sleep(2)

req_year = driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/div[2]/div[2]/section/div/div/div[1]/div/div[2]/form/div[1]/div[12]/div/div/div[1]/div[2]/div/div[2]/div[1]/span[4]')
req_year.click()
time.sleep(2)

req_month = driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/div[2]/div[2]/section/div/div/div[1]/div/div[2]/form/div[1]/div[12]/div/div/div[1]/div[2]/div/div[2]/div[2]/span[6]')
req_month.click()
time.sleep(2)

req_date = driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/div[2]/div[2]/section/div/div/div[1]/div/div[2]/form/div[1]/div[12]/div/div/div[1]/div[2]/div/div[2]/table/tbody/tr[3]/td[1]')
req_date.click()
time.sleep(3)