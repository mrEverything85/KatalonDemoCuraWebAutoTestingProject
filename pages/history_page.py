from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class HistoryPage:
    def __init__(self, driver):
        self.driver = driver

    def go_to_history(self):
        # Nhấn vào menu
        menu_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, "menu-toggle"))
        )
        menu_button.click()

        # Click vào "History"
        history_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.LINK_TEXT, "History"))
        )
        history_button.click()

        # Chờ trang history load xong
        history_title = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.TAG_NAME, "h2"))
        )

        return history_title.text == "History"

    def verify_last_appointment(self, expected_facility, expected_program, expected_comment):
        # Lấy thông tin appointment gần nhất
        facility = self.driver.find_element(By.ID, "facility").text
        program = self.driver.find_element(By.ID, "program").text
        comment = self.driver.find_element(By.ID, "comment").text

        # So sánh kết quả với dữ liệu mong đợi
        return (facility == expected_facility) and (program == expected_program) and (comment == expected_comment)
