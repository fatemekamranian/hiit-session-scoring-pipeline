# HIIT Session Scoring Project

## Overview
This project processes HRM files and scores HIIT training sessions based on whether the participant reaches target heart rate zones during high-intensity intervals.

The solution is implemented as a modular and reusable pipeline that can be applied to new HRM datasets without modification.

---

## Key Results
- Total sessions: 31
- Valid sessions: 24
- Invalid sessions: 7

Invalid sessions:
- 4 sessions with no RR data
- 3 sessions that were too short

Score distribution (valid sessions):
- Score 1: 2
- Score 2: 6
- Score 3: 8
- Score 4: 6
- Score 5: 2

---

## Method Summary
Pipeline steps:

Parse → Validate → Clean → Convert → Detect Peaks → Compute Zone → Score

- Extract RR intervals from HRM files
- Identify and exclude invalid sessions
- Handle artifacts (implausible values and missed beats)
- Convert RR intervals to heart rate
- Detect five high-intensity intervals
- Score sessions based on target heart rate zones

---

## Output
The project produces CSV files containing both results and diagnostic information.

Main fields:
- file_name
- date
- week
- score
- is_valid
- reason

Additional diagnostic fields:
- file_path
- max_hr
- rr_count_raw
- cleaned_rr_count
- removed_rr_count
- corrected_missed_beats
- target_zone_low
- target_zone_high
- num_peaks_detected

---

## How to Run
1. Place HRM files in the data directory
2. Open the notebook
3. Run all cells

Outputs will be saved in the `outputs/` folder.

---

## Project Structure
- hiit_session_scoring_pipeline.ipynb → main pipeline
- src/ → modular implementation
- outputs/ → CSV results
- reports/ → project report

---

## Report
A detailed explanation is available in:

reports/hiit_report.md
