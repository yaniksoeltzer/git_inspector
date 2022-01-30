from typing import List

from git import Repo

from ..common import (
    get_master_branch,
    get_non_master_branches,
    is_ancestors_of,
    is_ahead_of,
)
from .report import ReportType, Report, GIT_REPORT_LEVEL_HINT

merged_report = ReportType(
    "master_merged_branches", "branches merged into master", GIT_REPORT_LEVEL_HINT
)


def get_merged_reports(repo: Repo) -> List[Report]:
    merged_heads = get_merged_heads(repo)
    reports = [
        Report(
            repo=repo.working_dir,
            additional_info={"branch": merged_head.name},
            report_type=merged_report,
        )
        for merged_head in merged_heads
    ]
    return reports


def get_merged_heads(repo):
    merged_heads = []
    master = get_master_branch(repo)
    if master:
        non_masters = get_non_master_branches(repo)
        for non_master in non_masters:
            is_merged = not is_ahead_of(repo, master, non_master)
            if is_merged:
                merged_heads.append(non_master)
    return merged_heads
