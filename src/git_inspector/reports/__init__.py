from .report import *
from .dirty import get_dirty_report
from .merged import get_merged_report
from .unpushed import get_unpushed_report
from .untracked import get_untracked_report


def get_reports(repos):
    reports = []
    for repo in repos:
        reports.append(get_dirty_report(repo))
        reports.append(get_merged_report(repo))
        reports.append(get_unpushed_report(repo))
        reports.append(get_untracked_report(repo))
    return [r for r in reports if r is not None]
