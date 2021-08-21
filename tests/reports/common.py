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
        repo.index.commit("initial commit")
        yield repo


@contextmanager
def create_one_file_repo(filename="tracked_file.txt"):
    with create_clean_repo() as repo:
        tracked_file = os.path.join(repo.working_dir, filename)
        Path(tracked_file).touch()
        repo.index.add(["."])
        repo.index.commit("added a file")
        yield repo, tracked_file


@contextmanager
def create_repo_with_n_commits(n_commits):
    with create_clean_repo() as repo:
        for i in range(n_commits):
            repo.index.commit(f"commit-changed-{i}")
        yield repo


@contextmanager
def create_remote_and_local_repo():
    with TemporaryDirectory() as directory:
        remote_directory = os.path.join(directory, 'remote')
        remote_repo = Repo.init(remote_directory)
        remote_repo.index.commit(f"initial commit")

        local_directory = os.path.join(directory, "local")
        local_repo = remote_repo.clone(local_directory)
        yield remote_repo, local_repo
