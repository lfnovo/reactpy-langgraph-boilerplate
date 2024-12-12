from reactpy import use_state

def use_chat():
    """
    Custom hook to manage chat state and actions
    Returns:
        messages: list of message objects
        new_message: current message being typed
        set_new_message: function to update new message
        send_message: function to send a new message
    """
    messages, set_messages = use_state([
        {"id": 1, "sender": "AI", "text": "Hello! How can I help you today?", "timestamp": "10:00"},
        {"id": 2, "sender": "User", "text": "I need help organizing my tasks", "timestamp": "10:01"},
        {"id": 3, "sender": "AI", "text": "I can help you with that! What kind of tasks do you need to organize?", "timestamp": "10:02"},
    ])
    new_message, set_new_message = use_state("")
    
    def send_message(event=None):
        if event:
            event.preventDefault()
        if new_message.strip():
            # In a real app, this would send to an API
            new_msg = {
                "id": len(messages) + 1,
                "sender": "User",
                "text": new_message,
                "timestamp": "10:03"  # In real app, use actual timestamp
            }
            set_messages(messages + [new_msg])
            set_new_message("")
    
    return messages, new_message, set_new_message, send_message
