
from git import Repo
from git_inspector import find_git_directories, get_reports


def test_find_git_directories(repo: Repo):
    generator = find_git_directories(search_paths=[repo.working_dir])
    assert next(generator) == repo.working_dir


def test_get_reports(dirty_repo: Repo):
    reports = get_reports([dirty_repo, dirty_repo])
    assert next(reports) is not None
    assert next(reports) is not None


