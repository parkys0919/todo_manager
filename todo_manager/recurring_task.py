from datetime import datetime, timedelta

from .task import Task


class RecurringTask(Task):
    """
    반복 작업을 나타내는 클래스.

    :param title: 작업 제목
    :param priority: 우선순위
    :param due_date: 마감일 (YYYY-MM-DD)
    :param repeat_cycle: 반복 주기 (daily, weekly, monthly)

    >>> task = RecurringTask(
    ...     "Exercise",
    ...     "Medium",
    ...     "2026-06-30",
    ...     "daily"
    ... )
    >>> task.repeat_cycle
    'daily'
    """

    def __init__(
        self,
        title,
        priority,
        due_date,
        repeat_cycle
    ):
        super().__init__(
            title,
            priority,
            due_date
        )

        self.repeat_cycle = repeat_cycle

    def next_due_date(self):
        """
        다음 마감일을 계산한다.

        :return: str
        """

        current_date = datetime.strptime(
            self.due_date,
            "%Y-%m-%d"
        )

        if self.repeat_cycle == "daily":
            next_date = current_date + timedelta(days=1)

        elif self.repeat_cycle == "weekly":
            next_date = current_date + timedelta(days=7)

        elif self.repeat_cycle == "monthly":
            next_date = current_date + timedelta(days=30)

        else:
            raise ValueError(
                "repeat_cycle must be daily, weekly, or monthly"
            )

        return next_date.strftime("%Y-%m-%d")

    def update_due_date(self):
        """
        다음 반복 일정으로 마감일을 갱신한다.

        :return: None
        """

        self.due_date = self.next_due_date()

    def get_info(self):
        """
        반복 작업 정보를 반환한다.

        :return: str
        """

        base_info = super().get_info()

        return (
            f"{base_info}, "
            f"Repeat Cycle: {self.repeat_cycle}"
        )
