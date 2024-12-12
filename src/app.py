from reactpy import component, html
from reactpy.backend.fastapi import configure
from fastapi import FastAPI

from .components.statistics import Statistics
from .components.category import CategoryList
from .components.chat import Chat
from .styles.base import base_styles, create_style_tag

url = "https://cdn.jsdelivr.net/npm/@picocss/pico@2/css/pico.min.css"
pico_css = html.link({"rel": "stylesheet", "href": url})

@component
def HabitCanvas():
    return html.div({"class": "container"},
        pico_css,
        create_style_tag(base_styles),
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
