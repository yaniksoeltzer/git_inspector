from git_inspector.reports.dirty import get_dirty_report
from git_inspector.reports.merged import get_merged_report
from git_inspector.reports.unpushed import get_unpushed_report
from git_inspector.reports.untracked import get_untracked_report


def get_reports(repos):
    reports = []
    for repo in repos:
        reports.append(get_dirty_report(repo))
        reports.append(get_merged_report(repo))
        reports.append(get_untracked_report(repo))
        reports.append(get_unpushed_report(repo))
    return [r for r in reports if r is not None]
