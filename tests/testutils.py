import os
from contextlib import contextmanager
from pathlib import Path
from tempfile import TemporaryDirectory
from git import Repo


def create_repo(repo_directory) -> Repo:
    repo = Repo.init(repo_directory)
    repo.index.commit("initial commit")
    return repo


def create_dirty_repo(repo_directory):
    repo = create_repo(repo_directory)
    make_repo_dirty(repo)
    return repo


def make_repo_dirty(repo: Repo):
    tracked_file = os.path.join(repo.working_dir, "tracked_file.txt")
    Path(tracked_file).touch()
    repo.index.add(["."])


def add_n_commits(repo:Repo, n_commits):
    for i in range(n_commits):
        repo.index.commit(f"commit-changed-{i}")


@contextmanager
def create_remote_and_local_repo():
    with TemporaryDirectory() as directory:
        remote_directory = os.path.join(directory, 'remote')
        remote_repo = create_repo(remote_directory)

        local_directory = os.path.join(directory, "local")
        local_repo = remote_repo.clone(local_directory)
        yield remote_repo, local_repo
