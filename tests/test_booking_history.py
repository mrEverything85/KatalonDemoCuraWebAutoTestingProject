import time

import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from pages.login_page import LoginPage
from pages.appointment_page import AppointmentPage
from pages.history_page import HistoryPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


def test_appointment_history(driver):
    driver.get("https://katalon-demo-cura.herokuapp.com/")

    # Click "Make Appointment"
    WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable((By.ID, "btn-make-appointment"))
    ).click()

    # Đăng nhập
    login_page = LoginPage(driver)
    login_page.login("John Doe", "ThisIsNotAPassword")

    # Đặt lịch hẹn
    appointment_page = AppointmentPage(driver)
    appointment_page.book_appointment(
        facility="Hongkong CURA Healthcare Center",
        apply_readmission=True,
        healthcare_program="Medicaid",
        visit_date="12/12/2025",
        comment="Automated test booking"
    )

    # Kiểm tra lịch sử đặt lịch
    history_page = HistoryPage(driver)
    history_page.go_to_history()
    result = history_page.verify_last_appointment(
        expected_facility="Hongkong CURA Healthcare Center",
        expected_program="Medicaid",
        expected_comment="Automated test booking"
    )


    # Kiểm tra kết quả
    assert result, "Appointment history check failed!"
