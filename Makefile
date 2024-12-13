PHONY: front

front:
	REACTPY_DEBUG_MODE=1 uv run uvicorn src.frontend.app:app --reload