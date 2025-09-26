from db import insert_clip, get_clip_by_id

class ClipBoardService:
    def __init__(self):
        print("✅ ClipBoardService initialized")

    def create_clip(self, clip_id: str, content: str):
        if not clip_id or not content:
            raise ValueError("❌ clip_id and content cannot be empty")
        return insert_clip(clip_id, content)

    def fetch_clip(self, clip_id: str):
        data = get_clip_by_id(clip_id)
        if not data:
            return {"error": "❌ Clip not found"}
        return data
