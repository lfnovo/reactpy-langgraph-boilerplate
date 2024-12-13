from pathlib import Path

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from reactpy import component, html
from reactpy.backend.fastapi import configure

from .components.category import CategoryList
from .components.chat import Chat
from .components.statistics import Statistics
from .hooks.use_habits import use_habits
from .utils.css_loader import load_css

# Add Pico CSS with data-theme="dark"
pico_css = [
    html.link({"key": "pico-css", "rel": "stylesheet", "href": "https://cdn.jsdelivr.net/npm/@picocss/pico@2/css/pico.min.css"}),
    html.script({"key": "theme-script"}, """
        document.documentElement.setAttribute('data-theme', 'dark');
    """)
]

@component
def HabitCanvas():
    # Use our custom hook to fetch and manage habit data
    data, loading, error, refresh = use_habits()
    
    def handle_new_message(message):
        """Callback to handle new messages from the Chat component"""
        # In a real app, this would send the message to the server
        # For now, we'll just refresh the data to simulate an update
        refresh()
    
    # Show loading state
    if loading:
        return html.div(
            {"class": "container"},
            *pico_css,
            load_css('base.css'),
            html.h1("Loading...")
        )
    
    # Show error state
    if error:
        return html.div(
            {"class": "container"},
            *pico_css,
            load_css('base.css'),
            html.h1("Error"),
            html.p(error),
            html.button({"on_click": lambda _: refresh()}, "Retry")
        )
    
    # Show data
    return html.div(
        {"class": "container"},
        *pico_css,
        load_css('base.css'),
        html.h1("Canvas"),
        html.div(
            {"class": "grid-container"},
            html.div(
                {"class": "left-column"},
                Statistics(data["statistics"]),
                CategoryList(categories=data["categories"]),
            ),
            html.div(
                {"class": "right-column"},
                Chat(
                    messages=data["messages"],
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
