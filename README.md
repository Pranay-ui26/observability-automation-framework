# Observability Automation Framework

## Overview

This repository contains the UI automation framework for the Observability application built using **Playwright**, **Python**, and **Pytest** following the **Page Object Model (POM)** design pattern.

The framework is designed to be scalable, reusable, and easy to maintain while supporting UI automation, reporting, screenshots, and future API integrations.

---

# Technology Stack

- Python 3.11+
- Playwright
- Pytest
- Page Object Model (POM)
- Allure Reports
- Pytest HTML Reports
- Python Dotenv
- YAML Configuration

---

# Project Structure

```
observability-automation-framework
│
├── components/
│   ├── profile_menu.py
│
├── config/
│   └── config.py
│
├── locators/
│   ├── login_locators.py
│   ├── dashboard_locators.py
│
├── pages/
│   ├── base_page.py
│   ├── login_page.py
│   ├── dashboard_page.py
│
├── tests/
│   ├── test_login_logout.py
│
├── utilities/
│   └── logger.py
│
├── reports/
├── screenshots/
├── logs/
├── allure-results/
│
├── .env
├── .gitignore
├── conftest.py
├── pytest.ini
├── requirements.txt
└── README.md
```

---

# Framework Design

The framework follows the **Page Object Model (POM)** architecture.

```
Tests
    │
    ▼
Page Objects
    │
    ▼
Reusable Components
    │
    ▼
Base Page
    │
    ▼
Playwright
```

---

# Installation

Clone the repository

```bash
git clone <repository-url>
```

Navigate to the project

```bash
cd observability-automation-framework
```

Create virtual environment

```bash
py -m venv .venv
```

Activate virtual environment

PowerShell

```powershell
.\.venv\Scripts\Activate.ps1
```

Install dependencies

```bash
py -m pip install -r requirements.txt
```

Install Playwright browsers

```bash
playwright install
```

---

# Configuration

Create a `.env` file in the project root.

Example

```text
BASE_URL=https://app.niriksha.ai/login

APP_USERNAME=your-email@example.com

APP_PASSWORD=your-password

BROWSER=chromium

HEADLESS=False

TIMEOUT=30000
```

---

# Running Tests

Run all tests

```bash
py -m pytest
```

Run a single test file

```bash
py -m pytest tests/test_login_logout.py
```

Run a specific test

```bash
py -m pytest tests/test_login_logout.py -k test_login
```

Run with verbose output

```bash
py -m pytest -v
```

---

# Reports

Generate HTML Report

```bash
py -m pytest --html=reports/report.html
```

Open report

```
reports/report.html
```

Generate Allure Results

```bash
py -m pytest --alluredir=allure-results
```

View Allure Report

```bash
allure serve allure-results
```

---

# Logging

Execution logs are generated in

```
logs/
```

---

# Screenshots

Screenshots are automatically captured during execution (when implemented).

```
screenshots/
```

---

# Supported Features

- Login
- Logout
- Dashboard Validation
- Reusable Page Objects
- Reusable Components
- Centralized Configuration
- Logging
- HTML Reporting
- Allure Reporting

---

# Best Practices

- Follow Page Object Model (POM)
- Keep locators separate from page logic
- Avoid hardcoded test data
- Store credentials in `.env`
- Use reusable methods from `BasePage`
- Write independent test cases

---

# Future Enhancements

- API Automation
- Database Validation
- Parallel Execution
- Cross-browser Testing
- CI/CD Integration
- Docker Support
- Jenkins Integration
- Test Data Management
- Retry Mechanism
- Screenshot on Failure
- Playwright Trace Viewer
- Slack Notifications

---

# Author

Pranay Kumar Reddy
Automation Test Engineer
