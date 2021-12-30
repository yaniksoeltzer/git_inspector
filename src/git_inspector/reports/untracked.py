from git import Repo

from .merged import get_merged_heads
from ..common import get_untracked_heads

from .report import Report, ReportType, GIT_REPORT_LEVEL_WARNING

untracked_report = ReportType(
    'untracked',
    'untracked branches',
    GIT_REPORT_LEVEL_WARNING
)


def get_untracked_report(repo):
    untracked_branches = get_untracked_branches(repo)
    merged_branches = get_merged_heads(repo)
    untracked_branches = [
        b for b in untracked_branches if b not in merged_branches
    ]
    branch_names = [h.name for h in untracked_branches]
    if len(branch_names) > 0:
        return Report(repo.working_dir, branch_names, None, untracked_report)
    else:
        return None


def get_untracked_branches(repo: Repo):
    untracked_heads = get_untracked_heads(repo)
    return untracked_heads

