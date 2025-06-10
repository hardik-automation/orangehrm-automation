import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Chrome Setup
options = Options()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)
driver.maximize_window()
driver.delete_all_cookies()

# Open URL
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

# Wait setup
wait = WebDriverWait(driver, 10)

# Username input
username = wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@name='username']")))
username.click()
time.sleep(2)
username.send_keys("Admin")
time.sleep(1)
# Password input
password = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input[name='password']")))
password.click()
time.sleep(2)
password.send_keys("admin123")
time.sleep(1)

# Login button click
login_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']")))
login_btn.click()

# Click on dropdown icon (for logout)
dropdown_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[@class='oxd-userdropdown-tab']/i")))
dropdown_btn.click()
time.sleep(2)

# Click on Logout button
logout_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[text()='Logout']")))
logout_btn.click()
time.sleep(2)

# Completion Message
print("Login successful & Logout completed")
driver.quit()
