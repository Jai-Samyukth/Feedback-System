import logging
from .database import get_db
from utils import normalize_regno, encrypt_regno, is_encrypted

logger = logging.getLogger(__name__)

class Student:
    @staticmethod
    def add(registerno, department, semester):
        """Add a new student to the database."""
        client = get_db()
        try:
            result = client.table('students').insert({
                'registerno': registerno,
                'department': department,
                'semester': semester
            }).execute()
            return result.data[0]['id'] if result.data else None
        except Exception as e:
            logger.error(f"Error adding student: {e}")
            raise
    
    @staticmethod
    def bulk_add(students):
        """Add multiple students at once.
        students: list of tuples (registerno, department, semester)
        Returns: (added_count, duplicate_count, duplicates_list)
        """
        client = get_db()
        added = []
        duplicates = []
        
        for registerno, department, semester in students:
            try:
                # Check if student already exists
                existing = client.table('students')\
                    .select('registerno')\
                    .eq('registerno', registerno)\
                    .eq('department', department)\
                    .eq('semester', semester)\
                    .execute()
                
                if existing.data:
                    duplicates.append(registerno)
                else:
                    client.table('students').insert({
                        'registerno': registerno,
                        'department': department,
                        'semester': semester
                    }).execute()
                    added.append(registerno)
            except Exception as e:
                logger.error(f"Error adding student {registerno}: {e}")
                duplicates.append(registerno)
        
        return len(added), len(duplicates), duplicates
    
    @staticmethod
    def delete(registerno, department, semester):
        """Delete a student from the database."""
        client = get_db()
        try:
            result = client.table('students')\
                .delete()\
                .eq('registerno', registerno)\
                .eq('department', department)\
                .eq('semester', semester)\
                .execute()
            return len(result.data) > 0
        except Exception as e:
            logger.error(f"Error deleting student: {e}")
            return False
    
    @staticmethod
    def get_by_regno(registerno):
        """Get student info by registration number."""
        reg_num = normalize_regno(registerno)
        client = get_db()
        
        try:
            result = client.table('students')\
                .select('registerno, department, semester')\
                .eq('registerno', reg_num)\
                .execute()
            
            if result.data:
                row = result.data[0]
                return {
                    'registerno': row['registerno'],
                    'department': row['department'],
                    'semester': row['semester']
                }
            return None
        except Exception as e:
            logger.error(f"Error getting student by regno: {e}")
            return None
    
    @staticmethod
    def get_by_dept_sem(department, semester):
        """Get all students for a department and semester."""
        client = get_db()
        
        try:
            result = client.table('students')\
                .select('registerno, department, semester')\
                .eq('department', department)\
                .eq('semester', semester)\
                .order('registerno')\
                .execute()
            
            return [{'registerno': row['registerno'], 
                    'department': row['department'], 
                    'semester': row['semester']} 
                    for row in result.data]
        except Exception as e:
            logger.error(f"Error getting students by dept/sem: {e}")
            return []
    
    @staticmethod
    def get_all():
        """Get all students."""
        client = get_db()
        
        try:
            result = client.table('students')\
                .select('registerno, department, semester')\
                .order('department')\
                .order('semester')\
                .order('registerno')\
                .execute()
            
            return [{'registerno': row['registerno'], 
                    'department': row['department'], 
                    'semester': row['semester']} 
                    for row in result.data]
        except Exception as e:
            logger.error(f"Error getting all students: {e}")
            return []
    
    @staticmethod
    def exists(registerno, department=None, semester=None):
        """Check if a student exists."""
        reg_num = normalize_regno(registerno)
        client = get_db()
        
        try:
            query = client.table('students').select('id').eq('registerno', reg_num)
            
            if department and semester:
                query = query.eq('department', department).eq('semester', semester)
            
            result = query.execute()
            return len(result.data) > 0
        except Exception as e:
            logger.error(f"Error checking student existence: {e}")
            return False
    
    @staticmethod
    def count():
        """Get total number of students."""
        client = get_db()
        
        try:
            result = client.table('students').select('id', count='exact').execute()
            return result.count if result.count else 0
        except Exception as e:
            logger.error(f"Error counting students: {e}")
            return 0
