import os
import logging
from supabase import create_client, Client
from dotenv import load_dotenv

load_dotenv()

logger = logging.getLogger(__name__)

_supabase_client: Client = None

def get_supabase_client() -> Client:
    """Get or create the Supabase client instance."""
    global _supabase_client
    
    if _supabase_client is None:
        supabase_url = os.getenv("SUPABASE_URL")
        supabase_key = os.getenv("SUPABASE_KEY")
        
        if not supabase_url or not supabase_key:
            raise ValueError(
                "SUPABASE_URL and SUPABASE_KEY must be set in environment variables or .env file"
            )
        
        _supabase_client = create_client(supabase_url, supabase_key)
        logger.info("Supabase client initialized successfully")
    
    return _supabase_client

def init_db():
    """
    Initialize the database schema in Supabase.
    
    NOTE: You need to run these SQL commands in your Supabase SQL editor:
    
    -- Students table
    CREATE TABLE IF NOT EXISTS students (
        id BIGSERIAL PRIMARY KEY,
        registerno TEXT NOT NULL,
        department TEXT NOT NULL,
        semester TEXT NOT NULL,
        created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
        UNIQUE(registerno, department, semester)
    );
    
    CREATE INDEX IF NOT EXISTS idx_students_regno ON students(registerno);
    CREATE INDEX IF NOT EXISTS idx_students_dept_sem ON students(department, semester);
    
    -- Departments table
    CREATE TABLE IF NOT EXISTS departments (
        id BIGSERIAL PRIMARY KEY,
        name TEXT NOT NULL UNIQUE,
        created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
    );
    
    -- Semesters table
    CREATE TABLE IF NOT EXISTS semesters (
        id BIGSERIAL PRIMARY KEY,
        name TEXT NOT NULL UNIQUE,
        created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
    );
    
    -- Staff table
    CREATE TABLE IF NOT EXISTS staff (
        id BIGSERIAL PRIMARY KEY,
        name TEXT NOT NULL UNIQUE,
        created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
    );
    
    -- Subjects table
    CREATE TABLE IF NOT EXISTS subjects (
        id BIGSERIAL PRIMARY KEY,
        name TEXT NOT NULL UNIQUE,
        created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
    );
    
    -- Admin mappings table
    CREATE TABLE IF NOT EXISTS admin_mappings (
        id BIGSERIAL PRIMARY KEY,
        department TEXT NOT NULL,
        semester TEXT NOT NULL,
        staff TEXT NOT NULL,
        subject TEXT NOT NULL,
        created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
        UNIQUE(department, semester, staff, subject)
    );
    
    -- Ratings table
    CREATE TABLE IF NOT EXISTS ratings (
        id BIGSERIAL PRIMARY KEY,
        registerno TEXT NOT NULL,
        department TEXT NOT NULL,
        semester TEXT NOT NULL,
        staff TEXT NOT NULL,
        subject TEXT NOT NULL,
        q1 DOUBLE PRECISION NOT NULL,
        q2 DOUBLE PRECISION NOT NULL,
        q3 DOUBLE PRECISION NOT NULL,
        q4 DOUBLE PRECISION NOT NULL,
        q5 DOUBLE PRECISION NOT NULL,
        q6 DOUBLE PRECISION NOT NULL,
        q7 DOUBLE PRECISION NOT NULL,
        q8 DOUBLE PRECISION NOT NULL,
        q9 DOUBLE PRECISION NOT NULL,
        q10 DOUBLE PRECISION NOT NULL,
        average DOUBLE PRECISION NOT NULL,
        created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
    );
    
    CREATE INDEX IF NOT EXISTS idx_ratings_regno ON ratings(registerno);
    CREATE INDEX IF NOT EXISTS idx_ratings_dept_sem_staff_subj ON ratings(department, semester, staff, subject);
    
    -- Submitted feedback tracking table
    CREATE TABLE IF NOT EXISTS submitted_feedback (
        id BIGSERIAL PRIMARY KEY,
        registerno TEXT NOT NULL UNIQUE,
        submitted_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
    );
    
    -- Enable Row Level Security (RLS) on all tables
    ALTER TABLE students ENABLE ROW LEVEL SECURITY;
    ALTER TABLE departments ENABLE ROW LEVEL SECURITY;
    ALTER TABLE semesters ENABLE ROW LEVEL SECURITY;
    ALTER TABLE staff ENABLE ROW LEVEL SECURITY;
    ALTER TABLE subjects ENABLE ROW LEVEL SECURITY;
    ALTER TABLE admin_mappings ENABLE ROW LEVEL SECURITY;
    ALTER TABLE ratings ENABLE ROW LEVEL SECURITY;
    ALTER TABLE submitted_feedback ENABLE ROW LEVEL SECURITY;
    
    -- Create policies for service role (full access)
    CREATE POLICY "Enable all access for service role" ON students FOR ALL USING (true);
    CREATE POLICY "Enable all access for service role" ON departments FOR ALL USING (true);
    CREATE POLICY "Enable all access for service role" ON semesters FOR ALL USING (true);
    CREATE POLICY "Enable all access for service role" ON staff FOR ALL USING (true);
    CREATE POLICY "Enable all access for service role" ON subjects FOR ALL USING (true);
    CREATE POLICY "Enable all access for service role" ON admin_mappings FOR ALL USING (true);
    CREATE POLICY "Enable all access for service role" ON ratings FOR ALL USING (true);
    CREATE POLICY "Enable all access for service role" ON submitted_feedback FOR ALL USING (true);
    """
    try:
        client = get_supabase_client()
        logger.info("Supabase database connection verified")
        logger.warning("Make sure to run the SQL schema creation script in your Supabase SQL editor")
    except Exception as e:
        logger.error(f"Database initialization error: {e}")
        raise
