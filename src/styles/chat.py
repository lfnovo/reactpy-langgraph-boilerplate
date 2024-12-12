from reactpy import html
from .base import create_style_tag

chat_styles = """
    .chat-container {
        display: flex;
        flex-direction: column;
        height: 100%;
    }
    
    .messages-container {
        flex-grow: 1;
        overflow-y: auto;
        padding: 1rem;
        display: flex;
        flex-direction: column;
        gap: 1rem;
        min-height: 400px;
    }
    
    .chat-message {
        padding: 0.5rem 1rem;
        border-radius: 8px;
        max-width: 80%;
    }
    
    .ai-message {
        background-color: #e9ecef;
        align-self: flex-start;
    }
    
    .user-message {
        background-color: #007bff;
        color: white;
        align-self: flex-end;
    }
    
    .message-content {
        display: flex;
        flex-direction: column;
    }
    
    .timestamp {
        font-size: 0.8rem;
        color: #666;
    }
    
    .user-message .timestamp {
        color: #e9ecef;
    }
    
    .chat-form {
        display: flex;
        gap: 0.5rem;
        padding: 1rem;
        background: white;
        border-top: 1px solid #dee2e6;
    }
    
    .chat-form input {
        flex-grow: 1;
    }
"""

chat_style_tag = create_style_tag(chat_styles)
