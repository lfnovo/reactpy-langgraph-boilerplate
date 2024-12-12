from reactpy import html

# Base styles that are shared across components
base_styles = """
    .container {
        max-width: 1200px;
        margin: 0 auto;
        padding: 2rem;
    }
    
    .grid-container {
        display: grid;
        grid-template-columns: 2fr 1fr;
        gap: 2rem;
        padding: 1rem;
    }
    
    .left-column {
        display: flex;
        flex-direction: column;
        gap: 2rem;
    }
    
    .right-column {
        background-color: #f8f9fa;
        border-radius: 8px;
        padding: 1rem;
    }
"""

def create_style_tag(styles: str) -> html.style:
    """Helper function to create a style tag with the given styles"""
    return html.style(styles)
