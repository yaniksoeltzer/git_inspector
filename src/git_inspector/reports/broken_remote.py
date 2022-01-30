from typing import List
from git import Repo

from .report import ReportType, Report, GIT_REPORT_LEVEL_WARNING
from ..common import remote_is_gone

broken_remote_report = ReportType(
    "broken_remote", "remote branch gone", GIT_REPORT_LEVEL_WARNING
)


def get_remote_branch_is_gone_reports(repo: Repo) -> List[Report]:
    reports = []
    for remote in repo.remotes:
        if remote_is_gone(remote):
            report = Report(
                repo=repo.working_dir,
                additional_info={"remote": remote.name},
                report_type=broken_remote_report,
            )
            reports.append(report)
    return reports


def get_tracked_branches(repo: Repo):
    return [
        (head, head.tracking_branch())
        for head in repo.heads
        if head.tracking_branch() is not None
    ]
