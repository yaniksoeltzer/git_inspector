from git_inspector.common import filter_dirty_repos


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
