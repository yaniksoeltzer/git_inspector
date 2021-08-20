import os
from tempfile import TemporaryDirectory

import pytest
from git import Repo

from git_inspector.find_git_repo import find_git_repositories


# Directories
# outer
# - middle_1
#   * repo-a
# - middle_2
#   * repo-b
#   * repo-c
# - middle_3
#   - inner_1
#     * repo-d
#   - inner_2
#     * repo-e
#     * repo-f


@pytest.fixture
def test_setup():
    with TemporaryDirectory() as outer_directory:
        middle_1 = os.path.join(outer_directory, 'middle_1')
        os.mkdir(middle_1)
        repo_a = os.path.join(middle_1, 'repo-a')
        Repo.init(repo_a)

        middle_2 = os.path.join(outer_directory, 'middle_2')
        os.mkdir(middle_2)
        repo_b = os.path.join(middle_2, 'repo-b')
        Repo.init(repo_b)
        repo_c = os.path.join(middle_2, 'repo-c')
        Repo.init(repo_c)

        middle_3 = os.path.join(outer_directory, 'middle_3')
        os.mkdir(middle_3)

        inner_1 = os.path.join(middle_3, 'inner_1')
        os.mkdir(inner_1)
        repo_d = os.path.join(inner_1, 'repo-d')
        Repo.init(repo_d)

        inner_2 = os.path.join(middle_3, 'inner_2')
        os.mkdir(inner_2)
        repo_e = os.path.join(inner_2, 'repo-e')
        Repo.init(repo_e)
        repo_f = os.path.join(inner_2, 'repo-f')
        Repo.init(repo_f)

        yield outer_directory, {
            "repo-a": repo_a,
            "repo-b": repo_b,
            "repo-c": repo_c,
            "repo-d": repo_d,
            "repo-e": repo_e,
            "repo-f": repo_f,
            "middle_1": middle_1,
            "middle_2": middle_2,
            "middle_3": middle_3,
        }


def test_exclude_test_dir(test_setup):
    test_directory, paths = test_setup
    repo_paths = find_git_repositories(
        search_paths=[test_directory],
        excluded_dirs=[test_directory]
    )
    repo_paths = [r for r in repo_paths]
    assert len(repo_paths) == 0


def test_exclude_root_dir(test_setup):
    test_directory, paths = test_setup
    repo_paths = find_git_repositories(
        search_paths=[test_directory],
        excluded_dirs=["/"]
    )
    repo_paths = [r for r in repo_paths]
    assert len(repo_paths) == 0


def test_exclude_git_repo(test_setup):
    test_directory, paths = test_setup
    repo_paths = find_git_repositories(
        search_paths=[test_directory],
        excluded_dirs=[paths["repo-a"]]
    )
    repo_paths = [r for r in repo_paths]
    assert paths["repo-a"] not in repo_paths
    assert len(repo_paths) == 5


def test_absolute_directory(test_setup):
    test_directory, paths = test_setup
    repo_paths = find_git_repositories(
        search_paths=[test_directory],
        excluded_dirs=[paths["middle_1"]]
    )
    repo_paths = [r for r in repo_paths]
    assert paths["repo-a"] not in repo_paths
    assert len(repo_paths) == 5


def test_exclude_directory_name(test_setup):
    test_directory, paths = test_setup
    repo_paths = find_git_repositories(
        search_paths=[test_directory],
        excluded_dirs=["middle_1"]
    )
    repo_paths = [r for r in repo_paths]
    assert paths["repo-a"] not in repo_paths
    assert len(repo_paths) == 5
