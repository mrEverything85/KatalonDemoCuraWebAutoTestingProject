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
To execute all test cases:
```
OPTION 1: use cmd to run all the test script in the tests folder and export the result to a html file
pytest tests/ -v --html=report.html --self-contained-html
```

```
OPTION 2: use shift+f10 in Pycharm for each script
```

NOTE: if you use option 1, it's ok to place the conftest.py outside the tests folder. But in the option 2, you have to
put the script in the tests folder, otherwise it'll be fail (because PyCharm run config working inventory only in the
tests folder, it wont find the conftest.py outside). So i'd recommend using option 1.

Test Report:
------------
After running the tests, an HTML report will be generated as `report.html`.
Open it in a web browser to view detailed results.

Author:
-------
Nguyen Thanh An

