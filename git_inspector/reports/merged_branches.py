from git_inspector.common import *
from git_inspector.reports.report import Report


class MergedBranchesRepoReport(Report):
    def __init__(self, repo):
        self.repo = repo
        self.merged_heads = []
        master = get_master_branch(repo)
        if master:
            non_masters = get_non_master_branches(repo)
            for non_master in non_masters:
                cmp = compare_commits(master.commit, non_master.commit)
                if cmp and cmp >= 0:
                    self.merged_heads.append(non_master)

    def number_of_warnings(self):
        return len(self.merged_heads)

    def number_of_alerts(self):
        return 0

    def __str__(self):
        if len(self.merged_heads) == 0:
            return ""
        return "\n".join([
            f"     {self.repo.working_tree_dir}  {f'@{head}' if not is_master_branch(head) else ''}" for head in
            self.merged_heads
        ])


class MergedBranchesReport(Report):
    merged_branches_repo_reports = []

    def __init__(self, repos):
        for repo in repos:
            report = MergedBranchesRepoReport(repo)
            if str(report) != "":
                self.merged_branches_repo_reports.append(report)

    def number_of_alerts(self):
        return 0

    def number_of_warnings(self):
        return sum([
            r.number_of_warnings()
            for r in self.merged_branches_repo_reports
        ])

    def __str__(self):
        if len(self.merged_branches_repo_reports) == 0:
            return ""
        return "merged branches:\n" + \
               "\n".join(map(str, self.merged_branches_repo_reports))
