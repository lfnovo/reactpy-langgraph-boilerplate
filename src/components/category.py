from reactpy import component, html
from ..utils.css_loader import load_css

# Mock data - In a real app, this would come from a database or API
mock_categories = [
    {"id": 1, "name": "Work", "color": "#FF6B6B", "count": 12},
    {"id": 2, "name": "Personal", "color": "#4ECDC4", "count": 8},
    {"id": 3, "name": "Health", "color": "#45B7D1", "count": 15},
    {"id": 4, "name": "Learning", "color": "#96CEB4", "count": 6},
    {"id": 5, "name": "Projects", "color": "#FFEEAD", "count": 10},
    {"id": 6, "name": "Family", "color": "#D4A5A5", "count": 9},
]

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
        load_css('category.css'),
        html.h2("Categories"),
        html.div(
            {"class": "category-grid"},
            [
                html.div(
                    {"key": f"category-{category['id']}"}, 
                    CategoryCard(category)
                ) for category in mock_categories
            ]
        )
    )
