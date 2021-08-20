from git_inspector.reports.git_report import GitReport, GIT_REPORT_LEVEL_ALERT


def get_dirt_repo_report(repos):
    dirty_repos = filter_dirty_repos(repos)
    report = GitReport(
        'dirty',
        'dirty repositories',
        GIT_REPORT_LEVEL_ALERT,
        dirty_repos,
        [])
    return report


def filter_dirty_repos(repos):
    dirty_repos = filter(lambda x: x.is_dirty(), repos)
    return list(dirty_repos)