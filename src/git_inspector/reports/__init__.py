from .report import *
from .dirty import get_dirty_report
from .merged import get_merged_report
from .unpushed import get_unpushed_report
from .untracked import get_untracked_report

REPORT_FUNCTIONS = [
    get_dirty_report,
    get_merged_report,
    get_unpushed_report,
    get_untracked_report,
]


def get_reports(repos):
    for repo in repos:
        for get_report in REPORT_FUNCTIONS:
            report = get_report(repo)
            if report is not None:
                yield report
