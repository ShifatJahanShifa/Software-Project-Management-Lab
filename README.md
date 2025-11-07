# Chat Assistant Application

A modern, minimalistic chat application with a FastAPI backend and a frontend interface.

## Table of Contents

- [Architecture](#architecture)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Configuration](#configuration)
- [Running the Application](#running-the-application)
- [API Documentation](#api-documentation)
- [Troubleshooting](#troubleshooting)



### Key Technologies

- **Backend**: FastAPI (Python)
- **Frontend**: Vanilla JavaScript, HTML5, CSS3
- **AI Model**: Google Gemini 2.5 Pro
- **Server**: Uvicorn (ASGI server)

## Architecture

```
┌─────────────────┐
│   Frontend      │
│  (Port 3000)    │
│  HTML/CSS/JS    │
└────────┬────────┘
         │ HTTP Requests
         │ (CORS enabled)
         ▼
┌─────────────────┐
│   Backend       │
│  (Port 8000)    │
│   FastAPI       │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  LLM Service    │
│  Gemini API     │
└─────────────────┘
```

### Component Flow

1. User types a question in the frontend chat interface
2. Frontend sends POST request to `/generate` endpoint
3. Backend processes the question through the LLM service
4. Gemini API generates a response
5. Response is sent back to frontend and displayed in the chat

## Prerequisites

- Python 3.8+ (Python 3.13 recommended)
- pip (Python package manager)
- Google Gemini API Key ([Get one here](https://makersuite.google.com/app/apikey))

## Installation

### 1. Clone the Repository

```bash
git clone <repository-url>
cd Software-Project-Management-Lab
```

### 2. Backend Setup

```bash
cd backend
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 3. Configuration

Create a `.env` file in the `backend` directory:

```bash
cd backend
cp .env.example .env
```

Edit `.env` and add your Gemini API key:

```env
GEMINI_API_KEY=your_api_key_here
```

**Important**: Never commit your `.env` file to version control.

## Configuration

### Backend Configuration

The backend runs on `http://localhost:8000` by default. You can change this in the uvicorn command.

For production, update CORS configuration in `main.py`:

```python
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Specific origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
```

### Frontend Configuration

The frontend API URL is configured in `frontend/app.js`:

```javascript
const API_BASE_URL = 'http://localhost:8000';
```

Update this if your backend runs on a different URL or port.

## Running the Application

### Start Backend Server

```bash
cd backend
source venv/bin/activate  # On Windows: venv\Scripts\activate
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

The backend will be available at:
- API: `http://localhost:8000`
- API Docs: `http://localhost:8000/docs` (Swagger UI)
- Alternative Docs: `http://localhost:8000/redoc` (ReDoc)

### Start Frontend Server

```bash
cd frontend
python3 -m http.server 3000
```

The frontend will be available at: `http://localhost:3000`

### Verify Both Servers

```bash
curl http://localhost:8000/
curl http://localhost:3000/
```

## API Documentation

### Base URL

```
http://localhost:8000
```

### Endpoints

#### Health Check

**GET** `/`

Check if the backend is running.

**Response:**
```json
{
  "message": "Chatbot backend is running!"
}
```

#### Generate Answer

**POST** `/generate`

Generate an AI response to a user's question.

**Request Body:**
```json
{
  "question": "What is artificial intelligence?"
}
```

**Response:**
```json
{
  "answer": "Artificial intelligence (AI) is..."
}
```

**Example:**
```bash
curl -X POST http://localhost:8000/generate \
  -H "Content-Type: application/json" \
  -d '{"question": "Hello, how are you?"}'
```

**Error Responses:**

- 400 Bad Request: Invalid request body
- 500 Internal Server Error: API key issues, quota limits, or other errors

FastAPI provides automatic interactive documentation:
- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`



## Troubleshooting

### Backend Issues

#### ModuleNotFoundError: No module named 'google.generativeai'

```bash
cd backend
source venv/bin/activate
pip install -r requirements.txt
```

#### GEMINI_API_KEY not found

1. Ensure `.env` file exists in `backend/` directory
2. Check that `.env` contains: `GEMINI_API_KEY=your_key_here`
3. Restart the backend server

#### Cannot process your query

- Check error logs in console/terminal
- Verify API key is correct
- Check Google Cloud Console for quota limits

#### Port 8000 already in use

```bash
lsof -ti:8000
kill -9 <PID>
# Or use a different port
uvicorn main:app --reload --port 8001
```

### Frontend Issues

#### CORS errors

- Ensure backend CORS is configured correctly
- Check that backend is running
- Verify API_BASE_URL in `app.js` matches backend URL

#### Failed to fetch

- Verify backend is running: `curl http://localhost:8000/`
- Check browser console for detailed error
- Ensure no firewall blocking connections

#### Frontend not loading styles

- Use a web server (not file:// protocol)
- Check file paths in HTML
- Clear browser cache
