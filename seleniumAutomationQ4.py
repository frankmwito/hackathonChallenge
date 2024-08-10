#Q4 - Google search automation(Test case - Search for Test Automation)

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

service = Service(executable_path  = "chromedriver.exe")
driver = webdriver.Chrome(service = service)  
try:

    driver.get("https://www.google.com")

    search_box = driver.find_element(By.NAME, "q")  
    search_box.send_keys("Test Automation")         # search query
    search_box.send_keys(Keys.RETURN)               

    time.sleep(2)

    
    results = driver.find_elements(By.CSS_SELECTOR, "div.g") # Verify for search results page contains results

    if len(results) > 0:
        print("Search results are displayed on the page.")
    else:
        print("No search results found.")

finally:
    driver.quit()
