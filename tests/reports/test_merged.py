import pytest
from git import Repo

from git_inspector.reports.merged import get_merged_report
from tests.reports.common import create_clean_repo, create_repo_with_n_commits


@pytest.fixture
def clean_repo():
    with create_clean_repo() as repo:
        yield repo


@pytest.fixture
def thick_repo():
    with create_repo_with_n_commits(10) as repo:
        yield repo


def test_return_none_on_clean_repo(clean_repo: Repo):
    report = get_merged_report(clean_repo)
    assert report is None


def test_return_something_on_merged_branch_repo(thick_repo: Repo):
    thick_repo.create_head('merged_branch', 'HEAD~3')
    report = get_merged_report(thick_repo)
    assert report is not None
