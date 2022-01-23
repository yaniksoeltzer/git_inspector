from git import Repo

from src.git_inspector.common import is_ahead_of
from tests.testutils import add_ahead_branch


def test_same_commit(repo: Repo):
    assert not is_ahead_of(
        repo=repo,
        ancestor=repo.commit("HEAD"),
        commit=repo.commit("HEAD"))


def test_direct_ancestor(repo: Repo):
    assert is_ahead_of(
        repo=repo,
        ancestor=repo.commit("HEAD~1"),
        commit=repo.commit("HEAD"))


def test_direct_successor(repo: Repo):
    assert not is_ahead_of(
        repo=repo,
        ancestor=repo.commit("HEAD"),
        commit=repo.commit("HEAD~1"))


def test_distant_ancestor(repo: Repo):
    assert is_ahead_of(
        repo=repo,
        ancestor=repo.commit("HEAD~2"),
        commit=repo.commit("HEAD"))


def test_distant_successor(repo: Repo):
    assert not is_ahead_of(
        repo=repo,
        ancestor=repo.commit("HEAD"),
        commit=repo.commit("HEAD~2"))


def test_ahead_branch(repo: Repo):
    ahead_branch = add_ahead_branch(repo)
    assert is_ahead_of(
        repo=repo,
        ancestor=repo.commit("HEAD"),
        commit=ahead_branch.commit
    )


def test_behind_branch(repo: Repo):
    ahead_branch = add_ahead_branch(repo)
    assert not is_ahead_of(
        repo=repo,
        ancestor=ahead_branch.commit,
        commit=repo.commit("HEAD")
    )


def test_different_branches(repo: Repo):
    branch1 = add_ahead_branch(repo, "branch1")
    branch2 = add_ahead_branch(repo, "branch2")
    assert is_ahead_of(
        repo=repo,
        ancestor=branch1.commit,
        commit=branch2.commit
    )
