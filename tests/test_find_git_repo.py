import os
from tempfile import TemporaryDirectory
from git import Repo
from git_inspector.find_git_repo import find_git_repositories


def test_empty_directory():
    with TemporaryDirectory() as directory:
        repo_paths = find_git_repositories(search_paths=[directory], excluded_dirs=[])
        repo_paths = [r for r in repo_paths]
    assert len(repo_paths) == 0


def test_single_repo():
    with TemporaryDirectory() as directory:
        repo_path = os.path.join(directory, 'first_repo')
        Repo.init(repo_path)
        repo_paths = find_git_repositories(search_paths=[directory], excluded_dirs=[])
        repo_paths = [r for r in repo_paths]
        assert len(repo_paths) == 1
        assert repo_paths[0] == repo_path


def test_multiple_repos():
    number_of_repos = 10
    with TemporaryDirectory() as directory:
        for i in range(number_of_repos):
            Repo.init(os.path.join(directory, f'repo-{i}'))
        repo_paths = find_git_repositories(search_paths=[directory], excluded_dirs=[])
        repo_paths = [r for r in repo_paths]
    assert len(repo_paths) == number_of_repos


def test_nested_repos():
    with TemporaryDirectory() as directory:
        outer_repo_path = os.path.join(directory, 'outer-repo')
        inner_repo_path = os.path.join(outer_repo_path, 'inner-repo')
        Repo.init(outer_repo_path)
        Repo.init(inner_repo_path)
        repo_paths = find_git_repositories(search_paths=[directory], excluded_dirs=[])
        repo_paths = [r for r in repo_paths]
    assert len(repo_paths) == 2
    assert outer_repo_path in repo_paths
    assert inner_repo_path in repo_paths


def test_sub_directory_repos():
    with TemporaryDirectory() as outer_directory:
        inner_directory_path_1 = os.path.join(outer_directory, 'inner_dir_1')
        os.mkdir(inner_directory_path_1)
        inner_directory_path_2 = os.path.join(outer_directory, 'inner_dir_2')
        os.mkdir(inner_directory_path_2)

        Repo.init(os.path.join(outer_directory, 'outer'))
        Repo.init(os.path.join(inner_directory_path_1, 'inner-1'))
        Repo.init(os.path.join(inner_directory_path_2, 'inner-2'))
        repo_paths = find_git_repositories(search_paths=[outer_directory], excluded_dirs=[])
        repo_paths = [r for r in repo_paths]
    assert len(repo_paths) == 3
