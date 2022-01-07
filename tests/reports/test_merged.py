from git import Repo
from git_inspector.reports import get_merged_reports

from tests.testutils import add_merged_branch, add_ahead_branch


def test_return_none_on_clean_repo(repo: Repo):
    reports = get_merged_reports(repo)
    assert len(reports) == 0


def test_return_something_on_merged_branch_repo(repo: Repo):
    add_merged_branch(repo)
    reports = get_merged_reports(repo)
    assert len(reports) > 0


def test_ahead_branch(repo: Repo):
    add_ahead_branch(repo)
    reports = get_merged_reports(repo)
    assert len(reports) == 0
