from typing import NamedTuple

from git import Repo


class GitInspectorReport:
    def __init__(self, repos):
        self.dirty_report = DirtyReposReport(repos)
        self.unpushed_report = UnpushedRemotesReport(repos)
        self.summary_report = SummaryReport(repos)

    def __str__(self):
        return "\n".join(
            filter(lambda s: s != "", [
                str(self.dirty_report),
                str(self.unpushed_report),
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


def get_tracked_heads(repo):
    return list(filter(
        lambda head: head.tracking_branch() is not None,
        repo.heads
    ))


def compare_commits(commit_1, commit_2):
    if commit_1.hexsha == commit_2.hexsha:
        return 0
    com_1_parent_hex = [p.hexsha for p in commit_1.parents]
    if commit_2.hexsha in com_1_parent_hex:
        return 1
    com_2_parent_hex = [p.hexsha for p in commit_2.parents]
    if commit_1.hexsha in com_2_parent_hex:
        return -1
    return None


class UnpushedRemotesOfRepoReport:
    def __init__(self, repo):
        self.repo = repo
        self.unpushed_heads = []

        tracked_heads = get_tracked_heads(repo)
        for head in tracked_heads:
            remote = head.tracking_branch()
            try:
                re = compare_commits(head.commit, remote.commit)
                if not re:
                    pass
                elif re > 0:
                    self.unpushed_heads.append((head, "before"))
                elif re < 0:
                    pass
            except ValueError:
                #self.unpushed_heads.append((head, "error"))
                pass
                #print("error with ", head, remote)

    def __str__(self):
        if len(self.unpushed_heads) == 0:
            return ""
        return "\n".join([
            f"     {self.repo.working_tree_dir}  {f'@{head}' if str(head) != 'master' else ''}" for head, re in self.unpushed_heads
        ])

class UnpushedRemotesReport:

    unpushed_repo_reports = []
    def __init__(self, repos):
        for repo in repos:
            self.unpushed_repo_reports.append(
                UnpushedRemotesOfRepoReport(repo)
            )
    def __str__(self):
        if len(self.unpushed_repo_reports) == 0:
            return ""
        return "unpushed remotes:\n" +\
               "\n".join([
            str(unpushed_repo_report)
            for unpushed_repo_report in self.unpushed_repo_reports if str(unpushed_repo_report) != ""
        ])


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
