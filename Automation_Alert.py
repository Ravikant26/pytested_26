import time


from selenium import webdriver
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://the-internet.herokuapp.com/javascript_alerts")
time.sleep(5)
driver.find_element(By.XPATH,"//button[@onclick='jsConfirm()']").click()
time.sleep(3)
print(Alert(driver).text)
# Alert(driver).accept()
Alert(driver).dismiss()
time.sleep(3)
print(driver.find_element(By.CSS_SELECTOR,"#result").text)
time.sleep(3)
driver.find_element(By.CSS_SELECTOR,"button[onclick='jsConfirm()']").click()
time.sleep(5)
print(Alert(driver).text)
Alert(driver).accept()
# Alert(driver).dismiss()
time.sleep(5)
print(driver.find_element(By.CSS_SELECTOR,"#result").text)
time.sleep(4)

driver.find_element(By.CSS_SELECTOR,"button[onclick='jsPrompt()']").click()
time.sleep(3)
print(Alert(driver).send_keys("i am stright forword person."))
time.sleep(5)
Alert(driver).accept()
print(driver.find_element(By.CSS_SELECTOR,"#result").text)
time.sleep(3)





