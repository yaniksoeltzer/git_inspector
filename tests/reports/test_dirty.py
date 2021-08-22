from git import Repo
from src.git_inspector import get_dirty_report


def test_return_none_on_clean_repo(repo: Repo):
    report = get_dirty_report(repo)
    assert report is None


def test_return_something_on_dirty_repo(dirty_repo: Repo):
    report = get_dirty_report(dirty_repo)
    assert report is not None
