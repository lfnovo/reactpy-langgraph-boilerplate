from reactpy import component, html
from reactpy.backend.fastapi import configure
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from pathlib import Path

from .components.statistics import Statistics
from .components.category import CategoryList
from .components.chat import Chat
from .utils.css_loader import load_css

# Add Pico CSS with data-theme="dark"
pico_css = [
    html.link({"rel": "stylesheet", "href": "https://cdn.jsdelivr.net/npm/@picocss/pico@2/css/pico.min.css"}),
    html.script("""
        document.documentElement.setAttribute('data-theme', 'dark');
    """)
]

@component
def HabitCanvas():
    return html.div({"class": "container"},
        pico_css,
        load_css('base.css'),
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

# Mount static files
static_path = Path(__file__).parent / 'static'
app.mount("/static", StaticFiles(directory=str(static_path)), name="static")

configure(app, HabitCanvas)
