from tempfile import TemporaryDirectory
import pytest
from git import Repo
from git_inspector.reports.merged import get_merged_report
from tests.testutils import create_repo, add_n_commits, add_merged_branch


@pytest.fixture
def thick_repo():
    with TemporaryDirectory() as directory:
        repo = create_repo(directory)
        add_n_commits(repo, 10)
        yield repo


def test_return_none_on_clean_repo(repo: Repo):
    report = get_merged_report(repo)
    assert report is None


def test_return_something_on_merged_branch_repo(thick_repo: Repo):
    add_merged_branch(thick_repo)
    report = get_merged_report(thick_repo)
    assert report is not None
