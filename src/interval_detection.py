
from typing import List, Dict, Any
import numpy as np
from scipy.signal import find_peaks


def smooth_signal(values: List[float], window_size: int = 15) -> np.ndarray:
    """
    Smooth a signal using a simple moving average.

    Parameters
    ----------
    values : List[float]
        Input signal values.
    window_size : int
        Size of the moving average window.

    Returns
    -------
    np.ndarray
        Smoothed signal.
    """
    values = np.array(values, dtype=float)

    if len(values) < window_size:
        return values

    kernel = np.ones(window_size) / window_size
    return np.convolve(values, kernel, mode="same")


def detect_hiit_peaks(
    heart_rate: List[float],
    expected_intervals: int = 5,
    min_distance: int = 180,
    prominence: float = 5.0,
    smoothing_window: int = 15
) -> Dict[str, Any]:
    """
    Detect high-intensity HIIT peaks from a heart rate signal.

    Parameters
    ----------
    heart_rate : List[float]
        Heart rate signal in beats per minute.
    expected_intervals : int
        Expected number of HIIT intervals.
    min_distance : int
        Minimum distance between peaks in beat indices.
    prominence : float
        Minimum peak prominence.
    smoothing_window : int
        Window size used for signal smoothing.

    Returns
    -------
    Dict[str, Any]
        Detected peak indices, peak heart rates, and smoothed signal.
    """
    smoothed_hr = smooth_signal(heart_rate, window_size=smoothing_window)

    peaks, properties = find_peaks(
        smoothed_hr,
        distance=min_distance,
        prominence=prominence
    )

    if len(peaks) > expected_intervals:
        # Select the most prominent peaks
        prominences = properties["prominences"]
        top_indices = np.argsort(prominences)[-expected_intervals:]
        peaks = peaks[top_indices]

    # Sort peaks chronologically
    peaks = np.sort(peaks)

    return {
        "peaks": peaks.tolist(),
        "peak_heart_rates": smoothed_hr[peaks].tolist(),
        "smoothed_heart_rate": smoothed_hr.tolist(),
        "num_peaks_detected": len(peaks)
    }
