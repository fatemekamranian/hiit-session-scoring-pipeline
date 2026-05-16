
from typing import Dict
from datetime import datetime


def parse_date(date_str: str) -> datetime:
    """
    Convert a string in YYYYMMDD format to a datetime object.
    """
    return datetime.strptime(date_str, "%Y%m%d")


def compute_training_week(session_date: str, first_session_date: str) -> int:
    """
    Compute the training week for a session using the known program start date.
    """
    session_dt = parse_date(session_date)
    start_dt = parse_date(first_session_date)

    delta_days = (session_dt - start_dt).days
    week = delta_days // 7 + 1

    return week


def get_target_zone(max_hr: int, week: int) -> Dict[str, float]:
    """
    Compute target heart rate zone based on training week.
    """
    if week <= 2:
        low, high = 0.80, 0.85
    elif week <= 6:
        low, high = 0.85, 0.90
    else:
        low, high = 0.90, 0.95

    return {
        "low": low * max_hr,
        "high": high * max_hr
    }
