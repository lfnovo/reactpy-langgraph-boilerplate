from reactpy import component, html
from ..styles.statistics import statistics_style_tag

# Mock data - In a real app, this would come from a database or API
mock_data = {
    'Month': ['Jan', 'Feb', 'Mar', 'Apr', 'May'],
    'Tasks': [23, 34, 45, 56, 43]
}

@component
def Statistics():
    # Calculate percentage for each value
    max_value = max(mock_data['Tasks'])
    percentages = [int((value / max_value) * 100) for value in mock_data['Tasks']]
    
    return html.div(
        {"class": "statistics-container"},
        statistics_style_tag,
        html.h2("Statistics"),
        html.div(
            {"class": "chart-container"},
            [
                html.div(
                    {"class": "chart-column"},
                    html.div(
                        {"class": "chart-bar", "style": {"height": f"{percentage}%"}},
                    ),
                    html.div({"class": "chart-label"}, 
                        html.div(str(value)),
                        html.div(month)
                    )
                ) for month, value, percentage in zip(mock_data['Month'], mock_data['Tasks'], percentages)
            ]
        )
    )
