"""User interface for the todo application."""
from typing import Tuple
from .models import Todo


def display_menu() -> None:
    """Display the main menu with numbered options."""
    print("\n=== Todo App ===")
    print("1. Add Todo")
    print("2. View Todos")
    print("3. Mark Complete/Incomplete")
    print("4. Update Todo")
    print("5. Delete Todo")
    print("6. Clear All Todos")
    print("7. Exit")
    print("=" * 15)


def get_user_choice() -> int:
    """Get user's menu choice with input validation."""
    while True:
        try:
            choice = input("Enter your choice (1-7): ").strip()
            choice_num = int(choice)
            if 1 <= choice_num <= 7:
                return choice_num
            print("Invalid choice. Please enter a number between 1 and 7.")
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 7.")


def get_todo_input() -> Tuple[str, str]:
    """Get title and description input from user."""
    while True:
        title = input("Enter todo title: ").strip()
        if title:
            break
        print("Title cannot be empty. Please try again.")

    description = input("Enter description (optional, press Enter to skip): ").strip()
    return title, description


def get_item_id() -> int:
    """Get item ID from user with input validation."""
    while True:
        try:
            item_id = input("Enter item number: ").strip()
            id_num = int(item_id)
            if id_num > 0:
                return id_num
            print("Item number must be a positive number. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")


def display_todos(todos: list) -> None:
    """Display all todos in a formatted way."""
    if not todos:
        print("\nNo todos in the list.")
        return

    print("\nYour Todos:")
    print("-" * 50)
    for todo in todos:
        status = "[x]" if todo.completed else "[ ]"
        print(f"{status} {todo.id}. {todo.title}")
        if todo.description:
            print(f"      Description: {todo.description}")
    print("-" * 50)


def display_message(message: str) -> None:
    """Display a message to the user."""
    print(message)


def get_confirmation(message: str) -> bool:
    """Get yes/no confirmation from user."""
    while True:
        response = input(f"{message} (yes/no): ").strip().lower()
        if response in ['yes', 'y']:
            return True
        elif response in ['no', 'n']:
            return False
        print("Please enter 'yes' or 'no'.")