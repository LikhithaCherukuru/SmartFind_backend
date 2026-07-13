from supabase import Client, create_client
from app.core.config import settings

supabase: Client = create_client(
    settings.SUPABASE_URL,
    settings.SUPABASE_SECRET_KEY,
)

# Temporary alias for compatibility
supabase_admin = supabase


def get_supabase() -> Client:
    return supabase


def get_supabase_admin() -> Client:
    return supabase_admin