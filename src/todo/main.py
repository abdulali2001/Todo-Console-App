"""Main entry point for the todo application."""
from .storage import TodoList
from .ui import (
    display_menu, get_user_choice, get_todo_input,
    display_todos, get_item_id, get_confirmation, display_message
)


def main() -> None:
    """Main function to run the todo application."""
    todo_list = TodoList()

    while True:
        try:
            display_menu()
            choice = get_user_choice()

            if choice == 1:  # Add Todo
                title, description = get_todo_input()
                try:
                    todo_id = todo_list.add_item(title, description)
                    display_message(f"Todo added successfully with ID: {todo_id}")
                except ValueError as e:
                    display_message(f"Error adding todo: {str(e)}")

            elif choice == 2:  # View Todos
                display_todos(todo_list.get_all_items())

            elif choice == 3:  # Mark Complete/Incomplete
                todos = todo_list.get_all_items()
                if not todos:
                    display_message("No todos available to mark.")
                    continue
                display_todos(todos)
                item_id = get_item_id()
                item = todo_list.get_item_by_id(item_id)
                if item is None:
                    display_message("Item not found. Please enter a valid item number.")
                    continue
                success = todo_list.mark_incomplete(item_id) if item.completed else todo_list.mark_complete(item_id)
                msg = f"Todo {item_id} marked as {'incomplete' if item.completed else 'complete'}."
                if success: display_message(msg)

            elif choice == 4:  # Update Todo
                todos = todo_list.get_all_items()
                if not todos:
                    display_message("No todos available to update.")
                    continue
                display_todos(todos)
                item_id = get_item_id()
                item = todo_list.get_item_by_id(item_id)
                if item is None:
                    display_message("Item not found. Please enter a valid item number.")
                    continue
                new_title = input(f"Enter new title (current: '{item.title}', press Enter to keep current): ").strip()
                new_description = input(f"Enter new description (current: '{item.description}', press Enter to keep current): ").strip()
                new_title = new_title if new_title else None
                new_description = new_description if new_description else None
                try:
                    success = todo_list.update_item(item_id, new_title, new_description)
                    msg = f"Todo {item_id} updated successfully." if success else "Failed to update todo."
                    display_message(msg)
                except ValueError as e:
                    display_message(f"Error updating todo: {str(e)}")

            elif choice == 5:  # Delete Todo
                todos = todo_list.get_all_items()
                if not todos:
                    display_message("No todos available to delete.")
                    continue
                display_todos(todos)
                item_id = get_item_id()
                item = todo_list.get_item_by_id(item_id)
                if item is None:
                    display_message("Item not found. Please enter a valid item number.")
                    continue
                success = todo_list.delete_item(item_id)
                msg = f"Todo {item_id} deleted successfully." if success else "Failed to delete todo."
                display_message(msg)

            elif choice == 6:  # Clear All Todos
                todos = todo_list.get_all_items()
                if not todos:
                    display_message("No todos to clear.")
                    continue
                if get_confirmation("Are you sure you want to clear all todos?"):
                    todo_list.clear_all()
                    display_message("All todos cleared successfully.")
                else:
                    display_message("Clear all operation cancelled.")

            elif choice == 7:  # Exit
                display_message("Thank you for using Todo App. Goodbye!")
                break

        except KeyboardInterrupt:
            display_message("\n\nApplication interrupted. Goodbye!")
            break
        except Exception as e:
            display_message(f"An unexpected error occurred: {str(e)}")
            display_message("Please try again.")


if __name__ == "__main__":
    main()