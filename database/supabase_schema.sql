-- Create products table in Supabase
-- Run this in your Supabase SQL Editor

CREATE TABLE products (
    id BIGINT PRIMARY KEY,
    name TEXT NOT NULL,
    category TEXT NOT NULL,
    price NUMERIC(10, 2) NOT NULL,
    brand TEXT NOT NULL,
    description TEXT,
    color TEXT,
    features TEXT,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

-- Create indexes for better search performance
CREATE INDEX idx_products_name ON products USING gin(to_tsvector('english', name));
CREATE INDEX idx_products_category ON products(category);
CREATE INDEX idx_products_brand ON products(brand);
CREATE INDEX idx_products_description ON products USING gin(to_tsvector('english', description));

-- Enable Row Level Security (optional, but recommended)
ALTER TABLE products ENABLE ROW LEVEL SECURITY;

-- Create a policy to allow public read access
CREATE POLICY "Allow public read access" ON products
    FOR SELECT
    USING (true);
