# Backend Documentation

FastAPI backend for the Chat Assistant application.

## 📋 Overview

The backend is built with FastAPI and integrates with Google's Gemini AI to provide intelligent responses to user queries.

## 🏗️ Architecture

```
FastAPI Application
    ├── CORS Middleware
    ├── API Routes
    │   ├── GET / (Health Check)
    │   └── POST /generate (Generate Answer)
    ├── Models (Pydantic)
    │   ├── Request
    │   └── Response
    └── Services
        └── LLM Service (Gemini Integration)
```

## 📁 File Structure

```
backend/
├── main.py              # FastAPI app, routes, and CORS configuration
├── models.py            # Pydantic models for request/response validation
├── llm_service.py       # Google Gemini API integration
├── prompts.py           # Prompt engineering and template
├── requirements.txt     # Python dependencies
├── .env                 # Environment variables (not in git)
├── .env.example         # Example environment file
└── venv/                # Virtual environment
```

## 🔧 Setup

### 1. Create Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure Environment

```bash
cp .env.example .env
# Edit .env and add your GEMINI_API_KEY
```

### 4. Run Server

```bash
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

## 📚 API Endpoints

### GET `/`

Health check endpoint.

**Response:**
```json
{
  "message": "Chatbot backend is running!"
}
```

### POST `/generate`

Generate an AI response.

**Request:**
```json
{
  "question": "Your question here"
}
```

**Response:**
```json
{
  "answer": "AI generated response"
}
```

**Error Response:**
```json
{
  "answer": "Error: [detailed error message]"
}
```

## 🔑 Environment Variables

| Variable | Description | Required |
|----------|-------------|----------|
| `GEMINI_API_KEY` | Google Gemini API key | Yes |

## 📦 Dependencies

- **fastapi**: Web framework
- **uvicorn**: ASGI server
- **google-generativeai**: Gemini AI SDK
- **python-dotenv**: Environment variable management
- **pydantic**: Data validation
- **pydantic-settings**: Settings management
- **black**: Code formatter
- **isort**: Import sorter

## 🛠️ Development

### Code Formatting

```bash
black .
isort .
```

### Testing Endpoints

```bash
# Health check
curl http://localhost:8000/

# Generate answer
curl -X POST http://localhost:8000/generate \
  -H "Content-Type: application/json" \
  -d '{"question": "Hello"}'
```

### Interactive API Docs

- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

## 🐛 Error Handling

The backend includes comprehensive error handling:

1. **API Key Validation**: Checks if API key is configured
2. **Detailed Error Messages**: Returns specific error information
3. **Logging**: Logs errors for debugging
4. **Graceful Degradation**: Handles errors without crashing

### Error Types

- **API Key Errors**: Missing or invalid API key
- **Quota Errors**: API usage limits exceeded
- **Network Errors**: Connection issues
- **Model Errors**: Model unavailable or errors

## 🔒 Security

### CORS Configuration

Currently allows all origins. For production:

```python
app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://yourdomain.com"],
    allow_credentials=True,
    allow_methods=["GET", "POST"],
    allow_headers=["*"],
)
```

### API Key Security

- Never commit `.env` file
- Use environment variables in production
- Rotate keys regularly

## 📊 Logging

Logs are output to console with INFO level. Includes:
- API key loading status
- Error messages with details
- Request processing information

## 🚀 Production Deployment

### Recommended Setup

1. Use a production ASGI server (Gunicorn with Uvicorn workers)
2. Set up reverse proxy (Nginx)
3. Use environment variables for configuration
4. Enable HTTPS
5. Configure proper CORS origins
6. Set up monitoring and logging

### Example with Gunicorn

```bash
pip install gunicorn
gunicorn main:app -w 4 -k uvicorn.workers.UvicornWorker --bind 0.0.0.0:8000
```

## 📝 Code Structure

### main.py

- FastAPI application initialization
- CORS middleware configuration
- API route definitions
- Request/response handling

### models.py

- Pydantic models for validation
- Request model: `question: str`
- Response model: `answer: str`

### llm_service.py

- Google Gemini API configuration
- API key management
- Response generation
- Error handling and logging

### prompts.py

- Prompt template construction
- System message configuration
- Question formatting

## 🔍 Troubleshooting

See main [README.md](../README.md) for detailed troubleshooting guide.

Common issues:
- Module not found: Install dependencies
- API key errors: Check `.env` file
- Port conflicts: Change port or kill existing process
- CORS errors: Check CORS configuration

