# VSB Engineering College Feedback System

A web-based feedback system designed for VSB Engineering College to collect and manage student feedback for faculty and courses.

## Features

- **Student Feedback Collection**
  - Secure student login using registration numbers
  - Rating system for 10 different feedback parameters
  - Real-time average calculation
  - Visual rating indicators (Green for good, Yellow for average, Red for poor)
  - One-time feedback submission per student

- **Admin Management**
  - Protected admin dashboard
  - Staff and subject mapping management
  - Student data management
  - Department and semester configuration
  - Feedback reports generation

- **HOD Access**
  - Department-specific feedback reports
  - Staff performance analysis

- **Security Features**
  - Registration number validation
  - Encrypted storage of student data
  - Prevention of duplicate submissions
  - Access control based on roles

## Setup Instructions

1. Clone the repository
2. Install required dependencies:
```bash
pip install -r requirements.txt
```

3. Ensure these CSV files are present in the root directory:
   - departments.csv
   - semesters.csv
   - staffs.csv
   - subjects.csv
   - students.csv
   - admin_mapping.csv

4. Run the application:
```bash
python app.py
```

The server will start on your machine's IP address on port 80.

## File Structure

- `app.py` - Main application file with routes and core logic
- `config.py` - Configuration settings and constants
- `utils.py` - Utility functions for data handling
- `report_generator.py` - Feedback report generation logic
- `report_non_submission.py` - Non-submission report generation
- `deencrypt.py` - Data encryption utilities
- `routes/`
  - `admin_routes.py` - Admin-specific routes
  - `hod_routes.py` - HOD-specific routes
- `templates/` - HTML templates
  - `feedback.html` - Main feedback form
  - `feedback_form.html` - Alternative feedback form
  - Other template files
- `static/` - Static assets (CSS, JS, images)

## Usage

### For Students
1. Visit the homepage
2. Enter your registration number
3. Fill the feedback form for all staff members
4. Submit the feedback

### For Administrators
1. Access the admin panel via /admin_login
2. Default password: "vsbec"
3. Manage:
   - Staff-subject mappings
   - Student data
   - Generate reports

### For HODs
1. Access HOD panel with credentials
2. View department-specific feedback reports
3. Monitor staff performance

## Data Files

- `mainrating.csv` - Stores the main feedback ratings
- `ratings.csv` - Processed feedback data
- `submitted.csv` - Tracks submitted feedback entries
- `students.csv` - Student information
- `staffs.csv` - Staff information
- `subjects.csv` - Subject information
- `departments.csv` - Department information
- `semesters.csv` - Semester information
- `admin_mapping.csv` - Staff-subject mapping data

## Security Notes

1. Change the default admin password in production
2. Ensure proper file permissions for CSV files
3. Keep encryption keys secure
4. Regularly backup feedback data

## License

See the LICENSE file for details.