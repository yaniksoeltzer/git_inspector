from git import Repo
from src.git_inspector import get_untracked_heads

from .report import Report, ReportType, GIT_REPORT_LEVEL_WARNING

untracked_report = ReportType(
    'untracked',
    'untracked branches',
    GIT_REPORT_LEVEL_WARNING
)


def get_untracked_report(repo):
    untracked_branches = get_untracked_branches(repo)
    if len(untracked_branches) > 0:
        return Report(repo, untracked_branches, untracked_report)
    else:
        return None


def get_untracked_branches(repo: Repo):
    untracked_heads = get_untracked_heads(repo)
    return untracked_heads

