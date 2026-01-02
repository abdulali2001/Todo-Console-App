<!-- Sync Impact Report:
     Version change: N/A (initial creation) → 1.0.0
     Modified principles: N/A (new principles created)
     Added sections: All sections (initial constitution)
     Removed sections: N/A
     Templates requiring updates: N/A (new file)
     Follow-up TODOs: None
-->
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