from git import Repo

from .report import ReportType, Report, GIT_REPORT_LEVEL_WARNING
from ..common import remote_is_gone

broken_remote_report = ReportType(
    'broken_remote',
    'remote branch gone',
    GIT_REPORT_LEVEL_WARNING
)


def get_remote_branch_is_gone_report(repo: Repo):
    gone_remotes = []
    for remote in repo.remotes:
        if remote_is_gone(remote):
            gone_remotes.append(remote.name)
    if len(gone_remotes) > 0:
        return Report(repo.working_dir, None, gone_remotes, broken_remote_report)
    else:
        return None


def get_tracked_branches(repo: Repo):
    return [(head, head.tracking_branch()) for head in repo.heads if head.tracking_branch() is not None]
