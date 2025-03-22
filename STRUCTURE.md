# VSB Feedback System - Project Structure

## Core Application Files
- `app.py` - Main Flask application entry point
- `config.py` - Configuration settings and constants
- `utils.py` - Utility functions used across the application

## Routes
- `routes/`
  - `hod_routes.py` - HOD portal routes for report generation and feedback management

## Templates
- `templates/`
  - `hod_select.html` - HOD interface for department/semester selection and report generation
  - `hod_login.html` - HOD login page

## Data Files
- `departments.csv` - List of departments
- `semesters.csv` - Available semesters
- `students.csv` - Student information database
- `staffs.csv` - Staff information database
- `subjects.csv` - Subject information database
- `ratings.csv` - Raw feedback ratings data
- `mainrating.csv` - Processed feedback ratings
- `submitted.csv` - Records of students who submitted feedback

## Report Generation
- `report_generator.py` - Generates feedback analysis reports
- `report_non_submission.py` - Creates reports of students who haven't submitted feedback
- `test_report.py` - Testing utilities for report generation

## Data Processing
- `deencrypt.py` - Decrypts student registration numbers in feedback data
- `encrypt_existing_data.py` - Encrypts student data for security

## Static Files
- `static/` - CSS, JavaScript, and other static assets

## Configuration Files
- `.gitignore` - Git ignore rules
- `requirements.txt` - Python package dependencies
- `LICENSE` - Proprietary license for VSB Engineering College

## Project Flow
1. Students submit feedback through the system
2. Data is encrypted for privacy (`encrypt_existing_data.py`)
3. HOD can:
   - View feedback reports by department/semester
   - Generate non-submission reports
   - View overall statistics
4. Reports are generated with watermarks and proper formatting

## Security Features
- Encrypted student registration numbers
- Login required for HOD access
- Data privacy measures
- Campus-restricted usage

## Created by GenrecAI
Founders:
- Shyamnath Sankar
- Jai Samyukth
- Harish V