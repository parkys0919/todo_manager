from datetime import datetime


class Task:
    """
    Todo 작업을 나타내는 기본 클래스.

    :param title: 작업 제목
    :param priority: 우선순위 (High, Medium, Low)
    :param due_date: 마감일 (YYYY-MM-DD)

    >>> task = Task("Study Python", "High", "2026-06-30")
    >>> task.completed
    False
    """

    def __init__(self, title, priority, due_date):
        self.title = title
        self.priority = priority
        self.due_date = due_date
        self.completed = False

    def mark_complete(self):
        """
        작업을 완료 상태로 변경한다.

        :return: None
        """
        self.completed = True

    def mark_incomplete(self):
        """
        작업을 미완료 상태로 변경한다.

        :return: None
        """
        self.completed = False

    def get_info(self):
        """
        작업 정보를 문자열로 반환한다.

        :return: str
        """
        status = "Completed" if self.completed else "Pending"

        return (
            f"Title: {self.title}, "
            f"Priority: {self.priority}, "
            f"Due Date: {self.due_date}, "
            f"Status: {status}"
        )

    def _validate_date(self):
        """
        날짜 형식을 검사하는 비공개 메서드.

        :return: bool
        """
        try:
            datetime.strptime(self.due_date, "%Y-%m-%d")
            return True
        except ValueError:
            return False
