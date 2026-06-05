# Todo Manager

## 1. Project Overview

Todo Manager is a Python package for managing tasks and recurring tasks.
It allows users to create tasks, mark them as completed, search tasks, and save/load task data using CSV files.

This project was developed as a final project for the Python Programming course and demonstrates object-oriented programming, inheritance, testing, documentation, and package distribution.

---

## 2. Installation

Clone the repository and install the package:

```bash
git clone https://github.com/parkys0919/todo_manager.git
cd todo_manager
pip install .
```

---

## 3. Quick Start

```python
from todo_manager import Task

task = Task(
    "Study Python",
    "High",
    "2026-06-30"
)

print(task.get_info())
```

---

## 4. Main Features

### Task Management

* Create tasks
* Mark tasks as complete
* Mark tasks as incomplete
* Display task information

### Recurring Tasks

* Daily recurring tasks
* Weekly recurring tasks
* Monthly recurring tasks
* Automatic due date calculation

### Utilities

* Search tasks by title
* Save tasks to CSV
* Load tasks from CSV

---

## 5. Running Tests

Install pytest:

```bash
pip install pytest
```

Run all tests:

```bash
pytest
```

---

## 6. Author

Name: Park Yunseung

Python Programming Final Project
