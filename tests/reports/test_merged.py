from tempfile import TemporaryDirectory

import pytest
from git import Repo

from git_inspector.reports.merged import get_merged_report
from tests.testutils import create_clean_repo, add_n_commits


@pytest.fixture
def clean_repo():
    with TemporaryDirectory() as directory:
        yield create_clean_repo(directory)


@pytest.fixture
def thick_repo():
    with TemporaryDirectory() as directory:
        repo = create_clean_repo(directory)
        add_n_commits(repo, 10)
        yield repo


def test_return_none_on_clean_repo(clean_repo: Repo):
    report = get_merged_report(clean_repo)
    assert report is None


def test_return_something_on_merged_branch_repo(thick_repo: Repo):
    thick_repo.create_head('merged_branch', 'HEAD~3')
    report = get_merged_report(thick_repo)
    assert report is not None
