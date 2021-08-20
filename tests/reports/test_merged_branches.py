import os
from pathlib import Path
from tempfile import TemporaryDirectory

import pytest
from git import Repo

from git_inspector.reports.merged_branches import get_merged_branches_report
from tests.reports.common import create_clean_repo, create_thick_one_file_repo
from tests.reports.test_dirty_report import one_file_repo


@pytest.fixture
def clean_repo():
    with create_clean_repo() as repo:
        yield repo


@pytest.fixture
def thick_one_file_repo():
    with create_thick_one_file_repo(10) as (repo, tracked_file):
        yield repo, tracked_file


def test_return_none_on_clean_repo(clean_repo: Repo):
    report = get_merged_branches_report(clean_repo)
    assert report is None


def test_return_something_on_merged_branch_repo(thick_one_file_repo: Repo):
    repo, tracked_file = thick_one_file_repo
    repo.create_head('merged_branch', 'HEAD~3')
    report = get_merged_branches_report(repo)
    assert report is not None
