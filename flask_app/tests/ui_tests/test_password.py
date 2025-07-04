from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest

class TestFlaskAppPasswordValidation(unittest.TestCase):

    def setUp(self):
        # Set up the Selenium WebDriver (we use headless Chrome for running tests without GUI)
        options = webdriver.ChromeOptions()
        options.add_argument("--headless")  # Run in headless mode (no UI)
        self.driver = webdriver.Chrome(options=options)
        self.driver.get("http://localhost:80")  # Change port if needed

    def test_password_too_short(self):
        # Find the password input field
        password_input = self.driver.find_element(By.NAME, "password")

        # Enter a password that is too short (less than 8 characters)
        password_input.send_keys("short")
        
        # Submit the form (assuming there's a submit button with name 'submit')
        password_input.send_keys(Keys.RETURN)

        # Wait for the error message to appear
        error_message = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//p[contains(text(), 'Password must be at least 8 characters long.')]"))
        )
        self.assertTrue(error_message.is_displayed(), "Error message not found")

    def test_password_too_common(self):
        # Find the password input field
        password_input = self.driver.find_element(By.NAME, "password")

        # Enter a common password (ensure this password exists in the 'xato-net-10-million-passwords-1000.txt' file)
        password_input.send_keys("baseball")

        # Submit the form
        password_input.send_keys(Keys.RETURN)

        # Wait for the error message to appear
        error_message = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//p[contains(text(), 'This password is too common.')]"))
        )
        self.assertTrue(error_message.is_displayed(), "Common password error message not found")

    def test_valid_password(self):
        # Find the password input field
        password_input = self.driver.find_element(By.NAME, "password")

        # Enter a valid password (greater than 8 characters and not common)
        password_input.send_keys("ValidPassword123")

        # Submit the form
        password_input.send_keys(Keys.RETURN)

        # Wait for the page to redirect to /welcome
        WebDriverWait(self.driver, 10).until(
            EC.url_to_be("http://localhost/welcome?password=ValidPassword123")
        )

        # Check if the password is displayed on the welcome page
        welcome_message = self.driver.find_element(By.XPATH, "//p[contains(text(), 'Your password is:')]")
        self.assertTrue(welcome_message.is_displayed(), "Welcome message not found")

    def tearDown(self):
        # Clean up by quitting the WebDriver
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
