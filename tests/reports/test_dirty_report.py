import os
from pathlib import Path
from tempfile import TemporaryDirectory

import pytest
from git import Repo

from git_inspector.reports.dirty import get_dirty_report


@pytest.fixture
def clean_repo():
    with TemporaryDirectory() as directory:
        repo = Repo.init(os.path.join(directory, 'first_repo'))
        yield repo


@pytest.fixture
def one_file_repo():
    with TemporaryDirectory() as directory:
        repo_directory = os.path.join(directory, 'first_repo')
        repo = Repo.init(repo_directory)
        tracked_file = os.path.join(repo_directory, 'tracked_file')
        Path(tracked_file).touch()
        repo.index.add(["."])
        repo.index.commit("initial commit")
        yield repo, tracked_file


def test_return_none_on_clean_repo(clean_repo: Repo):
    report = get_dirty_report(clean_repo)
    assert report is None


def test_return_something_on_dirty_repo(one_file_repo: Repo):
    repo_dir, tracked_file = one_file_repo
    with open(tracked_file, "w") as f:
        f.write("changed")
    report = get_dirty_report(repo_dir)
    assert report is not None
