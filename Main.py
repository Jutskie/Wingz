# Login

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

chromedriver_path = r"\Users\jonel\Desktop\python_ess\chromedriver-win64\chromedriver.exe"  # Adjust path

service = Service(chromedriver_path)
driver = webdriver.Chrome(service=service)

driver.get("https://auth.wingz.me/auth/signin")

time.sleep(2)

username_field = driver.find_element(By.NAME, "username")
password_field = driver.find_element(By.NAME, "password")

username_field.send_keys("qajonelctph@gmail.com")
password_field.send_keys("QAWingz123")

login_button = driver.find_element(By.XPATH, "//button[text()='Sign In']")
login_button.click()

time.sleep(5)
element = driver.find_element(By.CSS_SELECTOR, '[ui-sref="profile.edit-profile"]')
element.click()

time.sleep(5)
element = driver.find_element(By.CSS_SELECTOR, '[ui-sref="profile.my-profile"]')
element.click()
time.sleep(10)

driver.quit()
