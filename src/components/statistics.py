from reactpy import component, html
from ..utils.css_loader import load_css

@component
def Statistics(data):
    return html.div(
        {"class": "statistics-container"},
        load_css('statistics.css'),
        html.h2("Statistics"),
        html.div(
            {"class": "chart-container"},
            html.div(
                {"class": "chart"},
                [
                    html.div(
                        {
                            "class": "bar",
                            "style": {
                                "height": f"{(task / max(data['Tasks'])) * 100}%"
                            },
                            "key": f"bar-{i}"
                        },
                        html.div({"class": "task-count"}, str(task)),
                        html.div({"class": "month"}, month)
                    )
                    for i, (month, task) in enumerate(zip(data['Month'], data['Tasks']))
                ]
            )
        )
    )
