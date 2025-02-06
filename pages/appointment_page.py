from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class AppointmentPage:
    def __init__(self, driver):
        self.driver = driver

    def book_appointment(self, facility, apply_readmission, healthcare_program, visit_date, comment):
        # Chọn Facility
        facility_dropdown = WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable((By.ID, "combo_facility"))
        )
        facility_dropdown.click()
        self.driver.find_element(By.XPATH, f"//option[@value='{facility}']").click()

        # Chọn Apply for hospital readmission (nếu có)
        if apply_readmission:
            self.driver.find_element(By.ID, "chk_hospotal_readmission").click()

        # Chọn Healthcare Program
        if healthcare_program.lower() == "medicare":
            self.driver.find_element(By.ID, "radio_program_medicare").click()
        elif healthcare_program.lower() == "medicaid":
            self.driver.find_element(By.ID, "radio_program_medicaid").click()
        elif healthcare_program.lower() == "none":
            self.driver.find_element(By.ID, "radio_program_none").click()

        # Nhập ngày khám bệnh
        date_input = self.driver.find_element(By.ID, "txt_visit_date")
        date_input.clear()
        date_input.send_keys(visit_date)

        # Nhập ghi chú
        self.driver.find_element(By.ID, "txt_comment").send_keys(comment)

        # Click "Book Appointment"
        self.driver.find_element(By.ID, "btn-book-appointment").click()

        # Xác nhận đặt lịch thành công
        confirm_message = WebDriverWait(self.driver, 15).until(
            EC.visibility_of_element_located((By.TAG_NAME, "h2"))
        ).text

        return confirm_message == "Appointment Confirmation"
