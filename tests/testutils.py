import os
from pathlib import Path

import lorem as lorem
from git import Repo


def create_repo(repo_directory) -> Repo:
    repo = Repo.init(repo_directory)
    repo.index.commit("initial commit")
    repo.index.commit("second commit")
    repo.index.commit("third commit")
    return repo


def create_dirty_repo(repo_directory) -> Repo:
    repo = create_repo(repo_directory)
    make_repo_dirty(repo)
    return repo


def create_cloned_repo(repo_directory, remote_repo: Repo) -> Repo:
    return remote_repo.clone(repo_directory)


def make_repo_dirty(repo: Repo):
    tracked_file = os.path.join(repo.working_dir, "tracked_file.txt")
    Path(tracked_file).touch()
    repo.index.add(["."])


def add_n_commits(repo: Repo, n_commits):
    for i in range(n_commits):
        repo.index.commit(f"commit-changed-{i}")


def add_n_big_commits(repo: Repo, n_commits):
    FILENAME = "big_file.txt"
    for i in range(n_commits):
        with open(Path(repo.working_dir) / FILENAME , "w") as big_file:
            for i in range(100):
                big_file.write(lorem.paragraph())
        repo.index.add(FILENAME)
        repo.index.commit(f"commit-changed-{i}")


def add_tracked_branch(local_repo, remote_repo, prefix: str):
    # create remote branch
    remote_branch_name = f'remote_{prefix}'
    tb = remote_repo.create_head(remote_branch_name)
    origin = local_repo.remotes.origin
    origin.fetch()
    # create local branches
    local_branch_name = f'branch_{prefix}'
    lb = local_repo.create_head(local_branch_name)
    lb.set_tracking_branch(origin.refs[remote_branch_name])
    return lb, tb


def add_merged_branch(repo: Repo):
    repo.create_head('merged_branch', 'HEAD~1')


def add_ahead_branch(repo: Repo, name='ahead_branch'):
    repo.index.commit(f"new_branch_{name}")
    repo.create_head(name, 'HEAD')
    repo.active_branch.commit = repo.commit('HEAD~1')
    assert repo.active_branch.commit == repo.heads[name].commit.parents[0]
    return repo.heads[name]
