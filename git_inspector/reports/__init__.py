from git_inspector.reports.dirty import get_dirty_report
from git_inspector.reports.git_report import *
from git_inspector.reports.merged_branches import get_merged_branches_report
from git_inspector.reports.unpushed import get_unpushed_branches_report
from git_inspector.reports.untracked_branches import get_untracked_branches_report


def get_git_reports(repos):
    reports = [
        get_unpushed_branches_report(repos),
        get_untracked_branches_report(repos)
    ]
    for repo in repos:
        reports.append(get_dirty_report(repo))
        reports.append(get_merged_branches_report(repo))
    return [r for r in reports if r is not None]
