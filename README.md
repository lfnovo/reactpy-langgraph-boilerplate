# ReactPy Prototype Application

A modern web application built with ReactPy and FastAPI, demonstrating component-based architecture and state management patterns.

## 🏗️ Architecture

### Tech Stack
- **Frontend**: ReactPy (Python-based React-like library)
- **Backend**: FastAPI
- **Styling**: Pico CSS + Custom CSS
- **State Management**: ReactPy Hooks

### Project Structure
```
src/
├── components/          # React-like components
│   ├── category.py     # Category list and card components
│   ├── chat.py         # Chat interface component
│   └── statistics.py   # Statistics visualization component
├── static/
│   └── css/            # Component-specific and global styles
│       ├── base.css
│       ├── category.css
│       ├── chat.css
│       └── statistics.css
├── utils/
│   └── css_loader.py   # CSS loading utility
└── app.py              # Main application entry point
```

### Component Architecture

#### Main App (`app.py`)
- Acts as the application root
- Manages global state using ReactPy hooks
- Distributes state and callbacks to child components
- Configures FastAPI and static file serving

#### Components
1. **Statistics Component**
   - Displays task statistics in a bar chart
   - Receives data through props: `Month` and `Tasks` arrays

2. **Category Component**
   - Renders a grid of category cards
   - Each card shows category name, count, and custom color
   - Receives categories array through props

3. **Chat Component**
   - Implements real-time chat interface
   - Manages message input state locally
   - Receives messages array and message handler through props

### State Management
The application follows a top-down state management pattern:
- Global state is maintained in the root `HabitCanvas` component
- State is passed down to child components via props
- Child components communicate back to parent through callback functions
- Local state is used for component-specific UI elements (e.g., input fields)

## 🚀 Getting Started

### Prerequisites
- Python 3.7+
- pip (Python package manager)

### Installation
1. Clone the repository
```bash
git clone <repository-url>
cd reactpy-proto
```

2. Create and activate a virtual environment (optional but recommended)
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies
```bash
pip install -r requirements.txt
```

### Running the Application
```bash
uvicorn src.app:app --reload
```
The application will be available at `http://localhost:8000`

## 💅 Styling
The application uses a combination of:
- **Pico CSS**: For base styling and dark mode support
- **Custom CSS**: Component-specific styles in the `static/css` directory
- **CSS Variables**: For consistent theming and dark mode

## 🧪 Development Guidelines

### Adding New Components
1. Create a new file in the `components` directory
2. Import necessary ReactPy modules
3. Create corresponding CSS file in `static/css`
4. Use the `@component` decorator for component definition
5. Follow the props pattern for data and callback handling

### State Management Best Practices
- Keep state as close as possible to where it's needed
- Use props for parent-to-child communication
- Use callback functions for child-to-parent communication
- Avoid prop drilling by restructuring component hierarchy

### CSS Guidelines
- Use component-specific CSS files
- Leverage CSS variables for theming
- Follow BEM naming convention for classes
- Use the CSS loader utility for component styles

## 📚 Resources
- [ReactPy Documentation](https://reactpy.dev/docs/index.html)
- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [Pico CSS Documentation](https://picocss.com/docs/)
