"""
Utils module - UPDATED to use SQLite database instead of CSV files
"""
import hashlib
import base64
import logging
import os
# import dotenv

# dotenv.load_dotenv()
# Lazy import to avoid circular dependency
def _get_db():
    """Get database connection - lazy import to avoid circular dependency."""
    from app.models.database import get_db
    return get_db()

# Configure logging
logging.basicConfig(
    format='%(asctime)s - %(levelname)s - %(message)s',
    level=os.getenv('LOG_LEVEL', 'WARNING').upper(),
    datefmt='%Y-%m-%d %H:%M:%S'
)

# Secret key for encryption (in a real application, this should be stored securely)
SECRET_KEY = "VSB_FEEDBACK_SYSTEM_SECRET_KEY"

def normalize_regno(regno):
    """Normalize a registration number by removing leading zeros."""
    try:
        return str(int(regno))
    except (ValueError, TypeError):
        return regno

def encrypt_regno(regno):
    """
    Encrypt a registration number using a one-way hash function.
    """
    if not regno:
        logging.error("Empty registration number")
        return ""
    
    normalized_regno = normalize_regno(regno)
    input_str = normalized_regno + SECRET_KEY
    hash_obj = hashlib.sha256(input_str.encode())
    hash_str = base64.b64encode(hash_obj.digest()).decode('utf-8')
    return hash_str[:32]

def is_encrypted(value):
    """Check if a value is already encrypted."""
    if not value:
        return False
    try:
        if len(value) == 32:
            return all(c in "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/=" for c in value)
    except Exception as e:
        logging.error(f"Error checking encryption: {e}")
    return False

def read_csv_as_list(filename):
    """
    UPDATED: Return a list of values from the database instead of CSV file.
    Kept for backward compatibility.
    """
    client = _get_db()
    
    # Determine which table to query based on filename
    if 'departments' in filename.lower():
        result = client.table('departments').select('name').order('name').execute()
    elif 'semesters' in filename.lower():
        result = client.table('semesters').select('name').order('name').execute()
    elif 'staff' in filename.lower():
        result = client.table('staff').select('name').order('name').execute()
    elif 'subject' in filename.lower():
        result = client.table('subjects').select('name').order('name').execute()
    else:
        return []
    
    return [row['name'] for row in result.data]

def load_admin_mapping(department, semester):
    """
    UPDATED: Return a list of mapping dictionaries from database.
    """
    mappings = []
    dep_norm = department.strip()
    sem_norm = semester.strip()
    
    # Normalize semester (remove "Semester" prefix if present)
    if sem_norm.lower().startswith("semester"):
        sem_norm = sem_norm[len("semester"):].strip()
    
    client = _get_db()
    result = client.table('admin_mappings')\
        .select('department, semester, staff, subject')\
        .eq('department', dep_norm)\
        .eq('semester', sem_norm)\
        .execute()
    
    for row in result.data:
        mappings.append({
            'department': row['department'],
            'semester': row['semester'],
            'staff': row['staff'],
            'subject': row['subject']
        })
    
    return mappings

def update_admin_mappings(department, semester, new_mappings):
    """
    UPDATED: Overwrite existing mappings in database.
    """
    dep_norm = department.strip()
    sem_norm = semester.strip()
    
    # Normalize semester
    if sem_norm.lower().startswith("semester"):
        sem_norm = sem_norm[len("semester"):].strip()
    
    client = _get_db()
    
    # Delete existing mappings for this department/semester
    client.table('admin_mappings')\
        .delete()\
        .eq('department', dep_norm)\
        .eq('semester', sem_norm)\
        .execute()
    
    # Insert new mappings
    mappings_to_insert = [
        {
            'department': mapping.get('department', dep_norm),
            'semester': mapping.get('semester', sem_norm),
            'staff': mapping.get('staff', ''),
            'subject': mapping.get('subject', '')
        }
        for mapping in new_mappings
    ]
    
    if mappings_to_insert:
        client.table('admin_mappings').insert(mappings_to_insert).execute()

def append_ratings(rating_rows):
    """
    UPDATED: Append rating rows to database instead of CSV.
    """
    client = _get_db()
    
    for row in rating_rows:
        # Insert rating
        rating_data = {
            'registerno': row['registerno'],
            'department': row['department'],
            'semester': row['semester'],
            'staff': row['staff'],
            'subject': row['subject'],
            'q1': float(row['q1']),
            'q2': float(row['q2']),
            'q3': float(row['q3']),
            'q4': float(row['q4']),
            'q5': float(row['q5']),
            'q6': float(row['q6']),
            'q7': float(row['q7']),
            'q8': float(row['q8']),
            'q9': float(row['q9']),
            'q10': float(row['q10']),
            'average': float(row['average'])
        }
        client.table('ratings').insert(rating_data).execute()
        
        # Mark as submitted (check if already exists first)
        existing = client.table('submitted_feedback')\
            .select('registerno')\
            .eq('registerno', row['registerno'])\
            .execute()
        
        if not existing.data:
            client.table('submitted_feedback').insert({'registerno': row['registerno']}).execute()

def get_student_info(registerno):
    """
    UPDATED: Return student info from database by registration number.
    """
    logging.info(f"Validating {registerno}")
    reg_num = normalize_regno(registerno)
    
    client = _get_db()
    result = client.table('students')\
        .select('registerno, department, semester')\
        .eq('registerno', reg_num)\
        .execute()
    
    if result.data:
        row = result.data[0]
        logging.info(f"Validated {registerno} [Status: OK]")
        return {
            'registerno': row['registerno'],
            'department': row['department'],
            'semester': row['semester']
        }
    
    logging.info(f"Validated {registerno} [Status: FAILED]")
    return None

def has_submitted_feedback(registerno):
    """
    UPDATED: Return True if the student has already submitted feedback (from database).
    """
    reg_num = normalize_regno(registerno)
    
    client = _get_db()
    result = client.table('submitted_feedback')\
        .select('registerno')\
        .eq('registerno', reg_num)\
        .execute()
    
    if result.data:
        logging.info(f"Feedback found for {registerno}")
        return True
    
    return False

def update_mainratings():
    """
    UPDATED: Aggregate ratings from database.
    This function is kept for compatibility but now works with database.
    """
    aggregated = {}
    
    client = _get_db()
    result = client.table('ratings')\
        .select('department, semester, staff, subject, q1, q2, q3, q4, q5, q6, q7, q8, q9, q10, average')\
        .execute()
    
    for row in result.data:
        dep, sem, staff, subject = row['department'], row['semester'], row['staff'], row['subject']
        key = (dep, sem, staff, subject)
        
        if key not in aggregated:
            aggregated[key] = {
                'q_sums': [0.0] * 10,
                'count': 0,
                'total_avg': 0.0
            }
        
        # Add individual question ratings
        for i in range(1, 11):
            aggregated[key]['q_sums'][i-1] += row[f'q{i}']
        
        aggregated[key]['total_avg'] += row['average']
        aggregated[key]['count'] += 1
    
    # Store aggregated results (you can save this to a table if needed)
    return aggregated

def normalize_semester(semester):
    """Normalize semester string by removing 'semester' prefix if present."""
    semester = semester.strip()
    if semester.lower().startswith("semester"):
        semester = semester[len("semester"):].strip()
    return semester
