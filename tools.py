import datetime
from functools import wraps
from loguru import logger
from chinese_calendar import is_holiday


def run_only_on_workdays(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        today = datetime.datetime.today()
        if is_holiday(today) or today.weekday() in (5, 6):  # 周六日不上班
            logger.info("今天不上班")
            return None
        else:
            return func(*args, **kwargs)

    return wrapper
