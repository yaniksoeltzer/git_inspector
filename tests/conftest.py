import pytest
from tests.testutils import *
from tempfile import TemporaryDirectory


@pytest.fixture
def repo():
    with TemporaryDirectory() as directory:
        yield create_repo(directory)


@pytest.fixture
def dirty_repo():
    with TemporaryDirectory() as directory:
        yield create_dirty_repo(directory)


@pytest.fixture
def remote_repo():
    with TemporaryDirectory() as directory:
        yield create_repo(directory)


@pytest.fixture
def cloned_repo(remote_repo: Repo):
    with TemporaryDirectory() as directory:
        local_repo = remote_repo.clone(directory)
        yield local_repo
