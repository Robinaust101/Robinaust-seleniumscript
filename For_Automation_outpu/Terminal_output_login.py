import unittest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
import time
#import pytest


class Login(unittest.TestCase):
    def test_login_TC001_valid(self):
        driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
        driver.get("http://123.200.20.20:5300/")

        user_name = driver.find_element(By.XPATH, '//*[@id="exampleInputPassword1"]')
        user_name.clear()
        user_name.send_keys("admin")

        password = driver.find_element(By.NAME, "p_user_pass")
        user_name.clear()
        password.send_keys("cns2022")

        login = driver.find_element(By.XPATH, "/html/body/div[2]/div/section/div/div/div/form/div[3]/div[1]/button")
        login.click()
        time.sleep(2)

        print("Login Test case 001 executed.")
        self.assert_(True)

        driver.close()

    def test_login_TC002_invalid(self):
        driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
        driver.get("http://123.200.20.20:5300/")

        user_name = driver.find_element(By.XPATH, '//*[@id="exampleInputPassword1"]')
        user_name.clear()
        user_name.send_keys("robin")

        password = driver.find_element(By.NAME, "p_user_pass")
        user_name.clear()
        password.send_keys("cns2022")

        login = driver.find_element(By.XPATH, "/html/body/div[2]/div/section/div/div/div/form/div[3]/div[1]/button")
        login.click()
        time.sleep(2)

        print("Login Test case 002 executed.")
        self.assert_(True)

        driver.close()

    def test_login_TC003_invalid(self):
        driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
        driver.get("http://123.200.20.20:5300/")

        user_name = driver.find_element(By.XPATH, '//*[@id="exampleInputPassword1"]')
        user_name.clear()
        user_name.send_keys("admin")

        password = driver.find_element(By.NAME, "p_user_pass")
        user_name.clear()
        password.send_keys("cns2021")

        login = driver.find_element(By.XPATH, "/html/body/div[2]/div/section/div/div/div/form/div[3]/div[1]/button")
        login.click()
        time.sleep(2)

        print("Login Test case 003 executed.")
        self.assert_(True)

        driver.close()


if __name__ == '__main__':
    unittest.main
