from flask import Blueprint, render_template, request, redirect, url_for, flash, send_file, make_response, current_app
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter, landscape
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer, Image
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from utils import read_csv_as_list, update_mainratings, normalize_semester
from config import (DEPARTMENTS_FILE, SEMESTERS_FILE, MAINRATING_FILE,
                   RATING_FILE, STUDENT_FILE, REQUIRED_FILES, ADMIN_MAPPING_FILE)
from app.models.database import get_db
import subprocess
from report_non_submission import generate_non_submission_report
import os
import csv
import io
import base64
import matplotlib.pyplot as plt
from datetime import datetime
import textwrap
from report_generator import generate_feedback_report
import shutil

hod_bp = Blueprint('hod', __name__)

def create_empty_csv(file_path, headers):
    """Create a new CSV file with only headers."""
    with open(file_path, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(headers)

def safe_move_file(src, dst):
    """Move file if it exists, create empty one if it doesn't."""
    if os.path.exists(src):
        shutil.copy2(src, dst)  # Copy with metadata

@hod_bp.route('/hod', methods=['GET', 'POST'])
def hod_login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        if username == 'admin' and password == 'admin':
            return redirect(url_for('hod.hod_select'))
        else:
            flash("Incorrect credentials.", "danger")
            return redirect(url_for('hod.hod_login'))
    return render_template('hod_login.html')

@hod_bp.route('/hod/select', methods=['GET', 'POST'])
def hod_select():
    departments = read_csv_as_list(DEPARTMENTS_FILE)
    semesters = read_csv_as_list(SEMESTERS_FILE)
    
    if request.method == 'POST':
        action = request.form.get('action', '')
        department = request.form.get('department')
        semester = request.form.get('semester')
        
        if not department or not semester:
            flash("Please select both department and semester.", "danger")
            return redirect(url_for('hod.hod_select'))
        
        if action in ['view_pdf', 'download_pdf']:
            try:
                normalized_input_semester = normalize_semester(semester)
                update_mainratings()
                
                feedback_data = {}
                staff_counter = 1
                
                # Query ratings from database and calculate averages
                # Try multiple semester formats since data might be inconsistent
                sem_variations = [
                    normalized_input_semester,
                    f"Semester {normalized_input_semester}",
                    semester.strip()
                ]
                
                client = get_db()
                try:
                    result = client.rpc('get_average_ratings', {
                        'dept': department.strip(),
                        'sem_variations': sem_variations
                    }).execute()
                    
                    # Alternative: Manual aggregation if RPC not available
                    result = client.table('ratings')\
                        .select('staff, subject, q1, q2, q3, q4, q5, q6, q7, q8, q9, q10')\
                        .eq('department', department.strip())\
                        .in_('semester', sem_variations)\
                        .execute()
                    
                    # Group by staff and subject manually
                    from collections import defaultdict
                    grouped_data = defaultdict(lambda: {'q1': [], 'q2': [], 'q3': [], 'q4': [], 'q5': [], 
                                                         'q6': [], 'q7': [], 'q8': [], 'q9': [], 'q10': []})
                    
                    for row in result.data:
                        key = (row['staff'], row['subject'])
                        for i in range(1, 11):
                            grouped_data[key][f'q{i}'].append(row[f'q{i}'])
                    
                    # Calculate averages
                    aggregated_results = []
                    for (staff, subject), scores in grouped_data.items():
                        avg_row = {'staff': staff, 'subject': subject}
                        for i in range(1, 11):
                            q_scores = scores[f'q{i}']
                            avg_row[f'q{i}_avg'] = sum(q_scores) / len(q_scores) if q_scores else 0
                        aggregated_results.append(avg_row)
                except Exception as e:
                    current_app.logger.error(f"Database Error: {str(e)}")
                    flash(f"Error fetching ratings: {str(e)}", "danger")
                    return redirect(url_for('hod.hod_select'))
                    
                    for row in aggregated_results:
                        staff_name = row['staff'].strip()
                        subject_name = row['subject'].strip()
                        scores = [row[f'q{i}_avg'] for i in range(1, 11)]
                        
                        key = f"{staff_name}_{subject_name}"
                        feedback_data[key] = {
                            'reference': f'S{staff_counter}',
                            'staff_name': staff_name,
                            'subject': subject_name,
                            'scores': scores
                        }
                        staff_counter += 1
                
                if not feedback_data:
                    flash("No rating data found for the selected department and semester.", "danger")
                    return redirect(url_for('hod.hod_select'))
                
                # Generate PDF report
                year = (int(normalized_input_semester) + 1) // 2
                try:
                    pdf_path = generate_feedback_report(
                        academic_year=str(datetime.now().year),
                        branch=department,
                        semester=semester,
                        year=str(year),
                        feedback_data=feedback_data
                    )
                    
                    if not pdf_path or not os.path.exists(pdf_path):
                        raise ValueError("PDF file was not generated properly")
                    
                    # Read the generated PDF
                    with open(pdf_path, 'rb') as f:
                        pdf_content = f.read()
                    
                    # Create response
                    response = make_response(pdf_content)
                    response.headers['Content-Type'] = 'application/pdf'
                    
                    if action == 'download_pdf':
                        response.headers['Content-Disposition'] = f'attachment; filename={os.path.basename(pdf_path)}'
                    else:  # view_pdf
                        response.headers['Content-Disposition'] = f'inline; filename={os.path.basename(pdf_path)}'
                    
                    # Clean up the temporary PDF file
                    try:
                        os.remove(pdf_path)
                    except:
                        pass
                    
                    return response
                
                except Exception as e:
                    current_app.logger.error(f"PDF Generation Error: {str(e)}")
                    flash(f"Error generating PDF report: {str(e)}", "danger")
                    return redirect(url_for('hod.hod_select'))
                
            except Exception as e:
                current_app.logger.error(f"General Error: {str(e)}")
                flash(f"Error processing request: {str(e)}", "danger")
                return redirect(url_for('hod.hod_select'))
        
        elif action == 'non_submission_report':
            try:
                # Generate the non-submission report directly from database
                pdf_path = generate_non_submission_report(department, semester)
                
                if not pdf_path or not os.path.exists(pdf_path):
                    raise ValueError("PDF file was not generated properly")
                
                # Read the generated PDF
                with open(pdf_path, 'rb') as f:
                    pdf_content = f.read()
                
                # Create response
                response = make_response(pdf_content)
                response.headers['Content-Type'] = 'application/pdf'
                response.headers['Content-Disposition'] = f'inline; filename={os.path.basename(pdf_path)}'
                
                # Clean up the temporary PDF file
                try:
                    os.remove(pdf_path)
                except:
                    pass
                
                return response
                
            except Exception as e:
                current_app.logger.error(f"Report generation error: {str(e)}")
                flash(f"Error generating report: {str(e)}", "danger")
                return redirect(url_for('hod.hod_select'))
                
        elif action == 'archive':
            try:
                # Create history directory
                if not os.path.exists('history'):
                    os.makedirs('history')
                
                timestamp = datetime.now().strftime("%d-%b-%Y--%H-%M-%S")
                archive_dir = os.path.join('history', timestamp)
                if not os.path.exists(archive_dir):
                    os.makedirs(archive_dir)
                
                # Backup database file
                db_path = os.path.join('data', 'feedback.db')
                if os.path.exists(db_path):
                    archive_db_path = os.path.join(archive_dir, 'feedback_backup.db')
                    shutil.copy2(db_path, archive_db_path)
                    current_app.logger.info(f"Database backed up to: {archive_db_path}")
                
                # Clear specific tables (keep: staff, subjects, semesters, departments)
                client = get_db()
                try:
                    # Clear ratings table
                    ratings_result = client.table('ratings').delete().neq('id', 0).execute()
                    ratings_deleted = len(ratings_result.data) if ratings_result.data else 0
                    current_app.logger.info(f"Deleted {ratings_deleted} rows from ratings table")
                    
                    # Clear submitted_feedback table
                    submitted_result = client.table('submitted_feedback').delete().neq('id', 0).execute()
                    submitted_deleted = len(submitted_result.data) if submitted_result.data else 0
                    current_app.logger.info(f"Deleted {submitted_deleted} rows from submitted_feedback table")
                    
                    # Clear admin_mappings table
                    mappings_result = client.table('admin_mappings').delete().neq('id', 0).execute()
                    mappings_deleted = len(mappings_result.data) if mappings_result.data else 0
                    current_app.logger.info(f"Deleted {mappings_deleted} rows from admin_mappings table")
                    
                    # Clear students table
                    students_result = client.table('students').delete().neq('id', 0).execute()
                    students_deleted = len(students_result.data) if students_result.data else 0
                    current_app.logger.info(f"Deleted {students_deleted} rows from students table")
                except Exception as e:
                    current_app.logger.error(f"Error clearing tables: {str(e)}")
                    flash(f"Error clearing tables: {str(e)}", "danger")
                
                # Delete unnecessary files
                files_to_delete = [
                    'feedback_report.log',
                    'submitted.csv',
                    'students.csv'
                ]
                for file in files_to_delete:
                    if os.path.exists(file):
                        try:
                            os.remove(file)
                            current_app.logger.info(f"Deleted file: {file}")
                        except Exception as e:
                            current_app.logger.warning(f"Could not delete {file}: {e}")
                
                # Delete generated PDF reports
                for file in os.listdir('.'):
                    if file.startswith('feedback_report_') and file.endswith('.pdf'):
                        try:
                            os.remove(file)
                            current_app.logger.info(f"Deleted report: {file}")
                        except Exception as e:
                            current_app.logger.warning(f"Could not delete {file}: {e}")
                    elif file.startswith('non_submission_report_') and file.endswith('.pdf'):
                        try:
                            os.remove(file)
                            current_app.logger.info(f"Deleted report: {file}")
                        except Exception as e:
                            current_app.logger.warning(f"Could not delete {file}: {e}")
                
                flash("Data successfully archived and system reset. Preserved: staff, subjects, semesters, departments.", "success")
                
            except Exception as e:
                current_app.logger.error(f"Error during archival: {str(e)}")
                flash(f"Error during archival process: {str(e)}", "danger")
            
            return redirect(url_for('hod.hod_select'))
    
    return render_template('hod_select.html', 
                         departments=departments,
                         semesters=semesters)
