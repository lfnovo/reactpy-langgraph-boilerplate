from reactpy import component, html
from reactpy_apexcharts import ApexChart

from ..utils.css_loader import load_css


@component
def Statistics(data):
    # Get statistics data
    return html.div(
        {"class": "statistics-container"},
        load_css('statistics.css'),
        html.h2("Statistics"),
        html.div(
            {"class": "chart-container"},
            ApexChart(
                options={
                    'chart': {'id': 'tasks-chart'},
                    'xaxis': {'categories': data.get('month', [])},
                    'theme': {'mode': 'dark'},
                    'colors': ['#4ECDC4']
                },
                series=[{
                    'name': 'Tasks',
                    'data': data.get('tasks', [])
                }],
                chart_type="bar",
                width="100%",
                height=50
            )
        )
    )

