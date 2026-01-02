# Quickstart Guide: Todo App

**Feature**: 001-todo-app
**Date**: 2026-01-02

## Getting Started

### Prerequisites
- Python 3.13+ installed
- UV package manager installed

### Setup
1. Clone or create the project directory
2. Navigate to the project root
3. Run `uv init` to initialize the project
4. Run `python -m src.todo.main` to start the application

### Project Structure
```
todo/
├── pyproject.toml          # UV project configuration
├── README.md               # Project documentation
└── src/
    └── todo/
        ├── __init__.py
        ├── main.py         # Entry point and main loop
        ├── models.py       # Todo dataclass definition
        ├── storage.py      # In-memory storage operations
        └── ui.py           # Console user interface
```

## Running the Application

1. Ensure you're in the project root directory
2. Execute: `python -m src.todo.main`
3. The main menu will appear with numbered options

## Using the Todo App

### Main Menu Options
1. **Add Todo** - Create a new todo item with title and optional description
2. **View Todos** - Display all current todo items with status indicators
3. **Mark Complete** - Change a todo item's status to complete
4. **Update Todo** - Modify an existing todo item's title or description
5. **Delete Todo** - Remove a specific todo item from the list
6. **Clear All** - Remove all todo items (with confirmation)
7. **Exit** - Quit the application

### Example Workflow
1. Start the application
2. Select "Add Todo" and enter a task like "Buy groceries"
3. Select "View Todos" to see your list
4. Select "Mark Complete" and enter the number of the completed task
5. Continue managing your tasks as needed

## Error Handling
- Invalid inputs will show helpful error messages
- The application will not crash on invalid user input
- Empty titles or invalid numbers will prompt for re-entry