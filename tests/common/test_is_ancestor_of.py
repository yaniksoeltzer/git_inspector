from git import Repo
from git_inspector.common import is_ancestors_of

from tests.testutils import add_ahead_branch


def test_same_commit(repo: Repo):
    assert is_ancestors_of(
        ancestor=repo.commit("HEAD"),
        commit=repo.commit("HEAD"))


def test_direct_ancestor(repo: Repo):
    assert is_ancestors_of(
        ancestor=repo.commit("HEAD~1"),
        commit=repo.commit("HEAD"))


def test_reverse_direct_ancestor(repo: Repo):
    assert not is_ancestors_of(
        ancestor=repo.commit("HEAD"),
        commit=repo.commit("HEAD~1"))


def test_distant_ancestor(repo: Repo):
    assert is_ancestors_of(
        ancestor=repo.commit("HEAD~2"),
        commit=repo.commit("HEAD"))


def test_ahead_branch(repo: Repo):
    ahead_branch = add_ahead_branch(repo)
    assert is_ancestors_of(
        ancestor=repo.commit("HEAD"),
        commit=ahead_branch.commit
    )
    assert not is_ancestors_of(
        ancestor=ahead_branch.commit,
        commit=repo.commit("HEAD")
    )
