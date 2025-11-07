"""
Migration script to upload products from CSV to Supabase.
Run this once after setting up your Supabase table.
"""
import os
import pandas as pd
from dotenv import load_dotenv
from supabase import create_client

load_dotenv(".env.local")

def migrate_products():
    # Initialize Supabase client
    supabase_url = os.getenv("SUPABASE_URL")
    supabase_key = os.getenv("SUPABASE_KEY")
    supabase = create_client(supabase_url, supabase_key)
    
    # Read CSV
    df = pd.read_csv("database/products.csv")
    
    # Convert to list of dicts
    products = df.to_dict(orient="records")
    
    # Upload to Supabase
    try:
        response = supabase.table("products").insert(products).execute()
        print(f"✅ Successfully migrated {len(products)} products to Supabase!")
        return response
    except Exception as e:
        print(f"❌ Error migrating products: {e}")
        return None

if __name__ == "__main__":
    migrate_products()
