# E-commerce Voicebot

AI-powered voice assistant for e-commerce product search using LiveKit and Supabase.

## Project Structure

```
.
├── src/
│   ├── agent.py              # Main agent logic
│   ├── tools.py              # Agent function tools
│   ├── prompt.py             # Agent prompts and instructions
│   └── services/
│       └── product_search.py # Product search service (Supabase)
├── scripts/
│   └── migrate_to_supabase.py # CSV to Supabase migration
├── database/
│   ├── supabase_schema.sql   # Database schema
│   └── products.csv          # Legacy product data
├── main.py                   # Application entry point
├── .env.local                # Environment variables
└── pyproject.toml            # Project dependencies
```

## Setup

1. **Install dependencies:**
   ```bash
   uv sync
   ```

2. **Configure Supabase:**
   - Create a project at [supabase.com](https://supabase.com)
   - Run the SQL in `database/supabase_schema.sql` in your Supabase SQL Editor
   - Add your credentials to `.env.local`:
     ```
     SUPABASE_URL=your_project_url
     SUPABASE_KEY=your_anon_key
     ```

3. **Migrate data:**
   ```bash
   python scripts/migrate_to_supabase.py
   ```

4. **Run the agent:**
   ```bash
   python main.py dev
   ```

## Features

- Voice-based product search
- Natural language understanding
- Real-time responses
- Supabase-powered database
- Multi-language support
