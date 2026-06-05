import pytest

from todo_manager import RecurringTask


def test_recurring_task_creation():
    task = RecurringTask(
        "Exercise",
        "Medium",
        "2026-06-30",
        "daily"
    )

    assert task.repeat_cycle == "daily"


def test_next_due_date_daily():
    task = RecurringTask(
        "Exercise",
        "Medium",
        "2026-06-30",
        "daily"
    )

    assert task.next_due_date() == "2026-07-01"


def test_update_due_date():
    task = RecurringTask(
        "Exercise",
        "Medium",
        "2026-06-30",
        "daily"
    )

    task.update_due_date()

    assert task.due_date == "2026-07-01"


# Edge Case 2
def test_invalid_repeat_cycle():
    task = RecurringTask(
        "Exercise",
        "Medium",
        "2026-06-30",
        "invalid"
    )

    with pytest.raises(ValueError):
        task.next_due_date()


# Edge Case 3
def test_empty_title():
    task = RecurringTask(
        "",
        "Medium",
        "2026-06-30",
        "daily"
    )

    assert task.title == ""