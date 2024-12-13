from typing import Any, AsyncGenerator, Dict

from ...backend.agent import graph


class APIClient:
    
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
