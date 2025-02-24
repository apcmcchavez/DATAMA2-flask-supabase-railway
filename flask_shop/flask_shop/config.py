import os
from supabase import create_client
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Supabase credentials
SUPABASE_URL = os.getenv("SUPABASE_URL", "https://fylozuroogwzgyggvvlo.supabase.co")
SUPABASE_KEY = os.getenv("SUPABASE_KEY", "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImZ5bG96dXJvb2d3emd5Z2d2dmxvIiwicm9sZSI6ImFub24iLCJpYXQiOjE3MzgwMjcwMzUsImV4cCI6MjA1MzYwMzAzNX0.jKDjOiTAfGTaFgu-JHatUg1kzUbO4yaybupGI4JkW7c")  # Use environment variables in production

# Initialize Supabase client
supabase = create_client(SUPABASE_URL, SUPABASE_KEY)
