import csv
import os
import logging
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer, Frame, PageTemplate
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.pdfgen import canvas
from datetime import datetime

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('feedback_report.log'),
        logging.StreamHandler()
    ]
)

def normalize_department_name(department):
    """Normalize department name for consistent matching"""
    if not department:
        return ''
    # Convert to string and normalize
    dept = str(department).strip()
    # Remove extra spaces
    while '  ' in dept:
        dept = dept.replace('  ', ' ')
    # Standardize section indicators
    dept = dept.replace(' - ', '-')
    dept = dept.replace(' -', '-')
    dept = dept.replace('- ', '-')
    # Remove "Semester" prefix if present
    dept = dept.replace('Semester ', '')
    return dept

def normalize_semester(semester):
    """Normalize semester value"""
    if not semester:
        return ''
    # Remove any non-digit characters
    sem = ''.join(filter(str.isdigit, str(semester)))
    return sem

def generate_non_submission_report(department, semester):
    """
    Generate a PDF report of students who have not submitted feedback.
    
    Args:
        department (str): The department to filter by (e.g., "Computer Science and Engineering -A")
        semester (str): The semester to filter by (e.g., "2", "4", "6")
    """
    # Normalize department name
    department = normalize_department_name(department)
    semester = normalize_semester(semester)
    
    # Get submitted register numbers from submitted.csv
    submitted_regnos = set()
    logging.info(f"Processing feedback submissions for '{department}' - Semester '{semester}'")
    
    logging.info("Reading submitted.csv file...")
    if not os.path.exists('submitted.csv'):
        logging.warning("submitted.csv file not found!")
        return None
        
    with open('submitted.csv', 'r', newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        
        # Verify column names
        columns = reader.fieldnames
        logging.debug(f"Found columns in submitted.csv: {columns}")
        required_columns = ['Department', 'Semester', 'Original RegNo']
        missing_columns = [col for col in required_columns if col not in columns]
        if missing_columns:
            logging.error(f"Missing required columns in submitted.csv: {missing_columns}")
            return None
        
        submission_count = 0
        for row in reader:
            current_dept = normalize_department_name(row['Department'])
            current_sem = normalize_semester(row['Semester'])
            current_regno = row['Original RegNo'].strip()
            
            # Debug each row
            logging.debug(f"Checking submission:")
            logging.debug(f"Department: '{current_dept}' vs Expected: '{department}'")
            logging.debug(f"Semester: '{current_sem}' vs Expected: '{semester}'")
            logging.debug(f"Register No: '{current_regno}'")
            
            if (current_dept == department and current_sem == semester):
                submitted_regnos.add(current_regno)
                submission_count += 1
                logging.debug(f"Matched submission: {current_regno}")
            else:
                logging.debug("No match")
        
        logging.info(f"Found {submission_count} submissions for {department} semester {semester}")
    
    # Get all students from the specified department and semester
    logging.info("Reading students.csv file...")
    if not os.path.exists('students.csv'):
        logging.error("students.csv file not found!")
        return None
        
    all_students = []
    with open('students.csv', 'r', newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        
        # Verify column names
        columns = reader.fieldnames
        logging.debug(f"Found columns in students.csv: {columns}")
        required_columns = ['department', 'semester', 'registerno']
        missing_columns = [col for col in required_columns if col not in columns]
        if missing_columns:
            logging.error(f"Missing required columns in students.csv: {missing_columns}")
            return None
            
        student_count = 0
        for row in reader:
            current_dept = normalize_department_name(row['department'])
            current_sem = normalize_semester(row['semester'])
            current_regno = row['registerno'].strip()
            
            # Debug each row
            logging.debug(f"Checking student:")
            logging.debug(f"Department: '{current_dept}' vs Expected: '{department}'")
            logging.debug(f"Semester: '{current_sem}' vs Expected: '{semester}'")
            logging.debug(f"Register No: '{current_regno}'")
            
            if (current_dept == department and current_sem == semester):
                student_info = {
                    'registerno': current_regno,
                    'department': current_dept,
                    'semester': current_sem
                }
                all_students.append(student_info)
                student_count += 1
                logging.debug(f"Matched student: {current_regno}")
            else:
                logging.debug("No match")
    
    logging.info(f"Found {student_count} students in {department} semester {semester}")
    logging.info("Checking for non-submissions...")
    
    # Find students who haven't submitted
    non_submitted = []
    for student in all_students:
        regno = student['registerno']
        if regno not in submitted_regnos:
            non_submitted.append(student)
            logging.debug(f"Non-submission found: {regno}")
        else:
            logging.debug(f"Submission verified for: {regno}")
    
    logging.info(f"Total students: {len(all_students)}")
    logging.info(f"Total submissions: {len(submitted_regnos)}")
    logging.info(f"Non-submissions: {len(non_submitted)}")
    
    # Generate PDF report
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"non_submission_report_{department.replace(' ', '_')}_{semester}_{timestamp}.pdf"
    pdf_path = os.path.join(os.getcwd(), filename)
    
    def add_watermark(canvas, doc):
        canvas.saveState()
        # Create italic style for watermark
        watermark_style = ParagraphStyle(
            'WatermarkStyle',
            parent=styles['Italic'],
            textColor=colors.grey,
            fontSize=8,
            alignment=1  # Center alignment
        )
        watermark_text = Paragraph(
            "THIS REPORT AND SITE IS CREATED AND MANAGED BY GENRECAI",
            watermark_style
        )
        # Draw watermark at bottom of page
        w, h = watermark_text.wrap(doc.width, doc.bottomMargin)
        watermark_text.drawOn(canvas, doc.leftMargin, doc.bottomMargin/3)
        canvas.restoreState()

    doc = SimpleDocTemplate(
        pdf_path,
        pagesize=letter,
        rightMargin=36,
        leftMargin=36,
        topMargin=36,
        bottomMargin=36
    )
    
    # Create content
    styles = getSampleStyleSheet()
    
    # Set up the template with watermark
    frame = Frame(
        doc.leftMargin,
        doc.bottomMargin,
        doc.width,
        doc.height,
        id='normal'
    )
    template = PageTemplate(
        id='watermarked',
        frames=frame,
        onPage=add_watermark
    )
    doc.addPageTemplates([template])
    content = []
    
    # Title
    title_style = styles['Heading1']
    title_style.alignment = 1
    content.append(Paragraph("VSB ENGINEERING COLLEGE", title_style))
    content.append(Spacer(1, 12))
    
    # Subtitle
    subtitle_style = styles['Heading2']
    subtitle_style.alignment = 1
    content.append(Paragraph("Students Who Have Not Submitted Feedback", subtitle_style))
    content.append(Spacer(1, 12))
    
    # Department and Semester
    dept_sem_style = styles['Heading3']
    dept_sem_style.alignment = 1
    content.append(Paragraph(f"Department: {department} | Semester: {semester}", dept_sem_style))
    content.append(Spacer(1, 12))
    
    # Date
    date_style = styles['Normal']
    date_style.alignment = 1
    content.append(Paragraph(f"Generated on: {datetime.now().strftime('%d-%m-%Y %H:%M:%S')}", date_style))
    content.append(Spacer(1, 24))
    
    # Statistics
    total = len(all_students)
    not_submitted = len(non_submitted)
    submitted = total - not_submitted
    stats = Paragraph(
        f"Total Students: {total} | Submitted: {submitted} | Not Submitted: {not_submitted}",
        styles['Normal']
    )
    stats.alignment = 1
    content.append(stats)
    content.append(Spacer(1, 24))
    
    if non_submitted:
        # Create table
        table_data = [['#', 'Register No.', 'Department', 'Semester']]
        for i, student in enumerate(non_submitted, 1):
            table_data.append([
                i,
                student['registerno'],
                student['department'],
                student['semester']
            ])
        
        table = Table(table_data, repeatRows=1)
        table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.lightblue),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('FONTSIZE', (0, 0), (-1, 0), 12),
            ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
            ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ]))
        content.append(table)
    else:
        msg = Paragraph("All students have submitted their feedback!", styles['Heading3'])
        msg.alignment = 1
        content.append(msg)
    
    # Generate PDF
    doc.build(content)
    logging.info(f"Report generated: {filename}")
    return pdf_path
