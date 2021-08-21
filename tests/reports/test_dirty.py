from tempfile import TemporaryDirectory
import pytest
from git import Repo

from git_inspector.reports.dirty import get_dirty_report
from tests.testutils import create_clean_repo, create_dirty_repo


@pytest.fixture
def clean_repo():
    with TemporaryDirectory() as directory:
        yield create_clean_repo(directory)


@pytest.fixture
def dirty_repo():
    with TemporaryDirectory() as directory:
        yield create_dirty_repo(directory)


def test_return_none_on_clean_repo(clean_repo: Repo):
    report = get_dirty_report(clean_repo)
    assert report is None


def test_return_something_on_dirty_repo(dirty_repo: Repo):
    report = get_dirty_report(dirty_repo)
    assert report is not None
