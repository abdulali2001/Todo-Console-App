---
id: 1
title: "Create Todo App Constitution"
stage: "constitution"
date_iso: "2026-01-02"
surface: "agent"
model: "claude-sonnet-4-5-20250929"
feature: "none"
branch: "master"
user: "user"
command: "sp.constitution"
labels: ["constitution", "todo-app", "setup"]
spec: null
ticket: null
adr: null
pr: null
files_yaml: |
  - .specify/memory/constitution.md
  - history/prompts/constitution/1-create-todo-app-constitution.constitution.prompt.md
tests_yaml: []
prompt_text: |
  Project: Phase I - In-Memory Python Console-Based Todo App

  Core principles:
  - Simplicity first: minimal code, easy to understand and extend
  - Clean architecture: clear separation between data, logic and UI (console)
  - No persistence: everything lives only in memory (program restart = data loss)
  - User-friendly console interface: clear, readable, forgiving input handling
  - Defensive programming: validate all user inputs, graceful error messages

  Key standards:
  - Python 3.13+ (or latest stable: 3.14 as of Jan 2026) — use modern syntax where it improves clarity
  - No external libraries except built-ins (no click, typer, rich, etc. unless explicitly allowed later)
  - Follow PEP 8 style (black formatting strongly recommended)
  - Use type hints on all functions and important variables (from typing import ...)
  - Docstrings on every public function/class (Google or NumPy style)
  - Meaningful variable/function names (no abbreviations like lst, td, pri)
  - Error handling: specific except clauses only, never bare except:
  - Input validation: reject invalid choices, out-of-range numbers, empty titles, etc.

  Constraints:
  - Single file preferred (todo.py) — max 2 files if needed (e.g. models.py)
  - In-memory storage only: use list[dict] or dataclass + list (no json, pickle, database in Phase I)
  - No save/load commands allowed in Phase I (explicitly forbidden)
  - Console menu must support at minimum:
    - Add new todo (title + optional description/priority/due date)
    - List all todos (numbered, show status, priority if present)
    - Mark todo as done/undone (by number)
    - Delete todo (by number)
    - Clear all todos (with yes/no confirmation)
    - Exit / Quit
  - Use only basic input() and print() for UI — no curses, rich, prompt_toolkit, etc.

  Success criteria:
  - App runs without crashing on invalid inputs (e.g. non-integer when asking for number)
  - All required commands work correctly and consistently
  - Todos displayed in readable format, example:
    [ ] 1. Buy groceries     High     2026-01-15
    [x] 2. Finish constitution prompt
response_text: |
  Created a constitution for the Phase I In-Memory Python Console-Based Todo App based on the provided requirements. The constitution includes:

  1. Core Principles:
     - Simplicity First: Minimal, understandable, and extendable code
     - Clean Architecture: Clear separation between data, business logic, and UI
     - In-Memory Only: No persistence, data exists only in memory
     - User-Friendly Console Interface: Clear, readable, forgiving input handling
     - Defensive Programming: Input validation with graceful error messages
     - Type Safety and Documentation: Type hints and docstrings required

  2. Additional Constraints:
     - Python 3.13+ with PEP 8 style
     - No external libraries except built-ins
     - Single file application (todo.py)
     - Console menu requirements

  3. Development Standards:
     - Type hints on all functions
     - Docstrings on all public functions/classes
     - Specific error handling
     - Input validation requirements

  4. Governance section with amendment procedures
outcome: "Constitution file created successfully at .specify/memory/constitution.md"
evaluation: "The constitution accurately reflects all requirements provided by the user and follows the template structure."
---

# Todo App Constitution

## Core Principles

### Simplicity First
All code must be minimal, easy to understand and extend. Complexity should be introduced only when absolutely necessary. Features should be implemented with the fewest possible lines of code while maintaining readability and maintainability.

### Clean Architecture
Maintain clear separation between data, business logic and user interface (console). Data models, business rules, and presentation layers must be distinct and loosely coupled. This enables easier testing, maintenance and future modifications.

### In-Memory Only
All data must exist only in memory with no persistence. The application must not save data to files, databases or external storage. Program restart results in complete data loss - this is an intentional design constraint for Phase I.

### User-Friendly Console Interface
The console interface must be clear, readable and forgiving with input handling. Error messages should be helpful and guide users toward correct input. Menu navigation should be intuitive and consistent across all commands.

### Defensive Programming
All user inputs must be validated with graceful error messages. The application must handle invalid inputs without crashing. Input validation should reject invalid choices, out-of-range numbers, empty titles, and other malformed data.

### Type Safety and Documentation
All functions and important variables must use type hints. Every public function and class must have docstrings following Google or NumPy style. Variable and function names must be meaningful without abbreviations.

## Additional Constraints

Python 3.13+ (or latest stable) must be used with modern syntax where it improves clarity. No external libraries except built-ins are allowed. Follow PEP 8 style with black formatting. Use specific except clauses only, never bare except:. The application should be in a single file (todo.py) with in-memory storage using list[dict] or dataclass + list.

The console menu must support: Add new todo (title + optional description/priority/due date), List all todos (numbered, show status, priority if present), Mark todo as done/undone (by number), Delete todo (by number), Clear all todos (with yes/no confirmation), and Exit/Quit.

## Development Standards

All code must follow PEP 8 style guidelines with black formatting strongly recommended. Type hints are required on all functions and important variables using the typing module. Docstrings are required on every public function/class using Google or NumPy style. Error handling must use specific except clauses only, never bare except:.

Input validation must reject invalid choices, out-of-range numbers, empty titles, and other malformed inputs. The application must run without crashing on invalid inputs (e.g. non-integer when asking for number). All required commands must work correctly and consistently.

## Governance

This constitution supersedes all other practices and development guidelines for this project. All code changes must comply with these principles. Amendments to this constitution require explicit documentation, approval from project maintainers, and a migration plan for existing code.

All pull requests and code reviews must verify compliance with these principles. Code complexity must be justified with clear benefits that outweigh the added maintenance burden. New features must align with the core principles of simplicity, clean architecture, and defensive programming.

**Version**: 1.0.0 | **Ratified**: 2026-01-02 | **Last Amended**: 2026-01-02