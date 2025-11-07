# Quick Start Guide

Get the Chat Assistant application up and running in 5 minutes!

##  Quick Setup

### Step 1: Backend Setup

```bash
# Navigate to backend
cd backend

# Create and activate virtual environment
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Create .env file
cp .env.example .env
# Edit .env and add your GEMINI_API_KEY

# Start backend server
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

Backend will be running at: `http://localhost:8000`

### Step 2: Frontend Setup

Open a new terminal:

```bash
# Navigate to frontend
cd frontend

# Start web server
python3 -m http.server 3000
```

Frontend will be available at: `http://localhost:3000`

### Step 3: Test the Application

1. Open `http://localhost:3000` in your browser
2. Type a question in the chat
3. Press Enter or click Send
4. Wait for the AI response!

##  Verify Installation

### Check Backend

```bash
curl http://localhost:8000/
```

Should return: `{"message":"Chatbot backend is running!"}`

### Check Frontend

Open `http://localhost:3000` in your browser - you should see the chat interface.

##  Get API Key

1. Visit [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Sign in with your Google account
3. Create a new API key
4. Copy the key to your `.env` file

##  Common Issues

### Backend won't start
- Check if port 8000 is available: `lsof -ti:8000`
- Verify Python version: `python3 --version` (need 3.8+)
- Check virtual environment is activated

### Frontend can't connect
- Verify backend is running
- Check API_BASE_URL in `frontend/app.js`
- Check browser console for errors

### API errors
- Verify `.env` file exists and has GEMINI_API_KEY
- Check API key is valid
- Restart backend after changing .env

##  Next Steps

- Read the full [README.md](README.md) for detailed documentation
- Check [Backend README](backend/README.md) for API details
- See [Frontend README](frontend/README.md) for UI customization


chat assistant is now running. Start asking questions!

