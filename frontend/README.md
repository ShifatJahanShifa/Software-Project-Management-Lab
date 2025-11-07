# Frontend Documentation

A minimalistic, Grok-inspired chat interface for the Chat Assistant backend API.

## 📋 Overview

The frontend is a single-page application built with vanilla JavaScript, HTML5, and CSS3. It provides a modern, responsive chat interface that communicates with the FastAPI backend.

## ✨ Features

- **Modern UI**: Clean, minimalistic design inspired by Grok
- **Dark Theme**: Beautiful dark color scheme with blue accents
- **Real-time Chat**: Instant message display with smooth animations
- **Loading States**: Animated loading indicators during API calls
- **Responsive Design**: Works on desktop, tablet, and mobile devices
- **Auto-resizing Input**: Textarea automatically adjusts height
- **Error Handling**: User-friendly error messages
- **Keyboard Support**: Enter to submit, Shift+Enter for new line

## 📁 File Structure

```
frontend/
├── index.html      # Main HTML structure and DOM elements
├── styles.css      # Complete styling with CSS variables
├── app.js          # Application logic and API integration
└── README.md       # This file
```

## 🚀 Setup

### Prerequisites

- A web server (Python, Node.js, or any HTTP server)
- Backend running on `http://localhost:8000`

### Running the Frontend

#### Option 1: Python HTTP Server (Recommended)

```bash
cd frontend
python3 -m http.server 3000
```

Then open `http://localhost:3000` in your browser.

#### Option 2: Node.js

```bash
cd frontend
npx serve
```

#### Option 3: Direct File

Simply open `index.html` in your browser (may have CORS limitations with API calls).

## ⚙️ Configuration

### API Endpoint

Configure the backend URL in `app.js`:

```javascript
const API_BASE_URL = 'http://localhost:8000';
```

Update this if your backend runs on a different URL or port.

### Theme Customization

Edit CSS variables in `styles.css`:

```css
:root {
    --bg-primary: #0a0a0a;        /* Main background */
    --bg-secondary: #141414;      /* Container background */
    --bg-tertiary: #1a1a1a;       /* Header/input background */
    --accent: #4a9eff;            /* Primary accent color */
    --accent-hover: #5ba8ff;      /* Accent hover state */
    --text-primary: #e5e5e5;      /* Main text color */
    --text-secondary: #a0a0a0;    /* Secondary text color */
    --border: #2a2a2a;            /* Border color */
}
```

## 🎨 UI Components

### Chat Container

- Fixed height container with scrollable message area
- Header with title and subtitle
- Message display area
- Input area at bottom

### Message Bubbles

- **User Messages**: Blue background, right-aligned
- **Assistant Messages**: Dark background, left-aligned
- Smooth fade-in animations
- Auto-scroll to latest message

### Input Field

- Auto-resizing textarea (max 200px)
- Send button with icon
- Disabled state during processing
- Focus management

### Loading Indicator

- Animated three-dot loader
- Appears while waiting for API response
- Automatically removed when response arrives

## 💻 Code Structure

### index.html

- Semantic HTML structure
- DOM element IDs for JavaScript access
- SVG icons for send button
- Responsive meta tags

### styles.css

- CSS custom properties for theming
- Responsive design with media queries
- Smooth animations and transitions
- Scrollbar styling
- Mobile-first approach

### app.js

#### Key Functions

- `addMessage(type, content)`: Add message to chat
- `addLoadingMessage()`: Show loading indicator
- `removeMessage(id)`: Remove message by ID
- `scrollToBottom()`: Auto-scroll to latest message
- `setInputDisabled(disabled)`: Enable/disable input
- `checkBackend()`: Verify backend connection

#### Event Handlers

- Form submission handler
- Textarea auto-resize handler
- Input validation

#### API Integration

- Fetch API for HTTP requests
- Error handling and user feedback
- Loading state management

## 🔧 Customization

### Changing Colors

Edit the CSS variables in `styles.css`:

```css
:root {
    --accent: #your-color;
}
```

### Modifying Layout

Update the HTML structure in `index.html` and corresponding styles in `styles.css`.

### Adding Features

1. Add HTML elements in `index.html`
2. Style them in `styles.css`
3. Add JavaScript logic in `app.js`

## 📱 Responsive Design

The frontend is fully responsive with breakpoints:

- **Desktop**: Full width, centered container (max 900px)
- **Tablet**: Adjusted padding and font sizes
- **Mobile**: Full viewport, optimized spacing

Media query breakpoint: `768px`

## 🐛 Troubleshooting

### CORS Errors

- Ensure backend CORS is configured
- Check API_BASE_URL matches backend URL
- Verify backend is running

### Styles Not Loading

- Use a web server (not file://)
- Check file paths are correct
- Clear browser cache

### API Not Responding

- Verify backend is running: `curl http://localhost:8000/`
- Check browser console for errors
- Verify API_BASE_URL in app.js

### Messages Not Appearing

- Check browser console for JavaScript errors
- Verify DOM elements exist
- Check API response format

## 🎯 Best Practices

1. **Error Handling**: Always handle API errors gracefully
2. **User Feedback**: Show loading states and error messages
3. **Accessibility**: Use semantic HTML and ARIA labels
4. **Performance**: Minimize DOM manipulation
5. **Code Organization**: Keep functions focused and reusable

## 🔍 Browser Compatibility

- Chrome/Edge: ✅ Full support
- Firefox: ✅ Full support
- Safari: ✅ Full support
- Mobile browsers: ✅ Responsive design works

## 📚 API Integration

The frontend communicates with the backend via REST API:

```javascript
// POST request to /generate
const response = await fetch(`${API_BASE_URL}/generate`, {
    method: 'POST',
    headers: {
        'Content-Type': 'application/json',
    },
    body: JSON.stringify({ question: question }),
});
```

## 🚀 Performance

- No build process required
- Vanilla JavaScript (no framework overhead)
- Minimal dependencies
- Fast load times
- Smooth animations

## 📝 Development Tips

1. Use browser DevTools for debugging
2. Check Network tab for API requests
3. Use Console for error messages
4. Test on multiple browsers
5. Test responsive design on different screen sizes

## 🔗 Related Documentation

- [Main README](../README.md) - Complete project documentation
- [Backend README](../backend/README.md) - Backend API documentation

