from git import Repo
from git_inspector.reports.untracked import get_untracked_report
from tests.testutils import add_tracked_branch


def test_return_something_on_local_repo(repo: Repo):
    report = get_untracked_report(repo)
    assert report is not None


def test_return_none_on_tracked_repo(cloned_repo):
    report = get_untracked_report(cloned_repo)
    assert report is None


def test_multiple_braches(remote_repo, cloned_repo):
    n_tracked_branches = 3
    n_untracked_branches = 4

    for i in range(n_tracked_branches):
        lb, _ = add_tracked_branch(
            local_repo=cloned_repo,
            remote_repo=remote_repo,
            prefix=f"{i}"
        )

    for i in range(n_untracked_branches):
        local_branch_name = f'untracked_{i}'
        cloned_repo.create_head(local_branch_name)
    report = get_untracked_report(cloned_repo)
    assert report is not None
    assert report.branches is not None
    assert len(report.branches) == n_untracked_branches
