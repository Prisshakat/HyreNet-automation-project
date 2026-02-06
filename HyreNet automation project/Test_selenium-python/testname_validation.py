from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import time

# create screenshots folder if not exists
if not os.path.exists("screenshots"):
    os.makedirs("screenshots")

driver = webdriver.Chrome()
driver.get("https://app.hyrenet.in/sign-in")

# login
driver.find_element(By.ID, "email").send_keys("hyrenet+bugathon@guvi.in")
driver.find_element(By.ID, "password").send_keys("hyrenettest@123")

WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, "submit"))
).click()

# wait for dashboard
WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//span[text()='Test']"))
).click()

# click Create Test
WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CLASS_NAME, "create-test"))
).click()

# choose Create Manually
WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, "createTestManually"))
).click()

# wait for Test Name field
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "drive-name"))
)

# enter invalid input
test_name = driver.find_element(By.ID, "drive-name")
test_name.send_keys("ibbl@eee")

# click Save
WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Save')]"))
).click()

# wait for validation message
validation_msg = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//label[@for='drive-name' and contains(@class,'form-required')]"))
)

# print validation message text
print("Validation message:", validation_msg.text)

# take screenshot
driver.save_screenshot("screenshots/testname_validation.png")

driver.quit()