import csv
import hashlib
import base64
import os

# Secret key - same as in the original code
SECRET_KEY = "VSB_FEEDBACK_SYSTEM_SECRET_KEY"

def normalize_regno(regno):
    """Normalize a registration number while preserving the full format."""
    if not regno:
        return ""
    return str(regno).strip()

def encrypt_regno(regno):
    """Recreate the encryption function from the original code"""
    if not regno:
        return ""
    
    # Normalize the registration number
    normalized_regno = normalize_regno(regno)
    
    # Create a hash using the normalized number and secret key
    input_str = normalized_regno + SECRET_KEY
    
    hash_obj = hashlib.sha256(input_str.encode())
    hash_str = base64.b64encode(hash_obj.digest()).decode('utf-8')
    result = hash_str[:32]
    
    return result

def get_unique_encrypted_regnos(ratings_file):
    """Extract all unique encrypted registration numbers from the ratings file"""
    encrypted_regnos = {}  # Using dict to store regno -> (dept, sem) mapping
    
    with open(ratings_file, 'r', newline='', encoding='utf-8') as infile:
        reader = csv.DictReader(infile)
        for row in reader:
            if 'registerno' in row and row['registerno']:
                regno = row['registerno'].strip()
                dept = row.get('department', '').strip()
                sem = row.get('semester', '').strip()
                if regno:
                    encrypted_regnos[regno] = (dept, sem)
    
    return encrypted_regnos

def get_students_data(students_file):
    """Extract all registration numbers from the students file"""
    students_data = []
    
    with open(students_file, 'r', newline='', encoding='utf-8') as infile:
        reader = csv.DictReader(infile)
        for row in reader:
            if 'registerno' in row and row['registerno']:
                students_data.append({
                    'registerno': normalize_regno(row['registerno']),
                    'department': row.get('department', ''),
                    'semester': row.get('semester', '')
                })
    
    return students_data

def main():
    # Input and output file paths
    ratings_file = 'ratings.csv'
    students_file = 'students.csv'
    decrypted_file = 'submitted.csv'
    
    # Check if files exist
    for file_path in [ratings_file, students_file]:
        if not os.path.exists(file_path):
            print(f"Error: {file_path} does not exist")
            return
    
    print(f"Extracting unique encrypted registration numbers from {ratings_file}...")
    encrypted_regnos_info = get_unique_encrypted_regnos(ratings_file)
    encrypted_regnos = set(encrypted_regnos_info.keys())
    print(f"Found {len(encrypted_regnos)} unique encrypted registration numbers")
    
    print(f"Reading student data from {students_file}...")
    students_data = get_students_data(students_file)
    print(f"Found {len(students_data)} student records")
    
    # Create mapping of encrypted to original registration numbers
    matches = {}
    
    print("Mapping encrypted registration numbers to original values...")
    for student in students_data:
        regno = student['registerno']
        encrypted = encrypt_regno(regno)
        
        if encrypted in encrypted_regnos:
            matches[encrypted] = regno
            
    print(f"Successfully mapped {len(matches)} out of {len(encrypted_regnos)} registration numbers")
    
    # Create comprehensive results including student details
    final_results = []
    remaining_encrypted = set()
    
    for encrypted, (dept, sem) in encrypted_regnos_info.items():
        original_regno = matches.get(encrypted, "UNKNOWN")
        
        if original_regno == "UNKNOWN":
            remaining_encrypted.add(encrypted)
            final_results.append([ original_regno, dept, sem])
            continue
            
        # Find student details if available
        student_details = next((s for s in students_data if normalize_regno(s['registerno']) == normalize_regno(original_regno)), None)
        
        if student_details:
            # Use department and semester from ratings if available, otherwise from student data
            final_dept = dept if dept else student_details.get('department', '')
            final_sem = sem if sem else student_details.get('semester', '')
            final_results.append([
                 
                original_regno,
                final_dept,
                final_sem
            ])
        else:
            final_results.append([ original_regno, dept, sem])
            
    # Try another pass with remaining encrypted numbers
    for student in students_data:
        encrypted = encrypt_regno(student['registerno'])
        if encrypted in remaining_encrypted:
            final_results.append([
                student['registerno'],
                student.get('department', ''),
                student.get('semester', '')
            ])
            remaining_encrypted.remove(encrypted)
    
    # Write the decryption mapping to a CSV file
    with open(decrypted_file, 'w', newline='', encoding='utf-8') as outfile:
        writer = csv.writer(outfile)
        writer.writerow([ 'Original RegNo', 'Department', 'Semester'])
        writer.writerows(final_results)
    
    print(f"\nDecryption mapping written to {decrypted_file}")
    success_count = sum(1 for r in final_results if r[1] != "UNKNOWN")
    success_percentage = (success_count/len(final_results)*100) if final_results else 0
    print(f"Successfully decrypted: {success_count} of {len(final_results)} unique registration numbers ({success_percentage:.2f}%)")
    
    # Report any that couldn't be decrypted
    unknown_count = sum(1 for r in final_results if r[1] == "UNKNOWN")
    if unknown_count > 0:
        print(f"Failed to decrypt {unknown_count} registration numbers.")
        print("\nPossible reasons for unmatched registration numbers:")
        print("1. Some registration numbers in ratings.csv may not exist in students.csv")
        print("2. There might be formatting differences between the two files")
        
        # If there are a lot of unmatched numbers, offer to create a lookup file
        if unknown_count > 10:
            print("\nTo solve remaining unmatched numbers, you could:")
            print("1. Check for any missing students in the students.csv file")
            print("2. Run a broader search using one of the previous scripts")

if __name__ == "__main__":
    main()
