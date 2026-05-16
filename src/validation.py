
from typing import Dict, Any


MIN_RR_COUNT = 300


def validate_session(parsed_session: Dict[str, Any], min_rr_count: int = MIN_RR_COUNT) -> Dict[str, Any]:
    """
    Validate whether a parsed HRM session contains enough usable RR interval data.

    Parameters
    ----------
    parsed_session : Dict[str, Any]
        Parsed HRM session returned by read_hrm_file().
    min_rr_count : int
        Minimum number of RR intervals required to treat a session as valid.

    Returns
    -------
    Dict[str, Any]
        Validation result containing validity status and reason.
    """
    rr_count = parsed_session.get("rr_count", 0)

    if rr_count == 0:
        return {
            "is_valid": False,
            "reason": "invalid_no_rr_data"
        }

    if rr_count < min_rr_count:
        return {
            "is_valid": False,
            "reason": "invalid_too_short"
        }

    return {
        "is_valid": True,
        "reason": "valid"
    }
