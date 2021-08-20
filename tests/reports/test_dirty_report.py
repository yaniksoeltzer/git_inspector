import os
from pathlib import Path
from tempfile import TemporaryDirectory

import pytest
from git import Repo

from git_inspector.reports.dirty import get_dirty_report
from tests.reports.common import create_clean_repo, create_one_file_repo


@pytest.fixture
def clean_repo():
    with create_clean_repo() as repo:
        yield repo


@pytest.fixture
def one_file_repo():
    with create_one_file_repo() as (repo, file):
        yield repo, file


def test_return_none_on_clean_repo(clean_repo: Repo):
    report = get_dirty_report(clean_repo)
    assert report is None


def test_return_something_on_dirty_repo(one_file_repo: Repo):
    repo_dir, tracked_file = one_file_repo
    with open(tracked_file, "w") as f:
        f.write("changed")
    report = get_dirty_report(repo_dir)
    assert report is not None
