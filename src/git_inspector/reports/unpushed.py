from typing import List

from git import Repo, RemoteReference
from ..common import is_ancestors_of, CommitResolveError, remote_is_gone
from .report import ReportType, GIT_REPORT_LEVEL_WARNING, Report

unpushed_report = ReportType(
    'unpushed',
    'unpushed branches',
    GIT_REPORT_LEVEL_WARNING
)


def get_unpushed_reports(repo: Repo) -> List[Report]:
    unpushed_branches = get_unpushed_branches(repo)
    reports = [
        Report(
            repo=repo.working_dir,
            additional_info={
                'branch': unpushed_branch.name
            },
            report_type=unpushed_report,
        )
        for unpushed_branch in unpushed_branches
    ]
    return reports


def get_unpushed_branches(repo: Repo):
    unpushed_heads = []
    for head in repo.heads:
        remote_ref: RemoteReference = head.tracking_branch()
        if remote_ref is None:
            continue
        if not remote_ref.is_valid():
            continue
        remote_commit = remote_ref.commit
        local_commit = head.commit
        if remote_commit == local_commit:
            continue
        try:
            local_is_ahead_remote = is_ancestors_of(ancestor=remote_commit, commit=local_commit)
            if local_is_ahead_remote:
                unpushed_heads.append(head)
        except CommitResolveError:
            # Ignore heads that can not be resolved
            pass

    return unpushed_heads
