from collections import Counter
from typing import List

from ..reports import GIT_REPORT_LEVEL_ALERT, GIT_REPORT_LEVEL_WARNING


def calculate_exit_code(reports):
    n_warnings = count_warnings(reports)
    exit_code = min(255, n_warnings)
    return exit_code


def count_warnings(reports):
    alert_level: List[int] = [r.report_type.alert_level for r in reports]
    counter = Counter(alert_level)
    warning_count = counter[GIT_REPORT_LEVEL_ALERT] + counter[GIT_REPORT_LEVEL_WARNING]
    return warning_count
