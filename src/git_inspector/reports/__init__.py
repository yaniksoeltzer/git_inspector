import traceback
from git import Repo

from .report import *
from .dirty import get_dirty_report, dirty_report
from .merged import get_merged_report, merged_report
from .unpushed import get_unpushed_report, unpushed_report
from .untracked import get_untracked_report, untracked_report
from ..exceptions import FailedToGenerateReport

REPORTS = [
    (get_dirty_report, dirty_report),
    (get_merged_report, merged_report),
    (get_unpushed_report, unpushed_report),
    (get_untracked_report, untracked_report),
]


def get_reports(repo: Repo):
    for get_report, report_type in REPORTS:
        try:
            report = get_report(repo)
        except Exception as e:
            raise FailedToGenerateReport(repo, report_type, e, traceback.format_exc())
        if report is not None:
            yield report
