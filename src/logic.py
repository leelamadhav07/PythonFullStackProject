from db import insert_user, insert_clip, get_clip_by_id

#create a new User
def create_user(username, email):
    if '@' not in email:
        raise ValueError("Invalid email address")
    return insert_user(username, email)

#Create a new Clip
def create_clip(clip_id, user_id, content):
    return insert_clip(clip_id, user_id, content)

#Retrieve Clip by Clip ID
def fetch_clip(clip_id):
    data=get_clip_by_id(clip_id)
    if not data:
        return {"error": "Clip not found"}
    return data


