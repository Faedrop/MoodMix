# code for Mixmood application.

from fastapi import FastAPI , Request 
from pydantic import BaseModel
import uuid
from typing import Dict, List
from fastapi.responses import HTMLResponse , RedirectResponse
from fastapi.templating import Jinja2Templates
from fastapi import Form

# app instance
app = FastAPI()


templates = Jinja2Templates(directory="templates")



# Defining data models
class Song(BaseModel):
    title: str
    artist: str

class Room(BaseModel):
    id: str
    playlist: List[Song] = []

# In-memory "database" a dictionary to store all rooms
rooms: Dict[str, Room] = {}

@app.get("/room/{room_id}/view")
def view_room(request: Request, room_id: str):
    if room_id not in rooms:
        from fastapi import HTTPException
        raise HTTPException(status_code=404, detail="Room not found")
    
   # Return the HTML template with room data
    return templates.TemplateResponse(
        "index.html", 
        {"request": request, "room": rooms[room_id]}
    ) 

# Create a new room
@app.post("/room", response_model=Room)
def create_room():
    room_id = uuid.uuid4().hex # unique room ID using UUID
    new_room = Room(id=room_id)
    rooms[room_id] = new_room
    return RedirectResponse(url=f"/room/{room_id}/view", status_code=303)



@app.get("/")
def home(request: Request):
    return templates.TemplateResponse("home.html", {"request": request})
# Get room info
@app.get("/room/{room_id}", response_model=Room)
def get_room(room_id: str):
    if room_id not in rooms:
        from fastapi import HTTPException
        raise HTTPException(status_code=404, detail="Room not found")
    return rooms[room_id]

# Add a song to a room's playlist
@app.post("/room/{room_id}/song", response_model=Room)
def add_song(
    
    room_id: str, 
    title: str = Form(...),  # Get title from form data
    artist: str = Form(...)  # Get artist from form data
):
    if room_id not in rooms:
        from fastapi import HTTPException
        raise HTTPException(status_code=404, detail="Room not found")
    song = Song(title=title, artist=artist)
    rooms[room_id].playlist.append(song)
    return RedirectResponse(url=f"/room/{room_id}/view", status_code=303)


