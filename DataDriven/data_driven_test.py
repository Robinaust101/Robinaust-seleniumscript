from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from DataDriven import excel_utils
import time
import unittest

driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))

driver.get("http://123.200.20.20:5300/")

login_data_file = 'Login_data.xlsx'
login_sheet_invalid = 'Login'
# login_sheet_valid = 'Login_valid'
number_of_rows = excel_utils.get_row_count(login_data_file, login_sheet_invalid)
number_of_columns = excel_utils.get_column_count(login_data_file, login_sheet_invalid)

for r in range(2, number_of_rows + 1):
    dd_username = excel_utils.read_data(login_data_file, login_sheet_invalid, r, 1)
    dd_password = excel_utils.read_data(login_data_file, login_sheet_invalid, r, 2)

    user_name = driver.find_element(By.XPATH, '//*[@id="exampleInputPassword1"]')
    user_name.clear()
    user_name.send_keys(dd_username)
    time.sleep(2)

    password = driver.find_element(By.NAME, "p_user_pass")
    user_name.clear()
    password.send_keys(dd_password)
    time.sleep(2)

    login = driver.find_element(By.XPATH, "/html/body/div[2]/div/section/div/div/div/form/div[3]/div[1]/button")
    login.click()
    time.sleep(2)

    if driver.current_url == 'http://123.200.20.20:5300/':
        excel_utils.write_data(login_data_file, login_sheet_invalid, r, 3, "didn't login.Test passed")
    else:
        excel_utils.write_data(login_data_file, login_sheet_invalid, r, 3, "Login Success.Test Failed.")




driver.close()


