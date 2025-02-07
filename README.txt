Automation Testing Project - Selenium & Pytest
==============================================

Project Description:
--------------------
This is an automation testing project using Selenium and Pytest for the website https://katalon-demo-cura.herokuapp.com/. The project follows the Page Object Model (POM) structure and includes multiple test cases for user authentication, appointment booking, logout, and appointment history verification.

Prerequisites:
--------------
1. Python 3.x installed
2. Google Chrome and Microsoft Edge browsers installed
3. ChromeDriver and EdgeDriver (managed automatically by webdriver-manager)
4. Install the required Python packages using:
   ```
   pip install -r requirements.txt
   ```

Project Structure:
------------------
- **tests/**: Contains all test scripts
  - `test_login.py` - Tests user login functionality
  - `test_appointment.py` - Tests appointment booking
  - `test_logout.py` - Tests logout functionality
  - `test_booking_history.py` - Tests appointment history verification
- **pages/**: Implements the Page Object Model (POM)
  - `login_page.py`
  - `appointment_page.py`
  - `logout_page.py`
  - `history_page.py`
- **conftest.py**: Contains Pytest fixtures for browser setup and teardown
- **requirements.txt**: Lists required Python dependencies
- **README.txt**: This file

Running Tests:
--------------
To execute all test cases, run:
```
pytest tests/ -v --html=report.html --self-contained-html
```

Test Report:
------------
After running the tests, an HTML report will be generated as `report.html`. Open it in a web browser to view detailed results.

Author:
-------
Nguyen Thanh An

