from git_inspector.common import filter_dirty_repos


class SummaryReport:

    def __init__(self, repos):
        self.repo_cnt = len(repos)
        dirty_repos = filter_dirty_repos(repos)
        self.dirty_repo_cnt = len(dirty_repos)

    def __str__(self):
        summary_message = \
            f"{self.repo_cnt} git repositories found: " \
            f"{self.dirty_repo_cnt} have changes."

        if self.dirty_repo_cnt > 0:
            summary_message = "\033[1;31m" + summary_message
        else:
            summary_message = "\033[0;32m" + summary_message
        summary_message += "\033[0m"
        return summary_message
