import os
import logging
from supabase import Client
from dotenv import load_dotenv
from app.models.supabase_db import get_supabase_client, init_db as init_supabase_db

load_dotenv()

logger = logging.getLogger(__name__)

def get_db() -> Client:
    """Get Supabase client instance."""
    return get_supabase_client()

def get_db_path():
    """Legacy function - not used with Supabase."""
    logger.warning("get_db_path() is deprecated when using Supabase")
    return None

def init_db():
    """Initialize the Supabase database connection."""
    init_supabase_db()
    logger.info("Supabase database initialized")
