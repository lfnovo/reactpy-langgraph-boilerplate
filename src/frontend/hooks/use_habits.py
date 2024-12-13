from reactpy import hooks

from ..api.client import APIClient


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
    data, set_data = hooks.use_state({})
    loading, set_loading = hooks.use_state(True)
    error, set_error = hooks.use_state(None)
    
    async def fetch_data():
        """Fetch data from the API"""
        set_loading(True)
        set_error(None)
        
        try:
            current_data = {}
            async for values in APIClient.stream_habits_data():
                # Update our current data with the new values
                current_data.update(values)
                # Update the state with the accumulated data
                set_data(dict(current_data))  # Create new dict to trigger re-render
            
            if not current_data:
                set_error("No data received from API")
                
        except Exception as e:
            set_error(str(e))
        finally:
            set_loading(False)
    
    # Effect to fetch data on component mount
    hooks.use_effect(fetch_data, dependencies=[])
    
    return data, loading, error, fetch_data  # fetch_data can be used to refresh
