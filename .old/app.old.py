from reactpy import component, html
from reactpy.backend.fastapi import configure
from fastapi import FastAPI

@component
def HelloWorld():
    return html.h1("Hello, world!")

# @component
# def DataList(items, filter_by_priority=None, sort_by_priority=False):
#     if filter_by_priority is not None:
#         items = [i for i in items if i["priority"] <= filter_by_priority]
#     if sort_by_priority:
#         items = sorted(items, key=lambda i: i["priority"])
#     list_item_elements = [html.li({"key": i["id"]}, i["text"]) for i in items]
#     return html.ul(list_item_elements)


# @component
# def TodoList():
#     tasks = [
#         {"id": 0, "text": "Make breakfast", "priority": 0},
#         {"id": 1, "text": "Feed the dog", "priority": 0},
#         {"id": 2, "text": "Do laundry", "priority": 2},
#         {"id": 3, "text": "Go on a run", "priority": 1},
#         {"id": 4, "text": "Clean the house", "priority": 2},
#         {"id": 5, "text": "Go to the grocery store", "priority": 2},
#         {"id": 6, "text": "Do some coding", "priority": 1},
#         {"id": 7, "text": "Read a book", "priority": 1},
#     ]
#     return html.section(
#         html.h1("My Todo List"),
#         DataList(tasks, filter_by_priority=1, sort_by_priority=True),
#     )

@component
def Item(name, done):
    if done:
        return html.li(name, " ✔")
    else:
        return html.li(name)

url = "https://cdn.jsdelivr.net/npm/@picocss/pico@2/css/pico.min.css"
pico_css = html.link({"rel": "stylesheet", "href": url})

@component
def TodoList():
    return html.div({"class": "container"},
        pico_css, 
        html.h1("My Todo List"),
        html.ul(
            Item("Find a cool problem to solve", done=True),
            Item("Build an app to solve it", done=True),
            Item("Share that app with the world!", done=False),
        ),
    )

    
app = FastAPI()
configure(app, TodoList)