from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os

# create screenshots folder if not exists
if not os.path.exists("screenshots"):
    os.makedirs("screenshots")

driver = webdriver.Chrome()
driver.get("https://app.hyrenet.in/")

# enter credentials
driver.find_element(By.ID, "email").send_keys("hyrenet+bugathon@guvi.in")
driver.find_element(By.ID, "password").send_keys("hyrenettest@123")

# wait until the submit button is clickable, then click
WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID,"submit"))
).click()

# wait until the next page loads (for example, wait for some element that appears after login)
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.TAG_NAME, "body"))
)

# take screenshot
driver.save_screenshot("screenshots/screenshot.png")

driver.quit()