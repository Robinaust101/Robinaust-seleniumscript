from behave import *
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
import time


@given(u'I launched firefox')
def step_implementation(context):
    context.driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))


@when(u'I open login page')
def step_implementation(context):
    context.driver.get("http://123.200.20.20:5300/")
    time.sleep(2)


@when(u'I enter user name')
def step_implementation(context):
    context.driver.find_element(By.XPATH, '//*[@id="exampleInputPassword1"]').send_keys("admin")
    time.sleep(2)


@when(u'I enter password')
def step_implementation(context):
    context.driver.find_element(By.NAME, "p_user_pass").send_keys("cns2022")
    time.sleep(2)


@when(u'I click login')
def step_implementation(context):
    context.driver.find_element(By.XPATH, '/html/body/div[2]/div/section/div/div/div/form/div[3]/div[1]/button').click()
    time.sleep(2)


@when(u'I click PMIS')
def step_implementation(context):
    context.driver.find_element(By.XPATH,
                                '/html/body/div[2]/div[3]/div[2]/div[2]/section/div/div/div/div/div[2]/div/div/p/div['
                                '1]/div[1]/a/div/div[2]').click()
    time.sleep(2)


@then(u'Login successful')
def step_implementation(context):
    if context.driver.title == 'Dashboard':
        print("Login successful")
    else:
        print("Login Failed")

    context.driver.close()
