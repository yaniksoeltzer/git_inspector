import os
from contextlib import contextmanager
from pathlib import Path
from tempfile import TemporaryDirectory

from git import Repo


@contextmanager
def create_clean_repo() -> Repo:
    with TemporaryDirectory() as directory:
        repo_directory = os.path.join(directory, 'first_repo')
        repo = Repo.init(repo_directory)
        yield repo


@contextmanager
def create_one_file_repo():
    with create_clean_repo() as repo:
        tracked_file = os.path.join(repo.working_dir, 'tracked_file')
        Path(tracked_file).touch()
        repo.index.add(["."])
        repo.index.commit("initial commit")
        yield repo, tracked_file


@contextmanager
def create_thick_one_file_repo(n_commits):
    with create_one_file_repo() as (repo, tracked_file):
        for i in range(n_commits):
            with open(tracked_file, "w") as f:
                f.write(f"changed {i} times")
            repo.index.commit(f"commit-changed-{i}")
        yield repo, tracked_file
