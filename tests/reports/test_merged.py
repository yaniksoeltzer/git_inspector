from git import Repo
from git_inspector.reports import get_merged_report
from tests.testutils import add_merged_branch


def test_return_none_on_clean_repo(repo: Repo):
    report = get_merged_report(repo)
    assert report is None


def test_return_something_on_merged_branch_repo(ten_commits_repo: Repo):
    add_merged_branch(ten_commits_repo)
    report = get_merged_report(ten_commits_repo)
    assert report is not None
