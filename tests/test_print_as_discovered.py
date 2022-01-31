from git import Repo
from git_inspector import find_git_directories


def test_find_single_git_directory(repo: Repo):
    generator = find_git_directories(
        search_paths=[repo.working_dir], excluded_dir_selectors=[]
    )
    working_dirs = list(generator)
    assert len(working_dirs) == 1
    assert working_dirs[0] == repo.working_dir
