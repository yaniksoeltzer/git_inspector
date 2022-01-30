from git import Repo
from git_inspector import find_git_directories


def test_find_git_directories(repo: Repo):
    generator = find_git_directories(search_paths=[repo.working_dir])
    assert next(generator) == repo.working_dir
