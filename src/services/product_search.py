import os
from supabase import create_client, Client

# Initialize Supabase client
supabase_url = os.getenv("SUPABASE_URL")
supabase_key = os.getenv("SUPABASE_KEY")
supabase: Client = create_client(supabase_url, supabase_key)

def search_products(query: str):
    """Search products using Supabase full-text search."""
    query = query.lower()
    
    try:
        # Using Supabase's ilike for case-insensitive pattern matching
        response = supabase.table("products").select("*").or_(
            f"name.ilike.%{query}%,"
            f"category.ilike.%{query}%,"
            f"brand.ilike.%{query}%,"
            f"description.ilike.%{query}%,"
            f"features.ilike.%{query}%"
        ).execute()
        
        return response.data
    except Exception as e:
        print(f"Error searching products: {e}")
        return []
