from git import Repo
from git_inspector.reports.untracked import get_untracked_report


def test_return_something_on_local_repo(repo: Repo):
    report = get_untracked_report(repo)
    assert report is not None


def test_return_none_on_tracked_repo(cloned_repo):
    report = get_untracked_report(cloned_repo)
    assert report is None


def test_multiple_braches(remote_repo, cloned_repo):
    n_tracked_branches = 3
    n_untracked_branches = 4
    origin = cloned_repo.remotes.origin

    for i in range(n_tracked_branches):
        # create emote ranches
        remote_branch_name = f'remote_tracked_{i}'
        remote_repo.create_head(remote_branch_name)
        origin.fetch()
        # create local branches
        local_branch_name = f'tracked_{i}'
        lb = cloned_repo.create_head(local_branch_name)
        lb.set_tracking_branch(origin.refs[remote_branch_name])

    for i in range(n_untracked_branches):
        local_branch_name = f'untracked_{i}'
        cloned_repo.create_head(local_branch_name)
    report = get_untracked_report(cloned_repo)
    assert report is not None
    assert report.branches is not None
    assert len(report.branches) == n_untracked_branches
