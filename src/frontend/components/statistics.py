from reactpy import component, html
from reactpy_apexcharts import ApexChart

from ..utils.css_loader import load_css


@component
def Statistics(data):
    # Get statistics data with default empty values
    months = data.get('month', [])
    tasks = data.get('tasks', [])
    
    return html.div(
        {"class": "statistics-container"},
        load_css('statistics.css'),
        html.h2("Statistics"),
        html.div(
            {"class": "chart-container"},
            ApexChart(
                options={
                    'chart': {
                        'id': 'tasks-chart',
                        'toolbar': {'show': False},
                        'background': 'transparent',
                        'animations': {
                            'enabled': True,
                            'easing': 'easeinout',
                            'speed': 800,
                            'animateGradually': {
                                'enabled': True,
                                'delay': 150
                            }
                        }
                    },
                    'xaxis': {
                        'categories': months,
                        'labels': {'style': {'colors': '#ffffff'}}
                    },
                    'yaxis': {
                        'labels': {'style': {'colors': '#ffffff'}}
                    },
                    'theme': {'mode': 'dark'},
                    'colors': ['#4ECDC4'],
                    'grid': {
                        'borderColor': 'rgba(128,128,128,0.2)',
                        'strokeDashArray': 4
                    },
                    'plotOptions': {
                        'bar': {
                            'borderRadius': 4,
                            'columnWidth': '60%'
                        }
                    }
                },
                series=[{
                    'name': 'Tasks',
                    'data': tasks
                }],
                chart_type="bar",
                width="100%",
            )
        )
    )
