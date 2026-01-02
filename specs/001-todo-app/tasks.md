# Tasks: Todo App

**Feature**: 001-todo-app
**Date**: 2026-01-02
**Input**: Feature specification from `specs/001-todo-app/spec.md`

## Phase 1: Setup

**Goal**: Initialize project structure with UV and Python 3.13+

- [X] T001 Create project directory structure per plan
- [X] T002 Initialize UV project with Python 3.13+
- [X] T003 Create src/todo directory structure
- [X] T004 Create empty module files (__init__.py, models.py, storage.py, ui.py, main.py)
- [X] T005 Create tests directory structure
- [X] T006 Create README.md with project description

## Phase 2: Foundational

**Goal**: Implement core data models and storage layer that all user stories depend on

- [X] T007 [P] Define Todo dataclass in src/todo/models.py with id, title, description, completed, created_at attributes
- [X] T008 [P] Implement Todo validation rules in src/todo/models.py
- [X] T009 [P] Define TodoList class in src/todo/storage.py with items list and next_id counter
- [X] T010 [P] Implement add_item method in TodoList with validation for non-empty title
- [X] T011 [P] Implement get_all_items method in TodoList
- [X] T012 [P] Implement get_item_by_id method in TodoList with proper error handling
- [X] T013 [P] Implement update_item method in TodoList with validation rules
- [X] T014 [P] Implement delete_item method in TodoList with validation
- [X] T015 [P] Implement mark_complete and mark_incomplete methods in TodoList
- [X] T016 [P] Implement clear_all method in TodoList with confirmation requirement

## Phase 3: User Story 1 - Add New Todo Item (Priority: P1)

**Goal**: Implement functionality to add new todo items with title and optional details

**Independent Test**: Can be fully tested by entering "Add Todo" command, providing a title, and verifying the item appears in the list. Delivers the core value of capturing tasks.

- [X] T017 [US1] Implement display_menu function in src/todo/ui.py with numbered options
- [X] T018 [US1] Implement get_user_choice function in src/todo/ui.py with input validation
- [X] T019 [US1] Implement get_todo_input function in src/todo/ui.py to get title and description
- [X] T020 [US1] Implement add todo functionality in main.py that calls UI and storage
- [X] T021 [US1] Test adding todo with valid title creates item with incomplete status
- [X] T022 [US1] Test adding todo with empty title shows error and re-prompts
- [X] T023 [US1] Test adding todo with description stores both title and description

## Phase 4: User Story 2 - View Todo List (Priority: P1)

**Goal**: Implement functionality to display all todo items in a clear, readable format

**Independent Test**: Can be fully tested by adding some items and then viewing the list. Delivers the core value of seeing what tasks need to be done.

- [X] T024 [US2] Implement display_todos function in src/todo/ui.py with proper formatting
- [X] T025 [US2] Implement view todos functionality in main.py that calls storage and UI
- [X] T026 [US2] Test viewing todos after adding items shows all with numbers and status
- [X] T027 [US2] Test viewing empty todo list shows appropriate message
- [X] T028 [US2] Test viewing todos with many items displays in readable format

## Phase 5: User Story 3 - Mark Todo as Complete/Incomplete (Priority: P2)

**Goal**: Implement functionality to update status of todo items from incomplete to complete (or vice versa)

**Independent Test**: Can be fully tested by adding an item, marking it complete, then viewing the list to confirm status changed. Delivers value by allowing task tracking.

- [X] T029 [US3] Implement get_item_id function in src/todo/ui.py with validation
- [X] T030 [US3] Implement mark complete/incomplete functionality in main.py that calls storage and UI
- [X] T031 [US3] Test marking valid todo as complete changes status to complete
- [X] T032 [US3] Test marking with invalid item number shows error and re-prompts
- [X] T033 [US3] Test marking completed item as incomplete changes status to incomplete

## Phase 6: User Story 4 - Update Todo Item (Priority: P2)

**Goal**: Implement functionality to modify existing todo items' title or description

**Independent Test**: Can be fully tested by adding an item, updating its details, and viewing to confirm changes. Delivers value by allowing task refinement.

- [X] T034 [US4] Implement update todo functionality in main.py that calls storage and UI
- [X] T035 [US4] Test updating valid todo with new details updates the item correctly
- [X] T036 [US4] Test updating with invalid item number shows error and re-prompts

## Phase 7: User Story 5 - Delete Todo Item (Priority: P3)

**Goal**: Implement functionality to remove specific todo items from the list

**Independent Test**: Can be fully tested by adding items, deleting one, and viewing the list to confirm removal. Delivers value by allowing list maintenance.

- [X] T037 [US5] Implement delete todo functionality in main.py that calls storage and UI
- [X] T038 [US5] Test deleting valid todo removes it from the list
- [X] T039 [US5] Test deleting with invalid item number shows error and re-prompts

## Phase 8: User Story 6 - Clear All Todo Items (Priority: P3)

**Goal**: Implement functionality to remove all todo items with confirmation

**Independent Test**: Can be fully tested by adding multiple items, using clear all function with confirmation, and viewing the empty list. Delivers value by allowing quick list reset.

- [X] T040 [US6] Implement get_confirmation function in src/todo/ui.py for yes/no prompts
- [X] T041 [US6] Implement clear all functionality in main.py that calls storage and UI
- [X] T042 [US6] Test clearing all todos with confirmation removes all items
- [X] T043 [US6] Test clearing all todos without confirmation keeps items unchanged

## Phase 9: Polish & Cross-Cutting Concerns

**Goal**: Implement error handling, edge cases, and final integration

- [X] T044 Handle non-numeric input when number is expected with validation
- [X] T045 Handle empty input for required fields with appropriate error messages
- [X] T046 Handle invalid menu selections with re-prompt
- [X] T047 Handle trying to operate on non-existent item numbers with error messages
- [X] T048 Implement main loop in main.py that continues until user chooses to exit
- [X] T049 Add proper exception handling throughout to prevent crashes
- [X] T050 Test complete workflow with all 5 core features working together
- [X] T051 Verify application stays under 300 lines of code as specified
- [X] T052 Verify all functions have type hints and docstrings as per constitution
- [X] T053 Run complete integration test of all features

## Dependencies

**User Story Completion Order**: US1 and US2 must be completed first as they are foundational, then US3, US4, US5, US6 can be completed in any order.

## Parallel Execution Examples

- **Parallel Tasks**: T007-T016 can be developed in parallel since they are all foundational components in different files
- **Story-Specific Parallelism**: Within each user story, UI and storage implementations can often be developed in parallel by different developers

## Implementation Strategy

1. **MVP Scope**: Complete Phase 1 (Setup) + Phase 2 (Foundational) + US1 (Add Todo) + US2 (View Todo) to deliver basic functionality
2. **Incremental Delivery**: Each user story adds complete, testable functionality to the application
3. **Testing Approach**: Each task includes specific test criteria to verify completion