import pytest
from selenium import webdriver
from webdriver_manager.microsoft import EdgeChromiumDriverManager

@pytest.fixture()
def driver():
    """Fixture to initialize WebDriver for Edge."""
    driver = webdriver.Edge()
    driver.maximize_window()
    yield driver  # Cung cấp driver cho test case
    driver.quit()  # Đóng trình duyệt sau khi test xong
