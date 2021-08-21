import pytest
from git import Repo

from git_inspector.reports.unpushed import get_unpushed_report
from tests.reports.common import create_clean_repo, create_remote_and_local_repo


@pytest.fixture
def clean_repo():
    with create_clean_repo() as repo:
        yield repo


def test_return_none_on_local_repo(clean_repo: Repo):
    report = get_unpushed_report(clean_repo)
    assert report is None


def test_return_something_on_unpushed_repo():
    with create_remote_and_local_repo() as (remote_repo, local_repo):
        local_repo.index.commit("local-only-commit")
        report = get_unpushed_report(local_repo)
    assert report is not None


def test_multiple_up_to_date_branches():
    #
    # master -> origin/master
    # branch_1 -> origin/remote_1
    n_branches = 3
    with create_remote_and_local_repo() as (remote_repo, local_repo):
        origin = local_repo.remotes.origin

        for i in range(n_branches):
            # create emote ranches
            remote_branch_name = f'remote_{i}'
            remote_repo.create_head(remote_branch_name)
            origin.fetch()
            # create local branches
            local_branch_name = f'branch_{i}'
            lb = local_repo.create_head(local_branch_name)
            lb.set_tracking_branch(origin.refs[remote_branch_name])

        report = get_unpushed_report(local_repo)

    assert report is None


def test_multiple_branches():
    # master -> origin/master (up to date)
    # branch_{i} -> origin/remote_{i} (unpushed)
    n_branches = 3
    with create_remote_and_local_repo() as (remote_repo, local_repo):
        origin = local_repo.remotes.origin

        for i in range(n_branches):
            # create emote ranches
            remote_branch_name = f'remote_{i}'
            remote_repo.create_head(remote_branch_name)
            origin.fetch()
            # create local branches
            local_branch_name = f'branch_{i}'
            lb = local_repo.create_head(local_branch_name)
            lb.set_tracking_branch(origin.refs[remote_branch_name])

            # commit to local_branch
            lb.checkout()
            local_repo.index.commit(f"local only commit on {local_branch_name}")

        report = get_unpushed_report(local_repo)

    assert report is not None
    assert report.branches is not None
    assert len(report.branches) == n_branches


def test_outdated_branches():
    # commits on origin but not on local
    with create_remote_and_local_repo() as (remote_repo, local_repo):
        origin = local_repo.remotes.origin
        remote_repo.index.commit("remote only commit")
        origin.fetch()

        local = local_repo.heads.master
        remote = local.tracking_branch()
        assert local.commit != remote.commit

        report = get_unpushed_report(local_repo)

    assert report is None
