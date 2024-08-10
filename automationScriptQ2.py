#Q2 - Automation(Instagram - Testcase)

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

service = Service(executable_path = "chromedriver.exe")
driver = webdriver.Chrome(service = service)

try:
   
    driver.get("https://www.instagram.com/")  #login page 

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "username"))
    )

    
    username_input = driver.find_element(By.NAME, "username")  
    username_input.send_keys("deinharddavid@gmail.com")  # username - testcase

    
    password_input = driver.find_element(By.NAME, "password") 
    password_input.send_keys("Vision@2030")  # password - testcase


    login_button = driver.find_element(By.XPATH, "//button[@type='submit']") 
    login_button.click()

    welcome_message = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//h1[contains(text(), 'Welcome')]"))
    )

   
    if welcome_message.is_displayed():
        print("Test passed: User is successfully redirected to the homepage.") # welcome message is displayed
    else:
        print("Test failed: Welcome message not found.")

finally:
    driver.quit()
