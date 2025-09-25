# logic.py
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from db import *

class ClipBoardService:

    def __init__(self):
        print("✅ ClipBoardService initialized")

    def create_user(self, username: str, email: str):
        """Create a new user after validation."""
        if '@' not in email:
            raise ValueError("❌ Invalid email address")
        return insert_user(username, email)

    def create_clip(self, clip_id: str, user_id: int, content: str):
        """Create a new clip."""
        if not clip_id or not content:
            raise ValueError("❌ clip_id and content cannot be empty")
        return insert_clip(clip_id, user_id, content)

    def fetch_clip(self, clip_id: str):
        """Retrieve clip by clip_id."""
        data = get_clip_by_id(clip_id)
        if not data:
            return {"error": "❌ Clip not found"}
        return data
