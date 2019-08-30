from git_inspector.reports.git_report import *
from git_inspector.reports.dirty import get_dirt_repo_report
from git_inspector.reports.merged_branches import get_merged_branches_report
from git_inspector.reports.unpushed import get_unpushed_branches_report
from git_inspector.reports.untracked_branches import get_untracked_branches_report


def get_git_reports(repos):
    reports = [
        get_dirt_repo_report(repos),
        get_merged_branches_report(repos),
        get_unpushed_branches_report(repos),
        get_untracked_branches_report(repos)
    ]
    return reports
