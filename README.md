# MoodMix 🎵

A real-time collaborative playlist application. Create a room, share the link, and build a playlist with your friends instantly.

## Features

- **Real-time Updates**: See songs added by others immediately without refreshing.
- **Room System**: Create private rooms with unique URLs.
- **Simple Interface**: Easy-to-use form to add songs.

## Tech Stack

- **Backend**: FastAPI (Python)
- **Frontend**: Jinja2 Templates, HTML/CSS
- **Real-Time**: Socket.IO (for Phase 2)
- **Deployment**: Render (Web Service)

## Installation & Local Run

1. **Clone the repo**
   ```bash
   git clone https://github.com/your-username/moodmix.git
   cd moodmix

## Project Structure
   moodmix/
├── main.py          # FastAPI application and routes
├── requirements.txt # Python dependencies
├── render.yaml      # Deployment config for Render
└── templates/       # HTML templates
    ├── index.html   # Room page
    └── home.html    # Homepage