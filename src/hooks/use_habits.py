from reactpy import hooks
from ..api.client import APIClient

# Mock data that would normally come from an API
MOCK_DATA = {
    "statistics": {
        'Month': ['Jan', 'Feb', 'Mar', 'Apr', 'May'],
        'Tasks': [23, 34, 45, 56, 43]
    },
    "categories": [
        {"id": 1, "name": "Work", "color": "#FF6B6B", "count": 12},
        {"id": 2, "name": "Personal", "color": "#4ECDC4", "count": 8},
        {"id": 3, "name": "Health", "color": "#45B7D1", "count": 15},
        {"id": 4, "name": "Learning", "color": "#96CEB4", "count": 6},
        {"id": 5, "name": "Projects", "color": "#FFEEAD", "count": 10},
        {"id": 6, "name": "Family", "color": "#D4A5A5", "count": 9},
    ],
    "messages": [
        {"id": 1, "sender": "AI", "text": "Hello! How can I help you today?", "timestamp": "10:00"},
        {"id": 2, "sender": "User", "text": "I need help organizing my tasks", "timestamp": "10:01"},
        {"id": 3, "sender": "AI", "text": "I can help you with that! What kind of tasks do you need to organize?", "timestamp": "10:02"},
    ]
}

async def fetch_mock_data():
    """
    Simulates an API call by returning mock data
    In the future, this will be replaced with actual API calls
    """
    return MOCK_DATA

def use_habits():
    """
    Custom hook for managing habits data state and fetching from the API
    Returns:
        tuple: (data, loading, error, refresh)
        - data: The habits data (statistics, categories, messages)
        - loading: Boolean indicating if data is being fetched
        - error: Any error that occurred during fetching
        - refresh: Function to manually refresh the data
    """
    # Initialize state
    data, set_data = hooks.use_state(None)
    loading, set_loading = hooks.use_state(True)
    error, set_error = hooks.use_state(None)
    
    # Create API client
    client = APIClient()
    
    async def fetch_data():
        """Fetch data from the API"""
        set_loading(True)
        set_error(None)
        try:
            result = await client.get_habits_data()
            if result:
                set_data(result)
            else:
                set_error("Failed to fetch data")
        except Exception as e:
            set_error(str(e))
        finally:
            set_loading(False)
    
    # Effect to fetch data on component mount
    hooks.use_effect(fetch_data, dependencies=[])
    
    return data, loading, error, fetch_data  # fetch_data can be used to refresh
