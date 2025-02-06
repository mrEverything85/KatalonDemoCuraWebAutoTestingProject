import pytest
from selenium import webdriver

@pytest.fixture(params=["chrome", "firefox", "edge"])  # Chạy trên nhiều trình duyệt
def driver(request):
    if request.param == "chrome":
        driver = webdriver.Chrome()  # Hoặc chỉ định đường dẫn chromedriver
    elif request.param == "firefox":
        driver = webdriver.Firefox()  # Hoặc chỉ định đường dẫn geckodriver
    elif request.param == "edge":
        driver = webdriver.Edge()  # Hoặc chỉ định đường dẫn msedgedriver

    driver.maximize_window()
    yield driver
    driver.quit()
