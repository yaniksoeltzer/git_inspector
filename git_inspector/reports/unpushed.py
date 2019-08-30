import logging
from git import Repo
from git_inspector.common import get_tracked_heads, is_ancestors_of
from git_inspector.reports.git_report import GitReport, GIT_REPORT_LEVEL_WARNING


def get_unpushed_branches_report(repos):
    unpushed_heads = []
    for repo in repos:
        repo_merged_heads = get_unpushed_branches(repo)
        unpushed_heads.extend(repo_merged_heads)
    report = GitReport(
        'unpushed',
        'unpushed branches',
        GIT_REPORT_LEVEL_WARNING,
        [],
        unpushed_heads
    )
    return report


def get_unpushed_branches(repo:Repo):
    unpushed_heads = []
    tracked_heads = get_tracked_heads(repo)
    for head in tracked_heads:
        remote = head.tracking_branch()
        try:
            re = is_ancestors_of(ancestor=remote.commit, commit=head.commit)
            if re is None:
                pass
            elif re > 0:
                unpushed_heads.append(head)
        except ValueError:
            logging.warning(f"Error accessing {repo.working_dir}")
    return unpushed_heads

