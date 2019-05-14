from git_inspector.common import filter_dirty_repos
from git_inspector.reports.git_report import Reporter, GitReport, GIT_REPORT_LEVEL_ALERT


class DirtyReposReporter(Reporter):
    dirty_repo_paths = []

    def __init__(self, repos):
        dirty_repos = filter_dirty_repos(repos)
        self.dirty_repo_paths = list(
            map(lambda r: r.working_tree_dir, dirty_repos)
        )

    def number_of_alerts(self):
        return len(self.dirty_repo_paths)

    def number_of_warnings(self):
        return 0

    def __str__(self):
        if len(self.dirty_repo_paths) == 0:
            return ""
        return \
            f"dirty:\n" \
            + "\n".join(map(
                    lambda path: f"     {path}",
                    self.dirty_repo_paths
                ))



def get_dirt_repo_report(repos):
    dirty_repos = filter_dirty_repos(repos)
    report = GitReport(
        'dirty',
        'dirty repositories',
        GIT_REPORT_LEVEL_ALERT,
        dirty_repos,
        [])
    return report
