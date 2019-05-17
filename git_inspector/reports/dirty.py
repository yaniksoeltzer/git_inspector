from git_inspector.common import filter_dirty_repos
from git_inspector.reports.git_report import GitReport, GIT_REPORT_LEVEL_ALERT


def get_dirt_repo_report(repos):
    print("get_dirty_repos")
    dirty_repos = filter_dirty_repos(repos)
    report = GitReport(
        'dirty',
        'dirty repositories',
        GIT_REPORT_LEVEL_ALERT,
        dirty_repos,
        [])
    return report
