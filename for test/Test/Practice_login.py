from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from DataDriven import excel_utils
import time
driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
driver.get("https://demo.opencart.com/")
my_account = driver.find_element(By.XPATH, '/html/body/nav/div[2]/div[2]/ul/li[2]/div/a/span')
my_account.click()
login = driver.find_element(By.XPATH, '/html/body/nav/div[2]/div[2]/ul/li[2]/div/ul/li[2]/a')
login.click()

login_data_file = '../../DataDriven/Login_data.xlsx'
login_sheet_invalid = 'Login'
#login_sheet_valid = 'Login_valid'
number_of_rows = excel_utils.get_row_count(login_data_file, login_sheet_invalid)
number_of_columns = excel_utils.get_column_count(login_data_file, login_sheet_invalid)

for r in range(2, number_of_rows + 1):
    dd_email = excel_utils.read_data(login_data_file, login_sheet_invalid, r, 1)
    dd_password = excel_utils.read_data(login_data_file, login_sheet_invalid, r, 2)

    email = driver.find_element(By.XPATH, '//*[@id="input-email"]')
    email.clear()
    email.send_keys(dd_email)
    time.sleep(2)
    password = driver.find_element(By.XPATH, '/html/body/main/div[2]/div/div/div/div[2]/div/div/form/div[2]/input')
    password.clear()
    password.send_keys(dd_password)
    time.sleep(2)

    loginBtn = driver.find_element(By.XPATH, '/html/body/main/div[2]/div/div/div/div[2]/div/div/form/button')
    loginBtn.click()

    if driver.title == 'Account Login':
        excel_utils.write_data(login_data_file, login_sheet_invalid, r, 3, "Didn't Login.Test passed")
    else:
        excel_utils.write_data(login_data_file, login_sheet_invalid, r, 3, "Login successfully.test fail")


driver.close()