import asyncio
import operator
import time
from typing import Annotated, Dict, List, Optional

from langchain_core.runnables import RunnableConfig
from langgraph.graph import END, START, StateGraph
from pydantic import BaseModel, Field


class ThreadState(BaseModel):
    categories: Optional[List[Dict]] = Field(default_factory=list)
    messages: Annotated[list, operator.add] = Field(default_factory=list)
    statistics: Optional[Dict] = Field(default_factory=dict)
    

async def get_stats(state: ThreadState, config: RunnableConfig) -> dict:
    # Calculate dates for mock data
    return {"statistics": {
        'month': ['Jan', 'Feb', 'Mar', 'Apr', 'May'],
        'tasks': [23, 34, 45, 56, 43]
    },}


async def get_categories(state: ThreadState, config: RunnableConfig) -> dict:
    # Calculate dates for mock data
    return { "categories": [
        {"id": 1, "name": "Work", "color": "#FF6B6B", "count": 12},
        {"id": 2, "name": "Personal", "color": "#4ECDC4", "count": 8},
        {"id": 3, "name": "Health", "color": "#45B7D1", "count": 15},
        {"id": 4, "name": "Learning", "color": "#96CEB4", "count": 6},
        {"id": 5, "name": "Projects", "color": "#FFEEAD", "count": 10},
        {"id": 6, "name": "Family", "color": "#D4A5A5", "count": 9},
    ],}

async def get_chat(state: ThreadState, config: RunnableConfig) -> dict:
    # Calculate dates for mock data
    return { "messages": [
        {"id": 1, "sender": "AI", "text": "Hellowww! How can I help you today?", "timestamp": "10:00"},
        {"id": 2, "sender": "User", "text": "I need help organizing my tasks", "timestamp": "10:01"},
        {"id": 3, "sender": "AI", "text": "I can help you with that! What kind of tasks do you need to organize?", "timestamp": "10:02"},
    ]}


agent_state = StateGraph(ThreadState)
agent_state.add_node("get_stats", get_stats)
agent_state.add_node("get_categories", get_categories)
agent_state.add_node("get_chat", get_chat)
agent_state.add_edge(START, "get_stats")
agent_state.add_edge("get_stats", "get_categories")
agent_state.add_edge("get_categories", "get_chat")
agent_state.add_edge("get_chat", END)
graph = agent_state.compile()
graph = agent_state.compile()
