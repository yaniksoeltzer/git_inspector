from git import Repo, RemoteReference
from src.git_inspector import is_ancestors_of
from .report import ReportType, GIT_REPORT_LEVEL_WARNING, Report

unpushed_report = ReportType(
    'unpushed',
    'unpushed branches',
    GIT_REPORT_LEVEL_WARNING
)


def get_unpushed_report(repo):
    unpushed_branches = get_unpushed_branches(repo)
    if len(unpushed_branches) > 0:
        return Report(repo, unpushed_branches, unpushed_report)
    else:
        return None


def get_unpushed_branches(repo: Repo):
    unpushed_heads = []
    for head in repo.heads:
        remote: RemoteReference = head.tracking_branch()
        if remote is None:
            continue
        remote_commit = remote.commit
        local_commit = head.commit
        if remote_commit == local_commit:
            continue
        if is_ancestors_of(ancestor=remote_commit, commit=local_commit):
            unpushed_heads.append(head)
    return unpushed_heads
