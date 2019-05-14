from git_inspector.common import *
from git_inspector.reports.git_report import GitReport, GIT_REPORT_LEVEL_INFO


def get_merged_heads(repo):
    merged_heads = []
    master = get_master_branch(repo)
    if master:
        non_masters = get_non_master_branches(repo)
        for non_master in non_masters:
            cmp = compare_commits(master.commit, non_master.commit)
            if cmp and cmp >= 0:
                merged_heads.append(non_master)
    return merged_heads


def get_merged_branches_report(repos):
    merged_heads = []
    for repo in repos:
        repo_merged_heads = get_merged_heads(repo)
        merged_heads.extend(repo_merged_heads)
    merged_branches_report = GitReport(
        'merged_branches',
        'merged branches',
        GIT_REPORT_LEVEL_INFO,
        [],
        merged_heads)
    return merged_branches_report
