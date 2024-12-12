from reactpy import component, html, use_state
from reactpy.backend.fastapi import configure
from fastapi import FastAPI
import pandas as pd

url = "https://cdn.jsdelivr.net/npm/@picocss/pico@2/css/pico.min.css"
pico_css = html.link({"rel": "stylesheet", "href": url})

# Mock data
mock_data = {
    'Month': ['Jan', 'Feb', 'Mar', 'Apr', 'May'],
    'Tasks': [23, 34, 45, 56, 43]
}

mock_categories = [
    {"id": 1, "name": "Work", "color": "#FF6B6B", "count": 12},
    {"id": 2, "name": "Personal", "color": "#4ECDC4", "count": 8},
    {"id": 3, "name": "Health", "color": "#45B7D1", "count": 15},
    {"id": 4, "name": "Learning", "color": "#96CEB4", "count": 6},
    {"id": 5, "name": "Projects", "color": "#FFEEAD", "count": 10},
    {"id": 6, "name": "Family", "color": "#D4A5A5", "count": 9},
]

mock_messages = [
    {"id": 1, "sender": "AI", "text": "Hello! How can I help you today?", "timestamp": "10:00"},
    {"id": 2, "sender": "User", "text": "I need help organizing my tasks", "timestamp": "10:01"},
    {"id": 3, "sender": "AI", "text": "I can help you with that! What kind of tasks do you need to organize?", "timestamp": "10:02"},
]

@component
def Statistics():
    # Calculate percentage for each value
    max_value = max(mock_data['Tasks'])
    percentages = [int((value / max_value) * 100) for value in mock_data['Tasks']]
    
    return html.div(
        {"class": "statistics-container"},
        html.h2("Statistics"),
        html.div(
            {"class": "chart-container"},
            [
                html.div(
                    {"class": "chart-column"},
                    html.div(
                        {"class": "chart-bar", "style": {"height": f"{percentage}%"}},
                    ),
                    html.div({"class": "chart-label"}, 
                        html.div(str(value)),
                        html.div(month)
                    )
                ) for month, value, percentage in zip(mock_data['Month'], mock_data['Tasks'], percentages)
            ]
        )
    )

@component
def CategoryCard(category):
    return html.div(
        {
            "class": "category-card",
            "style": {
                "border-left": f"4px solid {category['color']}"
            }
        },
        html.h3(category["name"]),
        html.p(f"{category['count']} tasks"),
    )

@component
def CategoryList():
    return html.div(
        {"class": "category-list"},
        html.h2("Categories"),
        html.div(
            {"class": "category-grid"},
            [CategoryCard(category) for category in mock_categories]
        )
    )

@component
def ChatMessage(message):
    return html.div(
        {
            "class": f"chat-message {message['sender'].lower()}-message"
        },
        html.div(
            {"class": "message-content"},
            html.strong(message["sender"]),
            html.span({"class": "timestamp"}, message["timestamp"]),
            html.p(message["text"]),
        )
    )

@component
def Chat():
    message, set_message = use_state("")
    messages = mock_messages

    def handle_submit(event):
        event.preventDefault()
        if message.strip():
            # In a real app, we would send this to an API
            set_message("")

    return html.div(
        {"class": "chat-container"},
        html.h2("Chat"),
        html.div(
            {"class": "messages-container"},
            [ChatMessage(msg) for msg in messages]
        ),
        html.form(
            {
                "class": "chat-form",
                "on_submit": handle_submit
            },
            html.input({
                "type": "text",
                "value": message,
                "on_change": lambda e: set_message(e["target"]["value"]),
                "placeholder": "Type your message...",
            }),
            html.button({"type": "submit"}, "Send"),
        )
    )

@component
def HabitCanvas():
    return html.div({"class": "container"},
        pico_css,
        html.style("""
            .grid-container {
                display: grid;
                grid-template-columns: 2fr 1fr;
                gap: 2rem;
                padding: 1rem;
            }
            .left-column {
                display: flex;
                flex-direction: column;
                gap: 2rem;
            }
            .right-column {
                background-color: #f8f9fa;
                border-radius: 8px;
                padding: 1rem;
            }
            .statistics-container {
                background: white;
                padding: 1rem;
                border-radius: 8px;
                box-shadow: 0 2px 4px rgba(0,0,0,0.1);
            }
            .chart-container {
                display: flex;
                justify-content: space-around;
                align-items: flex-end;
                height: 300px;
                padding: 20px;
                background: white;
                border-radius: 8px;
            }
            .chart-column {
                display: flex;
                flex-direction: column;
                align-items: center;
                width: 60px;
            }
            .chart-bar {
                width: 40px;
                background: #007bff;
                border-radius: 4px 4px 0 0;
                transition: height 0.3s ease;
            }
            .chart-label {
                margin-top: 8px;
                text-align: center;
                font-size: 0.9rem;
            }
            .chart-label div:first-child {
                font-weight: bold;
                color: #007bff;
            }
            .category-list {
                background: white;
                padding: 1rem;
                border-radius: 8px;
                box-shadow: 0 2px 4px rgba(0,0,0,0.1);
            }
            .category-grid {
                display: grid;
                grid-template-columns: repeat(3, 1fr);
                gap: 1rem;
                padding: 1rem 0;
            }
            .category-card {
                background: white;
                padding: 1rem;
                border-radius: 8px;
                box-shadow: 0 2px 4px rgba(0,0,0,0.1);
            }
            .category-card h3 {
                margin: 0;
                font-size: 1.1rem;
            }
            .category-card p {
                margin: 0.5rem 0 0 0;
                color: #666;
            }
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
        """),
        html.h1("Canvas"),
        html.div({"class": "grid-container"},
            html.div({"class": "left-column"},
                Statistics(),
                CategoryList(),
            ),
            html.div({"class": "right-column"},
                Chat(),
            ),
        ),
    )
    
app = FastAPI()
configure(app, HabitCanvas)
