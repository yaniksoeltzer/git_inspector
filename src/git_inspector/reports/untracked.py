from typing import List

from git import Repo

from .merged import get_merged_heads
from ..common import get_untracked_heads, is_local_repo
from .report import Report, ReportType, GIT_REPORT_LEVEL_WARNING


untracked_report = ReportType(
    "untracked", "untracked branches", GIT_REPORT_LEVEL_WARNING
)


def get_untracked_reports(repo: Repo) -> List[Report]:
    if is_local_repo(repo):
        return []
    untracked_branches = get_untracked_branches(repo)
    merged_branches = get_merged_heads(repo)
    untracked_branches = [b for b in untracked_branches if b not in merged_branches]
    reports = [
        Report(
            repo=repo.working_dir,
            additional_info={"branch": untracked_branch.name},
            report_type=untracked_report,
        )
        for untracked_branch in untracked_branches
    ]
    return reports


def get_untracked_branches(repo: Repo):
    untracked_heads = get_untracked_heads(repo)
    return untracked_heads
