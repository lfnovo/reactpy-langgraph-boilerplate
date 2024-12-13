from pathlib import Path

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from reactpy import component, hooks, html
from reactpy.backend.fastapi import configure

from .components.category import CategoryList
from .components.chat import Chat
from .components.statistics import Statistics
from .utils.css_loader import load_css

# Mock data that would normally come from an API
initial_data = {
    "statistics": {
        'Month': ['Jan', 'Feb', 'Mar', 'Apr', 'May'],
        'Tasks': [23, 34, 45, 56, 43]
    },
    "categories": [
        {"id": 1, "name": "Work", "color": "#FF6B6B", "count": 12},
        {"id": 2, "name": "Personal", "color": "#4ECDC4", "count": 8},
        {"id": 3, "name": "Health", "color": "#45B7D1", "count": 15},
        {"id": 4, "name": "Learning", "color": "#96CEB4", "count": 6},
        {"id": 5, "name": "Projects", "color": "#FFEEAD", "count": 10},
        {"id": 6, "name": "Family", "color": "#D4A5A5", "count": 9},
    ],
    "messages": [
        {"id": 1, "sender": "AI", "text": "Hello! How can I help you today?", "timestamp": "10:00"},
        {"id": 2, "sender": "User", "text": "I need help organizing my tasks", "timestamp": "10:01"},
        {"id": 3, "sender": "AI", "text": "I can help you with that! What kind of tasks do you need to organize?", "timestamp": "10:02"},
    ]
}

# Add Pico CSS with data-theme="dark"
pico_css = [
    html.link({"key": "pico-css", "rel": "stylesheet", "href": "https://cdn.jsdelivr.net/npm/@picocss/pico@2/css/pico.min.css"}),
    html.script({"key": "theme-script"}, """
        document.documentElement.setAttribute('data-theme', 'dark');
    """)
]

@component
def HabitCanvas():
    # Initialize state with mock data
    statistics, set_statistics = hooks.use_state(initial_data["statistics"])
    categories, set_categories = hooks.use_state(initial_data["categories"])
    messages, set_messages = hooks.use_state(initial_data["messages"])
    
    def handle_new_message(message):
        """Callback to handle new messages from the Chat component"""
        new_message = {
            "id": len(messages) + 1,
            "sender": "User",
            "text": message,
            "timestamp": "10:03"  # In real app, use actual timestamp
        }
        set_messages(messages + [new_message])
    
    return html.div({"class": "container"},
        *pico_css,
        load_css('base.css'),
        html.h1("Canvas"),
        html.div({"class": "grid-container"},
            html.div({"class": "left-column"},
                Statistics(statistics),
                CategoryList(categories=categories),
            ),
            html.div({"class": "right-column"},
                Chat(
                    messages=messages,
                    on_new_message=handle_new_message
                ),
            ),
        ),
    )
    
app = FastAPI()

# Mount static files
static_path = Path(__file__).parent / 'static'
app.mount("/static", StaticFiles(directory=str(static_path)), name="static")

configure(app, HabitCanvas)
