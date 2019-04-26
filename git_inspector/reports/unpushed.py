from git_inspector.common import get_tracked_heads, compare_commits
from git_inspector.reports.report import Report


class UnpushedRemotesOfRepoReport(Report):
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
                # self.unpushed_heads.append((head, "error"))
                pass
                # print("error with ", head, remote)

    def number_of_alerts(self):
        return 0

    def number_of_warnings(self):
        return len(self.unpushed_heads)

    def __str__(self):
        if len(self.unpushed_heads) == 0:
            return ""
        return "\n".join([
            f"     {self.repo.working_tree_dir}  {f'@{head}' if str(head) != 'master' else ''}" for head, re in
            self.unpushed_heads
        ])


class UnpushedRemotesReport(Report):
    unpushed_repo_reports = []

    def __init__(self, repos):
        for repo in repos:
            self.unpushed_repo_reports.append(
                UnpushedRemotesOfRepoReport(repo)
            )

    def number_of_alerts(self):
        return 0

    def number_of_warnings(self):
        return sum(map(lambda x:x.number_of_warnings(),self.unpushed_repo_reports))

    def __str__(self):
        if len(self.unpushed_repo_reports) == 0:
            return ""
        return "unpushed remotes:\n" + \
               "\n".join([
                   str(unpushed_repo_report)
                   for unpushed_repo_report in self.unpushed_repo_reports if str(unpushed_repo_report) != ""
               ])
