"""Data models for the todo application."""
from dataclasses import dataclass
from datetime import datetime


@dataclass
class Todo:
    """Represents a single todo item."""
    id: int
    title: str
    description: str = ""
    completed: bool = False
    created_at: datetime = None

    def __post_init__(self):
        """Initialize the created_at field if not provided."""
        if self.created_at is None:
            self.created_at = datetime.now()

    def validate(self) -> None:
        """Validate the todo item attributes."""
        if not self.title or not self.title.strip():
            raise ValueError("Title must be a non-empty string")
        if not isinstance(self.completed, bool):
            raise ValueError("Completed status must be a boolean value")
        if not isinstance(self.id, int) or self.id <= 0:
            raise ValueError("ID must be a positive integer")