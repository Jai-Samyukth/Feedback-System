# 📖 User Manual - Students and Staff
## VSB Engineering College Faculty Feedback System

**Version**: 2.0  
**Last Updated**: January 2025

---

## 📌 Table of Contents

1. [Introduction](#introduction)
2. [System Access](#system-access)
3. [For Students](#for-students)
   - [Logging In](#student-login)
   - [Submitting Feedback](#submitting-feedback)
   - [Rating Guidelines](#rating-guidelines)
   - [Troubleshooting](#student-troubleshooting)
4. [For Staff/Faculty](#for-staff-faculty)
   - [Understanding Feedback](#understanding-feedback)
   - [Viewing Your Ratings](#viewing-your-ratings)
5. [For Admin](#for-admin)
   - [Admin Dashboard](#admin-dashboard)
   - [Managing Students](#managing-students)
   - [Managing Mappings](#managing-mappings)
   - [Bulk Operations](#bulk-operations)
   - [Generating Reports](#generating-reports)
6. [Frequently Asked Questions](#faq)
7. [Support](#support)

---

## 📘 Introduction

### What is the Faculty Feedback System?

The Faculty Feedback System is a web-based application designed to collect, manage, and analyze student feedback on faculty performance at VSB Engineering College. This system helps:

- **Students**: Share constructive feedback about their teachers
- **Faculty**: Understand student perspectives and improve teaching methods
- **Administration**: Monitor teaching quality and make data-driven decisions
- **HODs**: Review department-wide performance metrics

### Key Features

✅ **Secure & Anonymous**: Student registration numbers are encrypted for privacy  
✅ **One-Time Submission**: Each student can submit feedback only once per semester  
✅ **10-Point Rating Scale**: Comprehensive evaluation across 10 parameters  
✅ **User-Friendly**: Clean interface with visual color-coded indicators  
✅ **Real-Time Reports**: Instant report generation for administrators  
✅ **Excel Integration**: Bulk upload/download support  

### System Requirements

- **Device**: Desktop, Laptop, Tablet, or Smartphone
- **Browser**: Chrome, Firefox, Safari, Edge (latest versions)
- **Internet**: Stable internet connection
- **Registration**: Valid college registration number (for students)

---

## 🌐 System Access

### How to Access the System

**URL**: `https://your-app-name.onrender.com`  
*(Get the exact URL from your IT department)*

### Available Portals

1. **Student Portal**: Main homepage - Student feedback submission
2. **Admin Portal**: `https://your-app-name.onrender.com/admin_login`
3. **HOD Portal**: `https://your-app-name.onrender.com/hod_login`

---

## 👨‍🎓 For Students

### 🔐 Student Login

#### Step-by-Step Login Process

1. **Open the System**
   - Open your web browser
   - Go to the feedback system URL
   - You will see the homepage with a login form

2. **Enter Your Registration Number**
   - Type your college registration number
   - Example: `23CS001`, `22EE042`, `21ME103`
   - Numbers only or with department code

3. **Click "Validate & Continue"**
   - System validates your registration number
   - Checks if you're registered in the database
   - Verifies you haven't already submitted feedback

4. **Wait for Validation**
   - Green message: ✅ "Validation successful! Redirecting..."
   - Red message: ❌ Error (see [Troubleshooting](#student-troubleshooting))

5. **Automatic Redirect**
   - If successful, you'll be redirected to the feedback form
   - Your department and semester info will be loaded automatically

#### Login Requirements

- ✅ Must be a registered student in the database
- ✅ Must have a valid registration number
- ✅ Cannot have already submitted feedback for the current session
- ✅ Registration number must match your department and semester

---

### 📝 Submitting Feedback

#### Understanding the Feedback Form

After logging in, you'll see:

**Header Information:**
- Your Department (e.g., "Computer Science - A")
- Your Semester (e.g., "Semester 4")

**Faculty List:**
- List of all faculty members who teach your class
- Each faculty shows their name and subject
- Each faculty has 10 rating questions

**Rating Scale:**
- Range: 1 to 10
- 1 = Poor, 5 = Average, 10 = Excellent
- All ratings are required

#### How to Rate Faculty

**Step 1: Read Each Question Carefully**

The 10 feedback parameters are:

1. **Faculty's Approach**: Teaching methodology and style
2. **Class Preparation**: How prepared the faculty is for lectures
3. **Teaching Ability**: Clarity and effectiveness of teaching
4. **Illustration with Examples**: Use of real-world examples
5. **Course Coverage**: Completeness of syllabus coverage
6. **Emphasis on Key Concepts**: Focus on important topics
7. **Pace of Teaching**: Speed appropriate for understanding
8. **Ability to Clarify Doubts**: Responsiveness to questions
9. **Subject Mastery**: Deep knowledge of the subject
10. **Overall Rating**: Your overall impression

**Step 2: Select Rating for Each Question**

- Click on the dropdown menu for each question
- Select a number from 1 to 10
- **Visual Color Indicators**:
  - 🟢 **Green (7-10)**: Good to Excellent
  - 🟡 **Yellow (4-6)**: Average to Satisfactory
  - 🔴 **Red (1-3)**: Needs Improvement

**Step 3: Repeat for All Faculty**

- Rate all 10 questions for the first faculty member
- Scroll down to the next faculty member
- Repeat until all faculty are rated

**Step 4: Review Your Ratings**

- Double-check all ratings are filled
- Ensure ratings accurately reflect your opinion
- Remember: You cannot change ratings after submission

**Step 5: Submit Feedback**

- Click the green **"Submit All Feedback"** button at the bottom
- Confirm your submission
- Wait for success message

**Step 6: Success Confirmation**

- You'll see: ✅ "Feedback submitted successfully. Thank you!"
- You'll be redirected to the login page
- You **cannot** submit again with the same registration number

---

### 📊 Rating Guidelines

#### How to Rate Fairly

**Be Honest and Constructive**
- Rate based on actual classroom experience
- Don't rate based on personal likes/dislikes
- Focus on teaching effectiveness, not personality

**Consider the Full Semester**
- Think about the entire semester, not just recent classes
- Balance good and challenging aspects
- Consider improvements made during the semester

**Use the Full Rating Scale**
- Don't rate everyone 10 or everyone 1
- Use middle ratings (4-6) for average performance
- Reserve high ratings (8-10) for truly excellent teaching
- Use low ratings (1-3) only for serious concerns

#### Rating Interpretations

| Rating | Meaning | When to Use |
|--------|---------|-------------|
| 10 | Outstanding | Exceptional teacher, inspiring, goes above and beyond |
| 8-9 | Excellent | Very effective teaching, clear concepts, engaging |
| 7 | Good | Solid teaching, most concepts clear, effective |
| 5-6 | Satisfactory | Average teaching, concepts covered, some gaps |
| 4 | Below Average | Significant room for improvement |
| 2-3 | Poor | Many issues, difficult to understand |
| 1 | Very Poor | Major problems, ineffective teaching |

#### Examples

**Example 1: Excellent Teacher**
- Well-prepared for every class ➜ 9
- Explains concepts with clarity ➜ 9
- Uses real-world examples ➜ 8
- Always available for doubts ➜ 10
- Strong subject knowledge ➜ 9

**Example 2: Average Teacher**
- Sometimes prepared, sometimes not ➜ 5
- Explains concepts but sometimes unclear ➜ 6
- Few examples given ➜ 5
- Answers doubts when asked ➜ 6
- Adequate subject knowledge ➜ 6

**Example 3: Needs Improvement**
- Often unprepared ➜ 3
- Difficult to understand ➜ 3
- No examples or practical applications ➜ 2
- Rarely available for questions ➜ 3
- Limited subject knowledge shown ➜ 4

---

### 🔧 Student Troubleshooting

#### Common Issues and Solutions

**Issue 1: "Registration number not found"**

**Cause**: You're not in the system database

**Solutions**:
- ✅ Verify you entered the correct registration number
- ✅ Check with admin to add your registration number
- ✅ Ensure you're not entering extra spaces or special characters
- ✅ Try entering only the numeric part (e.g., `23001` instead of `23CS001`)

---

**Issue 2: "Feedback already submitted"**

**Cause**: You've already submitted feedback

**Solutions**:
- ℹ️ This is normal - you can only submit once per session
- ℹ️ No action needed - your feedback is already recorded
- ℹ️ If you believe this is an error, contact admin
- ❌ You cannot edit or resubmit feedback

---

**Issue 3: "Invalid registration number format"**

**Cause**: Registration number format not recognized

**Solutions**:
- ✅ Enter only numbers: `23001` not `23-CS-001`
- ✅ Remove any letters, dashes, or spaces
- ✅ Example: If your reg no. is `23CS042`, try entering `23042`

---

**Issue 4: "Please fill all rating boxes"**

**Cause**: One or more ratings are missing

**Solutions**:
- ✅ Scroll through the form carefully
- ✅ Check every faculty member has all 10 questions rated
- ✅ Look for empty dropdown boxes
- ✅ Ensure no rating is left as "Select Rating"

---

**Issue 5: Page loads slowly**

**Cause**: Internet connection or server response time

**Solutions**:
- ✅ Wait patiently (first load after inactivity can take 30-60 seconds)
- ✅ Check your internet connection
- ✅ Try refreshing the page
- ✅ Close other browser tabs
- ✅ Try a different browser

---

**Issue 6: "Registration number range exceeds limit"**

**Cause**: System security check detected unusual registration number

**Solutions**:
- ✅ Contact admin - this is an anti-fraud measure
- ✅ Verify you're using your own registration number
- ℹ️ This happens when registration numbers in your batch vary too much

---

**Issue 7: Cannot see faculty members after login**

**Cause**: No mappings created for your department/semester

**Solutions**:
- ✅ Contact admin to create staff-subject mappings
- ✅ Verify you're in the correct department and semester
- ℹ️ Admin must add faculty members for your class

---

**Issue 8: Submit button doesn't work**

**Cause**: Browser JavaScript issue or form validation error

**Solutions**:
- ✅ Ensure all ratings are filled
- ✅ Try a different browser (Chrome recommended)
- ✅ Clear browser cache and cookies
- ✅ Disable browser extensions temporarily
- ✅ Check browser console for errors (press F12)

---

## 👨‍🏫 For Staff/Faculty

### Understanding Feedback

#### What Feedback Means for You

The feedback system helps you:

- ✅ **Understand student perspectives** on your teaching
- ✅ **Identify strengths** to continue building upon
- ✅ **Discover areas for improvement** in teaching methodology
- ✅ **Track progress** over semesters
- ✅ **Enhance teaching effectiveness** based on constructive input

#### Feedback Confidentiality

- 🔒 Individual student identities are **anonymous**
- 🔒 Registration numbers are **encrypted**
- 🔒 Only aggregated data is shown in reports
- 🔒 No one can trace feedback to specific students

### Viewing Your Ratings

**How to Access Your Feedback:**

1. Contact your **Department HOD**
2. HOD can generate department reports showing all faculty ratings
3. Reports show average scores for each parameter
4. Comparative analysis available across department

**What You'll See in Reports:**

- Your name and subjects taught
- Average rating for each of the 10 parameters
- Overall average rating
- Number of students who provided feedback
- Departmental average for comparison

### Interpreting Your Feedback

**Rating Ranges:**

| Average Rating | Performance Level | Action |
|----------------|-------------------|--------|
| 8.5 - 10.0 | Excellent | Keep up the great work! |
| 7.0 - 8.4 | Good | Continue current methods, minor improvements |
| 5.5 - 6.9 | Satisfactory | Review teaching strategies, seek mentor advice |
| 4.0 - 5.4 | Needs Improvement | Significant changes needed, training recommended |
| Below 4.0 | Critical | Immediate intervention required |

### Using Feedback Constructively

**Step 1: Review Objectively**
- Don't take ratings personally
- Focus on trends, not individual comments
- Look for patterns across parameters

**Step 2: Identify Strengths**
- Note parameters with high ratings (8+)
- Understand what students appreciate
- Continue these effective practices

**Step 3: Identify Areas for Improvement**
- Focus on parameters with lower ratings (below 6)
- Prioritize the most critical areas
- Create an action plan

**Step 4: Take Action**
- Attend faculty development programs
- Seek mentorship from highly-rated colleagues
- Experiment with new teaching methods
- Request student feedback informally

**Step 5: Track Progress**
- Compare ratings across semesters
- Monitor improvement in target areas
- Celebrate improvements

---

## 👔 For Admin

### Admin Dashboard

#### Accessing Admin Portal

**URL**: `https://your-app-name.onrender.com/admin_login`

**Login**:
1. Enter admin password (provided by IT department)
2. Click "Login"
3. Access admin dashboard

#### Admin Capabilities

From the admin dashboard, you can:

- ✅ **Manage Students**: Add, view, upload student data
- ✅ **Manage Staff-Subject Mappings**: Assign faculty to departments/semesters
- ✅ **Bulk Add**: Add multiple staff/subjects at once
- ✅ **Generate Reports**: Create feedback reports
- ✅ **View Mappings**: View and delete existing mappings
- ✅ **Upload Excel**: Import data via Excel files

---

### Managing Students

#### Adding Students via Excel Upload

**⚠️ CRITICAL: Download Reference File First!**

Before creating your Excel file, **YOU MUST download the reference file** that contains the exact department and semester names from the database. Using incorrect names will cause upload errors!

**Step 0: Download Reference File** (DO THIS FIRST!)

1. Login as admin
2. Go to **"Student Management"** from dashboard
3. Look for the **"Download Reference File"** button (top of page)
4. Click **"Download Reference File"** 
5. Save the file: `REFERENCE_Names.xlsx`
6. Open the file - it contains 4 sheets:
   - **Departments**: Exact department names
   - **Semesters**: Exact semester names  
   - **Staff**: Exact staff names (for mappings)
   - **Subjects**: Exact subject names (for mappings)

**Alternative Downloads** (if you only need specific data):
- **"Download Department Names"** button - CSV file with departments only
- **"Download Semester Names"** button - CSV file with semesters only

---

**Step 1: Prepare Excel File**

Create an Excel file (.xlsx or .xls) with these columns:

| registerno | department | semester |
|------------|------------|----------|
| 23001 | Computer Science - A | 4 |
| 23002 | Computer Science - A | 4 |
| 23003 | Electrical Engineering | 6 |

**Required Columns**:
- `registerno`: Student registration number (numeric or alphanumeric)
- `department`: Full department name (must match existing departments)
- `semester`: Semester number (1-8)

**🚨 CRITICAL REQUIREMENTS**:
- ⚠️ First row must be column headers
- ⚠️ No empty rows
- ⚠️ Registration numbers must be unique
- ⚠️ **Department names must match EXACTLY** (copy from reference file!)
- ⚠️ **Semester names must match EXACTLY** (copy from reference file!)
- ⚠️ Even one extra space or character will cause error!

**Example of Common Errors**:

❌ **WRONG**:
- `Computer Science A` (missing dash)
- `Computer Science- A` (space before dash)
- `Computer Science -A` (no space after dash)
- ` Computer Science - A` (leading space)
- `Computer Science - A ` (trailing space)

✅ **CORRECT**:
- `Computer Science - A` (exactly as shown in reference file)

**How to Ensure Exact Match**:
1. Open the REFERENCE_Names.xlsx file
2. Go to "Departments" sheet
3. **COPY** the department name (don't type it!)
4. **PASTE** into your student Excel file
5. Repeat for semester names from "Semesters" sheet

---

**Step 2: Upload File**

1. Login as admin
2. Go to **"Student Management"** from dashboard
3. Click **"Choose File"** button
4. Select your Excel file
5. Choose upload mode:
   - **Replace**: Delete all existing students and upload new list
   - **Append**: Add to existing students
6. Click **"Upload"**
7. Wait for confirmation message

**Step 3: Verify Upload**

1. Click **"View All Students"** button
2. Check students are listed correctly
3. Verify registration numbers, departments, and semesters
4. Filter by department/semester to check specific groups

---

#### Deleting Students

**Single Student Deletion**:

1. Go to **"Student Management"**
2. Select department and semester
3. Click **"View Students"**
4. Find the student you want to delete
5. Click **"Delete"** button next to their name
6. Confirm deletion
7. Student is removed from database

**Multi-Delete (Delete Multiple Students)**:

Use this feature to delete several students at once:

1. Go to **"Student Management"**
2. Select department and semester
3. Click **"View Students"**
4. Check the checkbox next to each student you want to delete
   - You can select multiple students
   - Or use "Select All" checkbox to select all visible students
5. Click **"Delete Selected"** button (appears when students are selected)
6. Confirm deletion (a popup will show how many students will be deleted)
7. Selected students are removed from database

**⚠️ Important Notes About Deletion**:
- Deletion is **permanent** and cannot be undone
- Make sure you have a backup before mass deletions
- If a student has already submitted feedback, consider whether to delete them
- Deleting a student does NOT delete their submitted feedback (separate tables)

**When to Use Multi-Delete**:
- Removing an entire batch of students who graduated
- Cleaning up test/dummy data
- Removing students who transferred to another department
- Bulk cleanup at end of academic year

---

#### Adding Students Manually (via Supabase)

If you have database access:

1. Login to Supabase
2. Go to **"Table Editor"**
3. Select **"students"** table
4. Click **"Insert row"**
5. Fill in: registerno, department, semester
6. Click **"Save"**

---

### Managing Mappings

#### Understanding Staff-Subject Mappings

Mappings define which faculty members teach which subjects to which classes. Each mapping contains:

- **Department**: e.g., "Computer Science - A"
- **Semester**: e.g., "4"
- **Staff**: Faculty name, e.g., "Dr. John Doe"
- **Subject**: Subject name, e.g., "Data Structures"

#### Creating Mappings Manually

**Step 1: Access Mapping Page**

1. Login as admin
2. Go to **"Staff-Subject Mapping"** from dashboard

**Step 2: Select Department and Semester**

1. Choose department from dropdown
2. Choose semester from dropdown

**Step 3: Add Staff-Subject Pairs**

1. For each faculty teaching this class:
   - Select **Staff** name from dropdown
   - Select **Subject** from dropdown
2. Click **"+ Add Another"** to add more mappings
3. Repeat for all faculty in this class

**Step 4: Save Mappings**

1. Review all entries
2. Click **"Save All Mappings"**
3. Wait for success confirmation

#### Uploading Mappings via Excel

**⚠️ CRITICAL: Download Reference File First!**

Before creating your mapping Excel file, **YOU MUST download the reference file** containing exact names for departments, semesters, staff, and subjects. Mismatched names will cause errors!

**Step 0: Download Reference File** (DO THIS FIRST!)

1. Login as admin
2. Go to **"Staff-Subject Mapping"** or **"Student Management"**
3. Click **"Download Reference File"** button
4. Open `REFERENCE_Names.xlsx`
5. Note the 4 sheets with exact names:
   - **Departments**: Copy exact department names
   - **Semesters**: Copy exact semester names
   - **Staff**: Copy exact staff names
   - **Subjects**: Copy exact subject names

**Step 1: Download Sample Template**

1. Go to **"Staff-Subject Mapping"** page
2. Click **"Download Sample Excel Template"**
3. Open the downloaded file

**Step 2: Fill in Template**

Sample format:

| department | semester | staff | subject |
|------------|----------|-------|---------|
| Computer Science - A | 4 | Dr. John Doe | Data Structures |
| Computer Science - A | 4 | Prof. Jane Smith | Operating Systems |
| Computer Science - A | 4 | Dr. Alex Kumar | Database Management |

**🚨 CRITICAL REQUIREMENTS**:
- ⚠️ **All values must match EXACTLY** with reference file!
- ⚠️ Staff and subjects must be added first (see [Bulk Operations](#bulk-operations))
- ⚠️ Department names: **COPY from reference file**, don't type!
- ⚠️ Semester names: **COPY from reference file**, don't type!
- ⚠️ Staff names: **COPY from reference file**, don't type!
- ⚠️ Subject names: **COPY from reference file**, don't type!
- ⚠️ Even a single extra space will cause upload failure!

**Why This Matters**:
- ❌ `Computer Science A` ≠ `Computer Science - A`
- ❌ `Dr John Doe` ≠ `Dr. John Doe`
- ❌ `Data structure` ≠ `Data Structures`
- ✅ Always COPY-PASTE from reference file!

**How to Fill Correctly**:
1. Open `REFERENCE_Names.xlsx` in one window
2. Open your mapping Excel file in another window
3. For each row:
   - Go to "Departments" sheet → **COPY** department name → **PASTE** in your file
   - Go to "Semesters" sheet → **COPY** semester → **PASTE** in your file
   - Go to "Staff" sheet → **COPY** staff name → **PASTE** in your file
   - Go to "Subjects" sheet → **COPY** subject name → **PASTE** in your file
4. **NEVER TYPE** these values manually!

**Step 3: Upload File**

1. Click **"Choose File"** in the upload section
2. Select your filled Excel file
3. Choose upload mode:
   - **Replace**: Delete existing mappings for this dept/semester
   - **Append**: Add to existing mappings
4. Click **"Upload Excel"**
5. Review upload summary
6. Confirm upload

#### Viewing and Managing Mappings

**View All Mappings**:

1. Go to **"Staff-Subject Mapping"**
2. Click **"View All Mappings"** tab
3. **Filter by**:
   - Department (dropdown)
   - Semester (dropdown)
   - Staff name (search box)

**Delete Mappings**:

1. Find the mapping in the table
2. Click **"Delete"** button next to it
3. Confirm deletion
4. Mapping is removed

---

### Bulk Operations

#### Bulk Add Staff

**Purpose**: Add multiple faculty members at once

**Steps**:

1. Login as admin
2. Go to **"Bulk Add Staff/Subjects"** from dashboard
3. In the **"Add Staff"** section:
   - Enter one staff name per line
   - Example:
     ```
     Dr. John Doe
     Prof. Jane Smith
     Dr. Alex Kumar
     Mr. Raj Patel
     ```
4. Click **"Add All Staff"**
5. System will:
   - Add new staff members
   - Skip duplicates
   - Show summary of additions

**Important Notes**:
- ✅ Duplicates are automatically ignored
- ✅ Whitespace is trimmed
- ✅ Empty lines are ignored
- ✅ Case-sensitive names

#### Bulk Add Subjects

**Purpose**: Add multiple subjects at once

**Steps**:

1. Go to **"Bulk Add Staff/Subjects"**
2. In the **"Add Subjects"** section:
   - Enter one subject name per line
   - Example:
     ```
     Data Structures
     Operating Systems
     Database Management
     Computer Networks
     Software Engineering
     ```
3. Click **"Add All Subjects"**
4. System will add new subjects and skip duplicates

---

### Generating Reports

#### Creating Feedback Reports

**Step 1: Access Report Generation**

1. Login as admin
2. Go to **"Generate Reports"** from dashboard (or contact HOD for access)

**Step 2: Select Filters**

1. **Department**: Choose specific department or "All Departments"
2. **Semester**: Choose specific semester or "All Semesters"
3. **Date Range** (if available): Select start and end dates

**Step 3: Generate Report**

1. Click **"Generate Report"** button
2. Wait for report processing (may take 30-60 seconds)
3. Report will display on screen

**Step 4: View Report Contents**

Reports include:

- **Summary Statistics**:
  - Total feedback submissions
  - Number of students
  - Number of faculty evaluated
  - Average ratings across department

- **Individual Faculty Ratings**:
  - Faculty name and subject
  - Ratings for all 10 parameters
  - Overall average rating
  - Number of feedback responses

- **Visual Charts** (if available):
  - Bar charts comparing faculty
  - Line graphs showing trends
  - Distribution of ratings

**Step 5: Download Report**

1. Click **"Download as PDF"** button (if available)
2. Or use browser print function (Ctrl+P) and save as PDF

#### Report Interpretation

**High Performers** (Average > 8.0):
- Recognize and reward
- Share best practices with other faculty

**Average Performers** (Average 6.0-8.0):
- Standard performance
- Encourage continued improvement

**Low Performers** (Average < 6.0):
- Provide support and training
- Create improvement plans
- Monitor progress

---

## ❓ Frequently Asked Questions (FAQ)

### For Students

**Q1: Can I change my feedback after submitting?**

**A**: No, feedback submissions are final. Please review carefully before submitting.

---

**Q2: Will faculty know who gave which rating?**

**A**: No, all feedback is anonymous. Registration numbers are encrypted and not visible to faculty.

---

**Q3: What if I forgot to rate one faculty member?**

**A**: You cannot submit partial feedback. All faculty members assigned to your class must be rated before submission.

---

**Q4: Can I submit feedback from my mobile phone?**

**A**: Yes, the system is mobile-friendly and works on smartphones and tablets.

---

**Q5: What happens if I refresh the page during feedback?**

**A**: Your ratings will be lost. You'll need to start over. Do not refresh until after submission.

---

**Q6: How long does the feedback window stay open?**

**A**: Check with your department for specific deadlines. Typically 1-2 weeks.

---

### For Admin

**Q7: Can I edit a student's registration number after adding?**

**A**: No, registration numbers cannot be edited. You must delete and re-add the student.

---

**Q8: What if I upload the wrong Excel file?**

**A**: If you used "Replace" mode, the previous data is overwritten. You'll need to re-upload the correct file. Always use "Append" mode for safety.

---

**Q9: How do I remove duplicate students?**

**A**: Access Supabase database directly and delete duplicates from the "students" table.

---

**Q10: Can mappings be edited after creation?**

**A**: No direct edit. You must delete the old mapping and create a new one.

---

## 📞 Support

### Getting Help

**For Students**:
- Contact your class representative
- Email IT support: [support-email]
- Visit IT department in person

**For Faculty**:
- Contact your HOD
- Contact admin office
- Email IT support: [support-email]

**For Admin**:
- Check DEPLOYMENT_GUIDE.md for technical issues
- Access Render logs for error messages
- Contact technical support: [tech-support-email]

### Reporting Bugs

If you encounter a bug:

1. Note the exact error message
2. Take a screenshot
3. Note what you were doing when it occurred
4. Email details to: [bug-report-email]

### Feature Requests

Have ideas for improvements?

1. Document your suggestion clearly
2. Explain the benefit
3. Submit to: [feature-request-email]

---

## 📄 Document Information

**Document Version**: 2.0  
**System Version**: 2.0  
**Last Updated**: January 2025  
**Created by**: GenrecAI  
**Website**: [Genrec.AI](https://revolvo-ai.netlify.app)

---

**Thank you for using the VSB Engineering College Faculty Feedback System!** 🎓
