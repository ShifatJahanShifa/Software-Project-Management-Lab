// Configuration
const API_BASE_URL = 'http://localhost:8000'; // Update this if your backend runs on a different port

// DOM elements
const messagesContainer = document.getElementById('messages');
const chatForm = document.getElementById('chat-form');
const questionInput = document.getElementById('question-input');
const sendButton = document.getElementById('send-button');

// Auto-resize textarea
questionInput.addEventListener('input', function() {
    this.style.height = 'auto';
    this.style.height = Math.min(this.scrollHeight, 200) + 'px';
});

// Handle form submission
chatForm.addEventListener('submit', async (e) => {
    e.preventDefault();
    
    const question = questionInput.value.trim();
    if (!question) return;
    
    // Add user message
    addMessage('user', question);
    
    // Clear input
    questionInput.value = '';
    questionInput.style.height = 'auto';
    
    // Disable input while processing
    setInputDisabled(true);
    
    // Add loading message
    const loadingId = addLoadingMessage();
    
    try {
        // Call API
        const response = await fetch(`${API_BASE_URL}/generate`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ question: question }),
        });
        
        // Remove loading message
        removeMessage(loadingId);
        
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        
        const data = await response.json();
        
        // Add assistant response
        addMessage('assistant', data.answer);
        
    } catch (error) {
        // Remove loading message
        removeMessage(loadingId);
        
        // Show error message
        addMessage('assistant', 'Sorry, I encountered an error processing your request. Please make sure the backend is running and try again.');
        console.error('Error:', error);
    } finally {
        // Re-enable input
        setInputDisabled(false);
        questionInput.focus();
    }
});

// Add a message to the chat
function addMessage(type, content) {
    const messageDiv = document.createElement('div');
    messageDiv.className = `message ${type}`;
    
    const contentDiv = document.createElement('div');
    contentDiv.className = 'message-content';
    
    const paragraph = document.createElement('p');
    paragraph.textContent = content;
    
    contentDiv.appendChild(paragraph);
    messageDiv.appendChild(contentDiv);
    messagesContainer.appendChild(messageDiv);
    
    // Scroll to bottom
    scrollToBottom();
    
    return messageDiv;
}

// Add a loading message
function addLoadingMessage() {
    const messageDiv = document.createElement('div');
    messageDiv.className = 'message assistant loading';
    messageDiv.id = 'loading-message';
    
    const contentDiv = document.createElement('div');
    contentDiv.className = 'message-content';
    
    const loadingDots = document.createElement('div');
    loadingDots.className = 'loading-dots';
    
    for (let i = 0; i < 3; i++) {
        const dot = document.createElement('div');
        dot.className = 'loading-dot';
        loadingDots.appendChild(dot);
    }
    
    contentDiv.appendChild(loadingDots);
    messageDiv.appendChild(contentDiv);
    messagesContainer.appendChild(messageDiv);
    
    // Scroll to bottom
    scrollToBottom();
    
    return 'loading-message';
}

// Remove a message by ID
function removeMessage(id) {
    const message = document.getElementById(id);
    if (message) {
        message.remove();
    }
}

// Scroll to bottom of messages
function scrollToBottom() {
    messagesContainer.scrollTop = messagesContainer.scrollHeight;
}

// Enable/disable input
function setInputDisabled(disabled) {
    questionInput.disabled = disabled;
    sendButton.disabled = disabled;
}

// Check backend connection on load
async function checkBackend() {
    try {
        const response = await fetch(`${API_BASE_URL}/`);
        if (response.ok) {
            console.log('Backend is connected');
        }
    } catch (error) {
        console.warn('Backend connection check failed:', error);
    }
}

// Initialize
checkBackend();
questionInput.focus();

