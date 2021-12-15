from ..common import get_master_branch, get_non_master_branches, is_ancestors_of
from .report import ReportType, Report, GIT_REPORT_LEVEL_HINT

merged_report = ReportType(
    'master_merged_branches',
    'branches merged into master',
    GIT_REPORT_LEVEL_HINT
)


def get_merged_report(repo):
    merged_heads = get_merged_heads(repo)
    branch_names = [h.name for h in merged_heads]
    if len(merged_heads) == 0:
        return None
    else:
        return Report(repo.working_dir, branch_names, None, merged_report)


def get_merged_heads(repo):
    merged_heads = []
    master = get_master_branch(repo)
    if master:
        non_masters = get_non_master_branches(repo)
        for non_master in non_masters:
            depth = is_ancestors_of(ancestor=non_master.commit, commit=master.commit)
            if depth is None:
                pass
            else:  # depth >= 0:
                merged_heads.append(non_master)
    return merged_heads
