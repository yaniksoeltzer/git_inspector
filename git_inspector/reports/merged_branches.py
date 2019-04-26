from git_inspector.common import *


class MergedBranchesRepoReport:
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

    def __str__(self):
        if len(self.merged_heads) == 0:
            return ""
        return "\n".join([
            f"     {self.repo.working_tree_dir}  {f'@{head}' if not is_master_branch(head) else ''}" for head in
            self.merged_heads
        ])


class MergedBranchesReport:
    merged_branches_repo_reports = []

    def __init__(self, repos):
        for repo in repos:
            self.merged_branches_repo_reports.append(
                MergedBranchesRepoReport(repo)
            )

    def __str__(self):
        if len(self.merged_branches_repo_reports) == 0:
            return ""
        return "merged branches:\n" + \
               "\n".join([
                   str(merged_branches_repo_report)
                   for merged_branches_repo_report in self.merged_branches_repo_reports
                   if str(merged_branches_repo_report) != ""
               ])
