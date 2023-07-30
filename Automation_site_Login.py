import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver= webdriver.Chrome()
driver.maximize_window()

driver.get("https://automation.credence.in/login")
time.sleep(5)

driver.find_element(By.XPATH,"//input[@name='email']").send_keys("Ravikant@23.com")
time.sleep(5)
driver.find_element(By.XPATH,"//input[@id='password']").send_keys("Ravikasu@1")
time.sleep(3)
driver.find_element(By.CSS_SELECTOR,"button[type='submit']").click()
time.sleep(6)

try:
    driver.find_element(By.XPATH,"//h2[normalize-space()='CredKart']")
    print("the test is passed")
except:
    print('login test is faile')

