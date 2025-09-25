import os
import sys
from supabase import create_client, Client  # pip install supabase
from dotenv import load_dotenv

load_dotenv()

# Load Supabase credentials
url = os.getenv("SUPABASE_URL")
key = os.getenv("SUPABASE_KEY")

sb: Client = create_client(url, key)
if sb is None:
    print("Failed to create Supabase client. Please check your credentials.")
    sys.exit(1)


# ---------------- Database Functions ---------------- #

# Insert user
def insert_user(username, email):
    payload = {"username": username, "email": email}
    resp = sb.table("users").insert(payload).execute()
    return resp.data

# Insert clip
def insert_clip(clip_id, user_id, content):
    payload = {"clip_id": clip_id, "user_id": int(user_id), "content": content}
    resp = sb.table("clips").insert(payload).execute()
    return resp.data

#Get Clip Details By Clip ID
def get_clip_by_id(clip_id):
    resp= sb.table("clips").select("*").eq("clip_id", clip_id).execute()
    return resp.data

# ---------------- Main Program ---------------- #

if __name__ == "__main__":
    choice = input("Do you want to add (1) User or (2) Clip or (3) get Clip data by Clip id ? Enter 1 or 2 or 3: ")

    if choice == "1":
        username = input("Enter username: ")
        email = input("Enter email: ")
        added = insert_user(username, email)
        print("✅ Added user:", added)

    elif choice == "2":
        clip_id = input("Enter clip_id: ")       # e.g. "CLIP123A"
        user_id = input("Enter user_id: ")       # must exist in users table
        content = input("Enter content: ")
        added = insert_clip(clip_id, user_id, content)
        print("✅ Added clip:", added)
    
    elif choice == "3":
        clip_id = input("Enter clip_id to fetch: ")       # e.g. "CLIP123A"
        clip_data = get_clip_by_id(clip_id)
        print("✅ Clip data:", clip_data)

    else:
        print("Invalid choice. Exiting...")
