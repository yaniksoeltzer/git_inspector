from git_inspector.common import *
from git_inspector.reports.git_report import GitReport, GIT_REPORT_LEVEL_HINT


def get_merged_branches_report(repos):
    merged_heads = []
    for repo in repos:
        repo_merged_heads = get_merged_heads(repo)
        merged_heads.extend(repo_merged_heads)
    merged_branches_report = GitReport(
        'master_merged_branches',
        'branches merged into master',
        GIT_REPORT_LEVEL_HINT,
        [],
        merged_heads)
    return merged_branches_report


def get_merged_heads(repo):
    merged_heads = []
    master = get_master_branch(repo)
    if master:
        non_masters = get_non_master_branches(repo)
        for non_master in non_masters:
            depth = is_ancestors_of(ancestor=non_master.commit, commit=master.commit)
            if not depth:
                pass
            else:# depth >= 0:
                merged_heads.append(non_master)
    return merged_heads
