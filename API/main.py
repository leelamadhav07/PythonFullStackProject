from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional
from logic import create_user, create_clip, fetch_clip

app = FastAPI(title="Online Clipboard API")

#Request Models
class UserCreate(BaseModel):
    username: str
    email: str

class ClipCreate(BaseModel):
    clip_id: str
    user_id: int
    content: str

#API Endpoints
@app.post("/users/")
def add_user(user: UserCreate):
    result = create_user(user.username, user.email)
    if "error" in result:
        raise HTTPException(status_code=400, detail=result["error"])
    return {"message": "User added successfully", "user": result}

@app.post("/clips/")
def add_clip(clip: ClipCreate):
    result = create_clip(clip.user_id, clip.content)
    # Override generated ID with user-chosen clip_id
    from db import insert_clip
    result = insert_clip(clip.clip_id, clip.user_id, clip.content)
    if "error" in result:
        raise HTTPException(status_code=400, detail=result["error"])
    return {"message": "Clip added successfully", "clip": result}

@app.get("/clips/{clip_id}")
def get_clip(clip_id: str):
    result = fetch_clip(clip_id)
    if "error" in result:
        raise HTTPException(status_code=404, detail=result["error"])
    return {"clip": result}
