from git import Repo
from git_inspector.reports.untracked import get_untracked_report
from tests.testutils import add_ahead_branch


def test_return_something_on_local_repo(repo: Repo):
    report = get_untracked_report(repo)
    assert report is not None


def test_return_none_on_tracked_repo(cloned_repo):
    report = get_untracked_report(cloned_repo)
    assert report is None


def test_untracked_branch(cloned_repo: Repo):
    # The untracked branch should not be merged in master branch
    # therefore, we create a branch that is ahead of the master branch
    add_ahead_branch(cloned_repo, 'untracked_branch')
    report = get_untracked_report(cloned_repo)
    assert report is not None


def test_no_report_on_untracked_merged_repo(cloned_repo: Repo):
    cloned_repo.create_head('untracked_merged_branch', 'HEAD~1')
    report = get_untracked_report(cloned_repo)
    assert report is None
