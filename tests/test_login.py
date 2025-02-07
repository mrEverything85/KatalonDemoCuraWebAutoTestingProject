import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.login_page import LoginPage


def test_login(driver):
    driver.get("https://katalon-demo-cura.herokuapp.com/")
    # Chờ và click 'Make Appointment'
    make_appointment_btn = WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable((By.ID, "btn-make-appointment"))
    )
    make_appointment_btn.click()

    login_page = LoginPage(driver)
    login_page.login("John Doe", "ThisIsNotAPassword")

    assert "appointment" in driver.current_url, "Login failed, check credentials or site behavior"
