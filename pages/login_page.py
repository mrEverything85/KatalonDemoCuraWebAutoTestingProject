from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def login(self, username, password):
        # Chờ và nhập Username
        WebDriverWait(self.driver, 15).until(
            EC.visibility_of_element_located((By.ID, "txt-username"))
        ).send_keys(username)

        # Nhập Password
        self.driver.find_element(By.ID, "txt-password").send_keys(password)

        # Click nút Login
        self.driver.find_element(By.ID, "btn-login").click()

        # Chờ đến khi login thành công
        WebDriverWait(self.driver, 15).until(
            EC.url_contains("appointment")
        )
