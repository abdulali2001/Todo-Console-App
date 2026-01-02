"""Storage layer for the todo application."""
from typing import List, Optional
from .models import Todo


class TodoList:
    """In-memory storage for todo items."""
    def __init__(self) -> None:
        """Initialize the todo list with an empty list and ID counter."""
        self.items: List[Todo] = []
        self.next_id: int = 1

    def add_item(self, title: str, description: str = "") -> int:
        """Add a new todo item to the list."""
        if not title or not title.strip(): raise ValueError("Cannot add item with empty title")
        todo = Todo(id=self.next_id, title=title.strip(), description=description.strip() if description else "", completed=False)
        todo.validate()
        self.items.append(todo)
        self.next_id += 1
        return todo.id

    def get_all_items(self) -> List[Todo]:
        """Get all todo items in the list."""
        return self.items.copy()

    def get_item_by_id(self, id: int) -> Optional[Todo]:
        """Get a specific todo item by its ID."""
        for item in self.items:
            if item.id == id: return item
        return None

    def update_item(self, id: int, title: str = None, description: str = None) -> bool:
        """Update an existing todo item."""
        item = self.get_item_by_id(id)
        if item is None: return False
        if title is not None:
            title = title.strip()
            if not title: raise ValueError("Title cannot be empty")
            item.title = title
        if description is not None:
            item.description = description.strip() if description else ""
        return True

    def delete_item(self, id: int) -> bool:
        """Delete a todo item by its ID."""
        item = self.get_item_by_id(id)
        if item is None: return False
        self.items.remove(item)
        return True

    def mark_complete(self, id: int) -> bool:
        """Mark a todo item as complete."""
        item = self.get_item_by_id(id)
        if item is None: return False
        item.completed = True
        return True

    def mark_incomplete(self, id: int) -> bool:
        """Mark a todo item as incomplete."""
        item = self.get_item_by_id(id)
        if item is None: return False
        item.completed = False
        return True

    def clear_all(self) -> bool:
        """Remove all todo items from the list."""
        self.items.clear()
        return True