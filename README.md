# Python Selenium Framework

## Overview
This is a Python-based Selenium testing framework utilizing the Page Object Model (POM) and Data-Driven Testing (DDT) methodologies. The framework supports parallel test execution using `pytest-xdist`.

## Features
- Page Object Model (POM) for clean and maintainable code
- Data-Driven Testing (DDT) using data from external sources
- Parallel test execution for faster test runs
- Detailed HTML reports
- Cross-browser testing support for Firefox and Chrome

## Prerequisites
- Python 3.x
- Google Chrome and Chromedriver
- Mozilla Firefox and Geckodriver
- `pip` for managing Python packages

## Installation
1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/selenium-python-framework.git
   cd selenium-python-framework

## Install dependencies:
Install dependencies: pip install -r requirements.txt

## Directory Structure
selenium-python-framework/
├── pages/
│   ├── __init__.py
│   ├── base_page.py
│   ├── home_page.py
│   └── login_page.py
├── tests/
│   ├── __init__.py
│   ├── test_login.py
│   └── test_home.py
├── data/
│   ├── test_data.xlsx
├── reports/
│   └── html/
├── utils/
│   ├── __init__.py
│   ├── read_excel.py
│   └── config.py
├── conftest.py
├── pytest.ini
├── requirements.txt
└── README.md

## Parallel Execution
To run tests in parallel using pytest-xdist, use the -n option followed by the number of CPUs to use (or auto to use all available CPUs):
pytest -n auto

## Generate HTML Report
To generate an HTML report, run:\
pytest --html=reports/html/report.html

## Conftest.py
This file includes the setup for Selenium WebDriver and supports both Chrome and Firefox.

## Pytest Configuration
Set up your pytest configuration in pytest.ini:

## Contributing
Feel free to contribute to this project by submitting issues or pull requests.

## License
This project is licensed under the MIT License.

## Contact
For any questions or suggestions, please contact.

This `README.md` file includes all the necessary details and examples for setting up and running the Python Selenium framework using POM and DDT, as well as executing tests in parallel. Feel free to customize it further based on your specific needs! 🚀
[_{{{CITATION{{{_1{](https://github.com/ivdunin/github-api-tests-example/tree/0c68a9771fdcbcba9644c0fddfd32ee345de591e/framework%2Ftest_cases%2Fui_tests%2Fconftest.py)[_{{{CITATION{{{_2{](https://github.com/shotsel/selenium_task/tree/6af635d6272c94af027742fc7ce7f28a3e63867b/tests%2Ftest_allegro.py)