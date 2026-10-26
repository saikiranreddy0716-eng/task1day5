
# Python Epic 0 Capstone — Contact Manager

## Project overview

A Python command-line application that creates, lists, searches,
updates and deletes contacts.

Contacts are stored locally in a JSON file and persist after the
application is restarted.

## Features

- Create contacts with an ID, name and phone number
- List all contacts
- Search by contact ID
- Update a contact's name and phone number
- Delete contacts
- Reject empty fields and duplicate IDs
- Handle missing or corrupt JSON files safely
- Automated tests with pytest

## Project structure

```text
task1day5/
├── contact_manager/
│   ├── __init__.py
│   ├── operations.py
│   ├── storage.py
│   └── cli.py
├── tests/
│   ├── test_operations.py
│   └── test_storage.py
├── .gitignore
└── README.md
```

## Requirements

- Python 3.10 or newer
- pytest

## Setup on Windows PowerShell

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install pytest
```

## Run the application

```powershell
python -m contact_manager.cli
```

## Run automated tests

```powershell
python -m pytest -v
```

## Example usage

```text
===== Contact Manager =====
1. Create contact
2. List contacts
3. Search contact
4. Update contact
5. Delete contact
6. Exit

Choose an option (1-6): 1
Enter contact ID: 101
Enter name: Ravi
Enter phone number: 9876543210
Contact 'Ravi' created.
```

Select option 2 to list contacts. Exit and run the application
again to confirm that the saved contact is still available.

## Troubleshooting

- If pytest is missing, activate `.venv` and run
  `python -m pip install pytest`.
- If imports fail, run commands from the project root,
  `task1day5`.
- If JSON is corrupt, inspect or repair `contacts.json` manually.
  The application will not start normally until the problem is fixed.
- If Git shows generated files, check `.gitignore` and `git status`.

## Data safety

`contacts.json` is local application data and should not be committed
to GitHub. Back up important contact data separately.
