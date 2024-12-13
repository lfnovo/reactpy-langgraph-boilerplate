import httpx
from typing import AsyncGenerator, Dict, Any
from ..agent import graph

class APIClient:
    def __init__(self, base_url: str = "http://localhost:8000"):
        self.base_url = base_url
        self.client = httpx.AsyncClient()
    
    async def get_habits_data(self):
        """Fetch all habit data including statistics, categories, and messages"""
        try:
            # In a real app, this would be an actual API endpoint
            # For now, we'll return mock data
            return {
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
        except Exception as e:
            print(f"Error fetching habits data: {e}")
            return None
    
    @staticmethod
    async def stream_habits_data(messages: list = None) -> AsyncGenerator[Dict[str, Any], None]:
        """
        Stream habits data from the langgraph
        Args:
            messages: List of messages to initialize the graph with
        Yields:
            Dictionary containing updates from the graph nodes
        """
        inputs = dict(messages=messages or [])
        
        async for chunk in graph.astream(inputs, stream_mode="updates"):
            for node, values in chunk.items():
                yield values
    
    async def close(self):
        await self.client.aclose()
