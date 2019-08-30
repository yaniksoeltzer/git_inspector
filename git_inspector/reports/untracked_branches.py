import logging
from git import Repo
from git_inspector.common import get_tracked_heads, is_ancestors_of, get_untracked_heads
from git_inspector.reports.git_report import GitReport, GIT_REPORT_LEVEL_WARNING


def get_untracked_branches_report(repos):
    untracked_heads = []
    for repo in repos:
        repo_untracked_heads = get_untracked_branches(repo)
        untracked_heads.extend(repo_untracked_heads)
    report = GitReport(
        'untracked',
        'untracked branches',
        GIT_REPORT_LEVEL_WARNING,
        [],
        untracked_heads
    )
    return report


def get_untracked_branches(repo: Repo):
    untracked_heads = get_untracked_heads(repo)
    return untracked_heads

