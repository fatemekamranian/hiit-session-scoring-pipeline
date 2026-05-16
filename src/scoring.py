
from typing import List, Dict, Any


def score_session(
    peak_heart_rates: List[float],
    target_zone: Dict[str, float]
) -> Dict[str, Any]:
    """
    Score a HIIT session based on how many detected peaks fall within the target heart rate zone.

    Parameters
    ----------
    peak_heart_rates : List[float]
        Heart rate values at detected HIIT peaks.
    target_zone : Dict[str, float]
        Dictionary containing lower and upper bounds of the target zone.

    Returns
    -------
    Dict[str, Any]
        Session score and per-peak pass/fail results.
    """
    low = target_zone["low"]
    high = target_zone["high"]

    interval_results = []

    for i, peak_hr in enumerate(peak_heart_rates, start=1):
        reached_target = low <= peak_hr <= high

        interval_results.append({
            "interval_number": i,
            "peak_heart_rate": peak_hr,
            "reached_target": reached_target
        })

    score = sum(result["reached_target"] for result in interval_results)

    return {
        "score": int(score),
        "max_score": len(peak_heart_rates),
        "interval_results": interval_results
    }
