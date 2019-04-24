class GitInspectorReport:
    def __init__(self, repos):
        self.dirty_report = DirtyReposReport(repos)
        self.summary_report = SummaryReport(repos)

    def __str__(self):
        return "\n".join(
            filter(lambda s: s != "", [
                str(self.dirty_report),
                str(self.summary_report),
            ]))


class DirtyReposReport:
    dirty_repo_paths = []

    def __init__(self, repos):
        dirty_repos = filter_dirty_repos(repos)
        self.dirty_repo_paths = list(
            map(lambda r: r.working_tree_dir, dirty_repos)
        )

    def __str__(self):
        if len(self.dirty_repo_paths) == 0:
            return ""
        return \
            f"dirty:\n" \
            + "\n".join(map(
                    lambda path: f"     {path}",
                    self.dirty_repo_paths
                ))


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


def filter_dirty_repos(repos):
    dirty_repos = filter(lambda x: x.is_dirty(), repos)
    return list(dirty_repos)
