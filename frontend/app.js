
const API_BASE_URL = 'http://localhost:8000'; 

const messagesContainer = document.getElementById('messages');
const chatForm = document.getElementById('chat-form');
const questionInput = document.getElementById('question-input');
const sendButton = document.getElementById('send-button');


questionInput.addEventListener('input', function() {
    this.style.height = 'auto';
    this.style.height = Math.min(this.scrollHeight, 200) + 'px';
});


chatForm.addEventListener('submit', async (e) => {
    e.preventDefault();
    
    const question = questionInput.value.trim();
    if (!question) return;
    
  
    addMessage('user', question);
    
 
    questionInput.value = '';
    questionInput.style.height = 'auto';
    

    setInputDisabled(true);
    

    const loadingId = addLoadingMessage();
    
    try {
    
        const response = await fetch(`${API_BASE_URL}/generate`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ question: question }),
        });
        
        
        removeMessage(loadingId);
        
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        
        const data = await response.json();
        
  
        addMessage('assistant', data.answer);
        
    } catch (error) {
        
        removeMessage(loadingId);
        
  
        addMessage('assistant', 'Sorry, I encountered an error processing your request. Please make sure the backend is running and try again.');
        console.error('Error:', error);
    } finally {
        
        setInputDisabled(false);
        questionInput.focus();
    }
});


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

