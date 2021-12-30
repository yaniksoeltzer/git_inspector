from git import Repo
from git_inspector.common import is_ancestors_of


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
