from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LogoutPage:
    def __init__(self, driver):
        self.driver = driver

    def logout(self):
        # Nhấn vào menu
        menu_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, "menu-toggle"))
        )
        menu_button.click()

        # Click vào nút Logout
        logout_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.LINK_TEXT, "Logout"))
        )
        logout_button.click()

        # Kiểm tra đã quay về trang login chưa
        login_button = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.ID, "btn-make-appointment"))
        )
        return login_button.is_displayed()
