
from pathlib import Path
from typing import Dict, List, Optional, Any


def parse_metadata(lines: List[str]) -> Dict[str, Optional[str]]:
    """
    Extract metadata from the [Params] section of an HRM file.

    Parameters
    ----------
    lines : List[str]
        Raw lines from the HRM file.

    Returns
    -------
    Dict[str, Optional[str]]
        Dictionary containing metadata fields such as date, start time, and max HR.
    """
    metadata = {}

    for line in lines:
        line = line.strip()

        # Stop reading metadata when another section starts
        if line.startswith("[") and line != "[Params]":
            break

        if "=" in line:
            key, value = line.split("=", 1)
            metadata[key.strip()] = value.strip() if value.strip() != "" else None

    return metadata


def extract_rr_intervals(lines: List[str]) -> List[int]:
    """
    Extract RR interval values from the [HRData] section.

    Parameters
    ----------
    lines : List[str]
        Raw lines from the HRM file.

    Returns
    -------
    List[int]
        RR interval values in milliseconds.
    """
    rr_intervals = []
    in_hrdata_section = False

    for line in lines:
        line = line.strip()

        if line == "[HRData]":
            in_hrdata_section = True
            continue

        if in_hrdata_section:
            if line == "":
                continue

            try:
                rr_intervals.append(int(line))
            except ValueError:
                # Ignore non-numeric lines in the HRData section
                continue

    return rr_intervals


def read_hrm_file(file_path: str) -> Dict[str, Any]:
    """
    Read an HRM file and extract metadata and RR intervals.

    Parameters
    ----------
    file_path : str
        Path to the HRM file.

    Returns
    -------
    Dict[str, Any]
        Parsed HRM content including file name, metadata, and RR intervals.
    """
    file_path = Path(file_path)

    with open(file_path, "r", encoding="utf-8", errors="ignore") as file:
        lines = file.readlines()

    metadata = parse_metadata(lines)
    rr_intervals = extract_rr_intervals(lines)

    return {
        "file_name": file_path.name,
        "file_path": str(file_path),
        "metadata": metadata,
        "rr_intervals": rr_intervals,
        "rr_count": len(rr_intervals),
    }
