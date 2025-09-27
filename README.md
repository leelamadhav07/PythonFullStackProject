### Online Clip Board

## Description:
The Online Clipboard Sharing Tool is a full-stack web application that allows users to paste text content, generate a unique ID (e.g., abc123), and share it via a URL (e.g., http://your-app.com/clip/abc123). Users can retrieve the content by entering the ID or visiting the URL. Clips expire after 24 hours for privacy, making it a secure and temporary solution for sharing text across devices.This project demonstrates full-stack development skills, including backend API design, database management with Supabase, and a responsive frontend. It’s ideal for showcasing proficiency in modern web technologies and secure data handling.

## Features:
-**Paste Content**: Users can paste text into a form and receive a unique ID and shareable URL.

-**Retrieve Content**: Users can enter the unique ID or visit the URL to view the content.

-**Expiration**: Clips automatically expire after 24 hours to ensure privacy.

-**Responsive UI**: Clean, mobile-friendly interface styled with CSS.

## Project Structure
```
ONLINECLIPBOARD/
    |
    |---src/            #Core Application Logic
    |   |---logic.py    #Business logic and task
    |   |---db.py       #Database Operations
    |
    |---api/            #Backend API
    |    |---main.py    #FASTAPI
    |
    |---frontend/       #Frontend Application
    |   |---app.py      #Streamlit web interface
    |
    |---requirements.txt#Python Dependencies
    |
    |---README.md       #Project Documentation
    |
    |---.env            #Python Variables
```
##Quick Start


### Prerequisites

- Python 3.8 or higher
- A Supabase Account
- Git(Push,cloning)

### 1. Clone or Download the Project

# Option 1: Clone with Git
git Clone <repository-url>

# Option 2: Download and extract the ZIP file

### 2. Install Dependencies

# Install all required python packages
pip install -r requirements.txt

### 3. Set Up Supabase Database

1.Create a Supabase Project:

2.Create the Table:

```
CREATE TABLE clips (
    clip_id SERIAL PRIMARY KEY,           -- Auto ID (internal use)
    unique_id VARCHAR(20) UNIQUE NOT NULL, -- Public ID (for URL sharing)
    content TEXT NOT NULL,                -- The pasted text
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- When created
    expires_at TIMESTAMP NOT NULL         -- When it should expire
);


```

3. **Get you credentials:

### 4. Configure Environment variables

1. Create a '.env' file in the project root

2. Add you supabase credentials to '.env' :
SUPABASE_URL=your_poject_url_here
SUPABASE_KEY=your_anon_key_here

### 5. Run the Application

## Streamlit Frontend
Streamlit run frontend/app.py

The app will open in your browser ar `http://localhost:8080`

## FastAPI Backend

cd api
python main.py

The API will be available at `http://localhost:8080`

## How to Use the application:


### Technical Details

### Technologies Used

- **Frontend**: Streamlit (Python Web Framework)
- **Backend**: FastAPI (Python REST API framework)
- **Database**: Supabase (PostgreSQL-based backend-as-a-service)
- **Language**: Python 3.8+

### Key Components

1. **`src/db.py`**: Databse Operations
    - Handles all CRUD operations with supabase

2. **`src/logic.py`**: Business logic 
    -Validation and processing

## TroubleShooting


## Common Problems
1. **Module Not Found Error**

## Future Enhancements

1. ## Support for Multiple Content Types:

Extend the clipboard to allow not just text, but also images, videos, and other file types.

2. ## Customizable Expiration Time:

Allow users to set their preferred expiration time for each clip instead of a fixed duration.

3. ## App Versioning and Updates:

Introduce a versioned app so that users can access the latest features while maintaining backward compatibility.

4. ## Enhanced User Experience:

Improve UI/UX for better responsiveness and accessibility.

## Support

If you encounter any issues or have questions:

Contact Me : 
## Mobile No: +91 7993857908
## Email : srinivasraosunkara846@gmail.com
