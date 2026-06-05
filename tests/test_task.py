from todo_manager import Task


def test_task_creation():
    task = Task("Study", "High", "2026-06-30")

    assert task.title == "Study"
    assert task.priority == "High"
    assert task.completed is False


def test_mark_complete():
    task = Task("Study", "High", "2026-06-30")

    task.mark_complete()

    assert task.completed is True


def test_mark_incomplete():
    task = Task("Study", "High", "2026-06-30")

    task.mark_complete()
    task.mark_incomplete()

    assert task.completed is False


def test_get_info_contains_title():
    task = Task("Study", "High", "2026-06-30")

    assert "Study" in task.get_info()


def test_validate_date_success():
    task = Task("Study", "High", "2026-06-30")

    assert task._validate_date() is True


# Edge Case 1
def test_validate_date_invalid():
    task = Task("Study", "High", "2026-99-99")

    assert task._validate_date() is False