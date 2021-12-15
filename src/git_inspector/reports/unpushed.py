from git import Repo, RemoteReference
from ..common import is_ancestors_of, CommitResolveError, remote_is_gone
from .report import ReportType, GIT_REPORT_LEVEL_WARNING, Report

unpushed_report = ReportType(
    'unpushed',
    'unpushed branches',
    GIT_REPORT_LEVEL_WARNING
)


def get_unpushed_report(repo):
    unpushed_branches = get_unpushed_branches(repo)
    branch_names = [h.name for h in unpushed_branches]
    if len(unpushed_branches) > 0:
        return Report(repo.working_dir, branch_names, None, unpushed_report)
    else:
        return None


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
