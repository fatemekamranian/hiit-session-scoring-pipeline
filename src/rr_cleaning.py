
from typing import List, Dict, Any
import numpy as np


MIN_RR_MS = 300
MAX_RR_MS = 2000
MISSED_BEAT_RATIO = 1.8


def clean_rr_intervals(
    rr_intervals: List[int],
    min_rr_ms: int = MIN_RR_MS,
    max_rr_ms: int = MAX_RR_MS,
    missed_beat_ratio: float = MISSED_BEAT_RATIO
) -> Dict[str, Any]:
    """
    Clean RR interval data by removing unrealistic values and correcting likely missed beats.

    Parameters
    ----------
    rr_intervals : List[int]
        Raw RR interval values in milliseconds.
    min_rr_ms : int
        Minimum physiologically plausible RR interval.
    max_rr_ms : int
        Maximum physiologically plausible RR interval.
    missed_beat_ratio : float
        Ratio used to identify likely missed beats compared with the previous RR interval.

    Returns
    -------
    Dict[str, Any]
        Cleaned RR intervals and cleaning statistics.
    """
    cleaned_rr = []
    removed_count = 0
    corrected_missed_beats = 0

    previous_valid_rr = None

    for rr in rr_intervals:
        # Remove physiologically implausible RR values
        if rr < min_rr_ms or rr > max_rr_ms:
            removed_count += 1
            continue

        # Correct likely missed beats by splitting unusually long intervals
        if previous_valid_rr is not None and rr > missed_beat_ratio * previous_valid_rr:
            half_rr = rr / 2

            if min_rr_ms <= half_rr <= max_rr_ms:
                cleaned_rr.extend([half_rr, half_rr])
                corrected_missed_beats += 1
                previous_valid_rr = half_rr
                continue

        cleaned_rr.append(rr)
        previous_valid_rr = rr

    return {
        "cleaned_rr": cleaned_rr,
        "raw_count": len(rr_intervals),
        "cleaned_count": len(cleaned_rr),
        "removed_count": removed_count,
        "corrected_missed_beats": corrected_missed_beats,
    }


def rr_to_heart_rate(rr_intervals: List[float]) -> List[float]:
    """
    Convert RR intervals in milliseconds to heart rate in beats per minute.

    Parameters
    ----------
    rr_intervals : List[float]
        RR interval values in milliseconds.

    Returns
    -------
    List[float]
        Heart rate values in beats per minute.
    """
    rr_array = np.array(rr_intervals, dtype=float)

    return (60000 / rr_array).tolist()
