from reactpy import component, html

from ..utils.css_loader import load_css


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
def CategoryList(categories):
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
                ) for category in categories
            ]
        )
    )

