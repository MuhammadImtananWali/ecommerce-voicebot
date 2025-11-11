import os
from supabase import create_client, Client

from dotenv import load_dotenv

load_dotenv(".env.local")

# Lazy-load Supabase client
_supabase_client = None


def get_supabase_client() -> Client:
    """Get or create Supabase client instance."""
    global _supabase_client
    if _supabase_client is None:
        supabase_url = os.getenv("SUPABASE_URL")
        supabase_key = os.getenv("SUPABASE_KEY")
        _supabase_client = create_client(supabase_url, supabase_key)
    return _supabase_client


def search_products(query: str):
    """Search products using Supabase full-text search."""
    query = query.lower()
    supabase = get_supabase_client()

    try:
        # Using Supabase's ilike for case-insensitive pattern matching
        response = (
            supabase.table("products")
            .select("*")
            .or_(
                f"name.ilike.%{query}%,"
                f"category.ilike.%{query}%,"
                f"brand.ilike.%{query}%,"
                f"description.ilike.%{query}%,"
                f"features.ilike.%{query}%"
            )
            .execute()
        )

        return response.data
    except Exception as e:
        print(f"Error searching products: {e}")
        return []
