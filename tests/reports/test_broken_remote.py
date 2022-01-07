import shutil
from tempfile import TemporaryDirectory

import pytest
from git import Repo
from git_inspector.reports.broken_remote import get_remote_branch_is_gone_reports

from tests.testutils import create_cloned_repo, create_repo


@pytest.fixture
def master_gone_repo(remote_repo: Repo):
    with TemporaryDirectory() as directory:
        with TemporaryDirectory() as remote_directory:
            remote_repo = create_repo(remote_directory)
            cloned_repo = create_cloned_repo(
                repo_directory=directory,
                remote_repo=remote_repo
            )
            # ensure the directory is gone
            shutil.rmtree(remote_directory, )
        # remove remote by closing remote_directory
        yield cloned_repo


def test_return_none_on_clean_repo(repo: Repo):
    reports = get_remote_branch_is_gone_reports(repo)
    assert len(reports) == 0


def test_return_something_on_broken_remote(master_gone_repo: Repo):
    reports = get_remote_branch_is_gone_reports(master_gone_repo)
    assert len(reports) > 0


def test_contain_origin_on_broken_remote(master_gone_repo: Repo):
    reports = get_remote_branch_is_gone_reports(master_gone_repo)
    assert len(reports) == 1
    assert reports[0].additional_info['remote'] == 'origin'
