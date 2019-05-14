from git_inspector.common import get_tracked_heads, compare_commits
from git_inspector.reports.git_report import GitReport, GIT_REPORT_LEVEL_WARNING

    def number_of_warnings(self):
        return len(self.unpushed_heads)

    def __str__(self):
        if len(self.unpushed_heads) == 0:
            return ""
        return "\n".join([
            f"     {self.repo.working_tree_dir}  {f'@{head}' if str(head) != 'master' else ''}" for head, re in
            self.unpushed_heads
        ])


class UnpushedRemotesReporter(Reporter):
    unpushed_repo_reports = []

    def __init__(self, repos):
        for repo in repos:
            report = UnpushedRemotesOfRepoReporter(repo)
            if str(report) != "":
                self.unpushed_repo_reports.append(report)

    def number_of_alerts(self):
        return 0

    def number_of_warnings(self):
        return sum(map(lambda x:x.number_of_warnings(),self.unpushed_repo_reports))

    def __str__(self):
        if len(self.unpushed_repo_reports) == 0:
            return ""
        return "unpushed remotes:\n" + \
               "\n".join(map(str, self.unpushed_repo_reports))

def get_unpushed_branches(repo):
    unpushed_heads = []
    tracked_heads = get_tracked_heads(repo)
    for head in tracked_heads:
        remote = head.tracking_branch()
        try:
            re = compare_commits(head.commit, remote.commit)
            if not re:
                pass
            elif re > 0:
                unpushed_heads.append(head)
            elif re < 0:
                pass
        except ValueError:
            # self.unpushed_heads.append((head, "error"))
            pass
            # print("error with ", head, remote)
    return unpushed_heads


def get_unpushed_branches_report(repos):
    unpushed_heads = []
    for repo in repos:
        repo_merged_heads = get_unpushed_branches(repo)
        unpushed_heads.extend(repo_merged_heads)
    report = GitReport(
        'unpushed',
        'unpushed branches',
        GIT_REPORT_LEVEL_WARNING,
        [],
        unpushed_heads
    )
    return report
