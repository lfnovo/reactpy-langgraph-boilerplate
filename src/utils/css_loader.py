from pathlib import Path
from reactpy import html

def load_css(css_file: str) -> html.style:
    """
    Load a CSS file and return it as a style tag
    Args:
        css_file: Path to the CSS file relative to the static/css directory
    Returns:
        html.style tag with the CSS content
    """
    css_path = Path(__file__).parent.parent / 'static' / 'css' / css_file
    with open(css_path, 'r') as f:
        return html.style(f.read())
