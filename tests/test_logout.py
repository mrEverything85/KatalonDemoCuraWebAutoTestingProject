import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from pages.login_page import LoginPage
from pages.logout_page import LogoutPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


def test_logout(driver):
    driver.get("https://katalon-demo-cura.herokuapp.com/")

    # Click "Make Appointment"
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "btn-make-appointment"))
    ).click()

    # Đăng nhập
    login_page = LoginPage(driver)
    login_page.login("John Doe", "ThisIsNotAPassword")

    # Thực hiện Logout
    logout_page = LogoutPage(driver)
    result = logout_page.logout()

    # Kiểm tra xem đã về lại trang Login chưa
    assert result, "Logout failed!"
