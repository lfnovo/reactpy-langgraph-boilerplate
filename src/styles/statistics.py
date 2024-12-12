from reactpy import html
from .base import create_style_tag

statistics_styles = """
    .statistics-container {
        background: white;
        padding: 1rem;
        border-radius: 8px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    
    .chart-container {
        display: flex;
        justify-content: space-around;
        align-items: flex-end;
        height: 300px;
        padding: 20px;
        background: white;
        border-radius: 8px;
    }
    
    .chart-column {
        display: flex;
        flex-direction: column;
        align-items: center;
        width: 60px;
    }
    
    .chart-bar {
        width: 40px;
        background: #007bff;
        border-radius: 4px 4px 0 0;
        transition: height 0.3s ease;
    }
    
    .chart-label {
        margin-top: 8px;
        text-align: center;
        font-size: 0.9rem;
    }
    
    .chart-label div:first-child {
        font-weight: bold;
        color: #007bff;
    }
"""

statistics_style_tag = create_style_tag(statistics_styles)
