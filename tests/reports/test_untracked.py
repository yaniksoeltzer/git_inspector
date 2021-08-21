from tempfile import TemporaryDirectory

import pytest
from git import Repo

from git_inspector.reports.untracked import get_untracked_report
from tests.testutils import create_clean_repo, create_remote_and_local_repo


@pytest.fixture
def local_repo():
    with TemporaryDirectory() as directory:
        yield create_clean_repo(directory)


def test_return_something_on_local_repo(local_repo: Repo):
    report = get_untracked_report(local_repo)
    assert report is not None


def test_return_none_on_tracked_repo():
    with create_remote_and_local_repo() as (remote_repo, local_repo):
        report = get_untracked_report(local_repo)
    assert report is None


def test_multiple_braches():
    n_tracked_branches = 3
    n_untracked_branches = 4
    with create_remote_and_local_repo() as (remote_repo, local_repo):
        origin = local_repo.remotes.origin

        for i in range(n_tracked_branches):
            # create emote ranches
            remote_branch_name = f'remote_tracked_{i}'
            remote_repo.create_head(remote_branch_name)
            origin.fetch()
            # create local branches
            local_branch_name = f'tracked_{i}'
            lb = local_repo.create_head(local_branch_name)
            lb.set_tracking_branch(origin.refs[remote_branch_name])

        for i in range(n_untracked_branches):
            local_branch_name = f'untracked_{i}'
            local_repo.create_head(local_branch_name)
        report = get_untracked_report(local_repo)
    assert report is not None
    assert report.branches is not None
    assert len(report.branches) == n_untracked_branches
