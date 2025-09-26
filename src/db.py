import os
import sys
from supabase import create_client, Client
from dotenv import load_dotenv

load_dotenv()

url = os.getenv("SUPABASE_URL")
key = os.getenv("SUPABASE_KEY")

sb: Client = create_client(url, key)
if sb is None:
    print("❌ Failed to create Supabase client. Please check your credentials.")
    sys.exit(1)

# Insert clip
def insert_clip(clip_id, content):
    payload = {"clip_id": clip_id, "content": content}
    resp = sb.table("clips").insert(payload).execute()
    return resp.data

# Get clip by ID
def get_clip_by_id(clip_id):
    resp = sb.table("clips").select("*").eq("clip_id", clip_id).execute()
    return resp.data
