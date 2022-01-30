from .broken_remote import get_remote_branch_is_gone_reports, broken_remote_report
from .report import *
from .dirty import dirty_report, get_dirty_reports
from .merged import get_merged_reports, merged_report
from .unpushed import get_unpushed_reports, unpushed_report
from .untracked import get_untracked_reports, untracked_report

REPORTS = [
    (get_dirty_reports, dirty_report),
    (get_merged_reports, merged_report),
    (get_unpushed_reports, unpushed_report),
    (get_untracked_reports, untracked_report),
    (get_remote_branch_is_gone_reports, broken_remote_report),
]
