# frameworks are all discussed and explained in the testFrameworkDesign.txt file this is just an illustration of code

# PAGE OBJECT MODEL
class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.username_input = driver.find_element(By.ID, "username")
        self.password_input = driver.find_element(By.ID, "password")
        self.login_button = driver.find_element(By.ID, "login")

    def login(self, username, password):
        self.username_input.send_keys(username)
        self.password_input.send_keys(password)
        self.login_button.click()
        
# UTILITY FUNCTIONS

def take_screenshot(driver, name):
    driver.save_screenshot(f"{name}.png")
# Reporting
import unittest
from xmlrunner import XMLTestRunner

class Reporter:
    def __init__(self, output_dir):
        self.output_dir = output_dir

    def run(self, test_suite):
        with open(self.output_dir + '/report.xml', 'wb') as output:
            runner = XMLTestRunner(output=output)
            runner.run(test_suite)