# Data Model: Todo App

**Feature**: 001-todo-app
**Date**: 2026-01-02

## Todo Item Entity

### Attributes
- **id** (int): Unique identifier for the todo item, assigned sequentially
- **title** (str): Required title of the todo item, non-empty string
- **description** (str): Optional description of the todo item, can be empty
- **completed** (bool): Status indicator, True if completed, False if incomplete
- **created_at** (datetime): Timestamp when the item was created

### Validation Rules
- Title must be a non-empty string (length > 0)
- ID must be a positive integer
- Completed status must be a boolean value
- Created timestamp must be a valid datetime object

### State Transitions
- **Incomplete → Complete**: When user marks item as done
- **Complete → Incomplete**: When user marks item as undone

### Relationships
- Part of a TodoList collection (one-to-many relationship)

## Todo List Entity

### Attributes
- **items** (list[Todo]): Collection of Todo items stored in memory
- **next_id** (int): Counter for assigning unique IDs to new items

### Operations
- **add_item(title: str, description: str = "")**: Creates new Todo item and adds to list
- **get_all_items()**: Returns all Todo items in the list
- **get_item_by_id(id: int)**: Returns specific Todo item by ID
- **update_item(id: int, title: str = None, description: str = None)**: Updates existing Todo item
- **delete_item(id: int)**: Removes Todo item from list
- **mark_complete(id: int)**: Sets completed status to True
- **mark_incomplete(id: int)**: Sets completed status to False
- **clear_all()**: Removes all items from the list

### Validation Rules
- Cannot add items with empty titles
- Cannot update or delete non-existent items
- ID must exist when performing update/delete/mark operations
- Maximum list size is limited by available memory only

### State Transitions
- **Empty → Populated**: When first item is added
- **Populated → Empty**: When all items are deleted or cleared