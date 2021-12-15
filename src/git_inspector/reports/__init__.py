from .broken_remote import get_remote_branch_is_gone_report, broken_remote_report
from .report import *
from .dirty import get_dirty_report, dirty_report
from .merged import get_merged_report, merged_report
from .unpushed import get_unpushed_report, unpushed_report
from .untracked import get_untracked_report, untracked_report

REPORTS = [
    (get_dirty_report, dirty_report),
    (get_merged_report, merged_report),
    (get_unpushed_report, unpushed_report),
    (get_untracked_report, untracked_report),
    (get_remote_branch_is_gone_report, broken_remote_report),
]
