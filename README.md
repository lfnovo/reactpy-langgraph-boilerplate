# 🚀 ReactPy + LangGraph Boilerplate

A modern, production-ready boilerplate for building reactive web applications using ReactPy and LangGraph. This project demonstrates best practices for building scalable applications with Python-based reactive UI and graph-based data processing.

## ✨ Features

- 🎯 **ReactPy Components**: Modern, React-like components written in pure Python
- 📊 **ApexCharts Integration**: Beautiful, responsive charts with dark mode support
- 🔄 **Async Data Streaming**: Real-time updates with LangGraph's streaming capabilities
- 🎨 **PicoCSS Integration**: Minimal, semantic CSS framework with automatic dark mode
- 🧩 **Component Library**: Ready-to-use components for common UI patterns
- 📱 **Responsive Layout**: Mobile-first design approach with PicoCSS's semantic elements
- 🛣️ **Client-side Routing**: Built-in routing with reactpy-router
- 🔧 **Developer Tools**: Comprehensive development setup with uv package manager

## 🏗️ Architecture

### Tech Stack
- **Frontend**: ReactPy (Python-based React-like library)
- **Backend**: FastAPI
- **Graphs**: LangGraph for async data processing
- **Charts**: ApexCharts via reactpy-apexcharts
- **Routing**: reactpy-router for client-side navigation
- **CSS Framework**: PicoCSS - A minimal, semantic CSS framework
- **State Management**: ReactPy Hooks

### Project Structure
```
src/
├── frontend/           # Frontend application
│   ├── components/     # Reusable UI components
│   │   ├── category.py # Category management
│   │   ├── chat.py     # Chat interface
│   │   └── statistics.py # Data visualization
│   ├── api/           # Frontend API clients
│   │   └── client.py   # API client with async streaming
│   ├── static/        # Static assets
│   │   └── css/       # PicoCSS customization and styles
│   └── utils/         # Frontend utilities
├── backend/           # Backend application
│   ├── api/          # API endpoints and routes
│   ├── models/       # Data models and schemas
│   ├── services/     # Business logic and services
│   ├── utils/        # Backend utilities
│   └── agent.py      # LangGraph setup and processing
└── app.py            # Application entry point
```

## 🚀 Getting Started

### Prerequisites
- Python 3.11 or higher
- [uv](https://github.com/astral-sh/uv) package manager (recommended)

### Installation

1. Clone the repository
```bash
git clone https://github.com/lfnovo/reactpy-langgraph-boilerplate.git
cd reactpy-langgraph-boilerplate
```

2. Create and activate a virtual environment
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

3. Install dependencies
```bash
uv pip install -r requirements.txt
```

### Development

1. Start the development server
```bash
uvicorn src.app:app --reload
```

2. Open your browser and navigate to `http://localhost:8000`

## 📚 Key Concepts

### Component Architecture
- **Atomic Design**: Components are organized following atomic design principles
- **Props & State**: Clean separation of props and state management
- **Custom Hooks**: Reusable logic encapsulated in custom hooks

### Async Data Flow
- **Streaming Updates**: Real-time data updates using LangGraph's streaming capabilities
- **State Management**: Centralized state management with ReactPy hooks
- **Error Handling**: Comprehensive error handling and loading states

### Styling with PicoCSS
- **Semantic HTML**: Leverage PicoCSS's semantic approach to styling
- **Automatic Dark Mode**: Built-in dark mode support without additional configuration
- **Custom Theming**: Easy customization through CSS variables
- **Responsive Grid**: Flexible layouts using PicoCSS's minimal grid system
- **Accessible Components**: Pre-styled, accessible form elements and components

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- [ReactPy](https://reactpy.dev/) - For the amazing Python-based reactive UI library
- [LangGraph](https://github.com/langchain-ai/langgraph) - For the powerful graph-based processing
- [FastAPI](https://fastapi.tiangolo.com/) - For the high-performance backend
- [PicoCSS](https://picocss.com/) - For the minimal, semantic CSS framework
- [ApexCharts](https://apexcharts.com/) - For beautiful, responsive charts
