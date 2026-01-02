# Internal API Contracts: Todo App

**Feature**: 001-todo-app
**Date**: 2026-01-02

## Storage Module Contracts

### TodoStorage Class
```python
class TodoStorage:
    def __init__(self) -> None: ...
    def add_item(self, title: str, description: str = "") -> int: ...
    def get_all_items(self) -> list[Todo]: ...
    def get_item_by_id(self, id: int) -> Todo | None: ...
    def update_item(self, id: int, title: str = None, description: str = None) -> bool: ...
    def delete_item(self, id: int) -> bool: ...
    def mark_complete(self, id: int) -> bool: ...
    def mark_incomplete(self, id: int) -> bool: ...
    def clear_all(self) -> bool: ...
```

**Contract Details**:
- `add_item`: Returns the ID of the newly created item, raises ValueError if title is empty
- `get_item_by_id`: Returns None if item doesn't exist
- `update_item/delete_item/mark_complete/mark_incomplete`: Return True on success, False if item doesn't exist
- `clear_all`: Returns True after clearing all items

## UI Module Contracts

### UI Functions
```python
def display_menu() -> None: ...
def get_user_choice() -> int: ...
def get_todo_input() -> tuple[str, str]: ...
def get_item_id() -> int: ...
def display_todos(todos: list[Todo]) -> None: ...
def display_message(message: str) -> None: ...
def get_confirmation(message: str) -> bool: ...
```

**Contract Details**:
- All input functions handle validation and re-prompt on invalid input
- `get_user_choice`: Returns valid menu option number
- `get_item_id`: Returns valid existing item ID
- `get_confirmation`: Returns True for 'yes', False for 'no'

## Main Module Contracts

### Main Loop
```python
def main() -> None: ...
```

**Contract Details**:
- Continuously displays menu until user chooses to exit
- Handles all exceptions gracefully without crashing
- Maintains in-memory state for the duration of the session