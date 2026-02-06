from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

# create screenshots folder
if not os.path.exists("screenshots"):
    os.makedirs("screenshots")

driver = webdriver.Chrome()
driver.get("https://app.hyrenet.in/")
driver.maximize_window()

# Login
driver.find_element(By.ID, "email").send_keys("hyrenet+bugathon@guvi.in")
driver.find_element(By.ID, "password").send_keys("hyrenettest@123")
driver.find_element(By.ID,"submit").click()

time.sleep(5)

# Click Tests menu (you may need to adjust XPath)
driver.find_element(By.XPATH, "//span[text()='Tests']").click()
time.sleep(3)

# Take screenshot of View Report availability
driver.save_screenshot("screenshots/view_report_availability.png")
driver.quit()
