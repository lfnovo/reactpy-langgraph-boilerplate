from reactpy import html
from .base import create_style_tag

category_styles = """
    .category-list {
        background: white;
        padding: 1rem;
        border-radius: 8px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    
    .category-grid {
        display: grid;
        grid-template-columns: repeat(3, 1fr);
        gap: 1rem;
        padding: 1rem 0;
    }
    
    .category-card {
        background: white;
        padding: 1rem;
        border-radius: 8px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    
    .category-card h3 {
        margin: 0;
        font-size: 1.1rem;
    }
    
    .category-card p {
        margin: 0.5rem 0 0 0;
        color: #666;
    }
"""

category_style_tag = create_style_tag(category_styles)
