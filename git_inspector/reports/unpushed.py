from git_inspector.common import get_tracked_heads, compare_commits
from git_inspector.reports.git_report import GitReport, GIT_REPORT_LEVEL_WARNING


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
