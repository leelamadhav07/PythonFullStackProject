import os, sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from logic import ClipBoardService

app = FastAPI(title="Online Clipboard API", version="2.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

service = ClipBoardService()

class ClipCreate(BaseModel):
    clip_id: str
    content: str

@app.post("/clips/")
def add_clip(clip: ClipCreate):
    try:
        result = service.create_clip(clip.clip_id, clip.content)
        return {"message": "✅ Clip added successfully", "clip": result}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.get("/clips/{clip_id}")
def get_clip(clip_id: str):
    result = service.fetch_clip(clip_id)
    if "error" in result:
        raise HTTPException(status_code=404, detail=result["error"])
    return {"clip": result}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("API.main:app", host="0.0.0.0", port=8000)
