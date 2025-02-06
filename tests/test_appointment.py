import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.login_page import LoginPage
from pages.appointment_page import AppointmentPage

@pytest.fixture
def driver():
    driver = webdriver.Edge()
    driver.maximize_window()
    driver.get("https://katalon-demo-cura.herokuapp.com/")
    yield driver
    driver.quit()

def test_make_appointment(driver):
    driver.get("https://katalon-demo-cura.herokuapp.com/")

    # Click "Make Appointment" button
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "btn-make-appointment"))
    ).click()

    # Khởi tạo trang LoginPage và đăng nhập
    login_page = LoginPage(driver)
    login_page.login("John Doe", "ThisIsNotAPassword")

    # Khởi tạo trang AppointmentPage và đặt lịch hẹn
    appointment_page = AppointmentPage(driver)
    result = appointment_page.book_appointment(
        facility="Hongkong CURA Healthcare Center",
        apply_readmission=True,
        healthcare_program="Medicaid",
        visit_date="12/12/2025",
        comment="This is an automated test."
    )

    # Kiểm tra kết quả
    assert result, "Appointment booking failed!"
