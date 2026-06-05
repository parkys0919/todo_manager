import csv

from .task import Task
from .recurring_task import RecurringTask


def find_task(tasks, title):
    """
    제목으로 작업을 검색한다.

    :param tasks: 작업 목록
    :param title: 찾을 제목
    :return: Task 또는 None

    >>> tasks = [Task("Study", "High", "2026-06-30")]
    >>> find_task(tasks, "Study").title
    'Study'
    """
    for task in tasks:
        if task.title == title:
            return task

    return None


def save_tasks(tasks, filename):
    """
    작업 목록을 CSV 파일로 저장한다.

    :param tasks: 작업 목록
    :param filename: 파일명
    :return: None
    """

    with open(filename, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)

        writer.writerow(
            [
                "title",
                "priority",
                "due_date",
                "completed",
                "repeat_cycle"
            ]
        )

        for task in tasks:
            repeat_cycle = ""

            if isinstance(task, RecurringTask):
                repeat_cycle = task.repeat_cycle

            writer.writerow(
                [
                    task.title,
                    task.priority,
                    task.due_date,
                    task.completed,
                    repeat_cycle
                ]
            )


def load_tasks(filename):
    """
    CSV 파일에서 작업 목록을 읽어온다.

    :param filename: 파일명
    :return: list
    """

    tasks = []

    with open(filename, "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for row in reader:

            if row["repeat_cycle"]:
                task = RecurringTask(
                    row["title"],
                    row["priority"],
                    row["due_date"],
                    row["repeat_cycle"]
                )
            else:
                task = Task(
                    row["title"],
                    row["priority"],
                    row["due_date"]
                )

            task.completed = (
                row["completed"] == "True"
            )

            tasks.append(task)

    return tasks
