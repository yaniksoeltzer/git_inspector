import os
from contextlib import contextmanager
from tempfile import TemporaryDirectory
from git import Repo
from git_inspector import inspect
from tests.testutils import *


@contextmanager
def test_setup():
    with TemporaryDirectory(prefix="projects_") as outer_directory:
        clean_repo_dir = os.path.join(outer_directory, 'clean_repo')
        create_repo(clean_repo_dir)

        dirty_repo_dir = os.path.join(outer_directory, 'dirty_repo')
        create_dirty_repo(dirty_repo_dir)

        yield outer_directory


if __name__ == '__main__':
    with test_setup() as directory:
        print(inspect([directory]))
