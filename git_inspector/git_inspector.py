from git import Repo
from git_inspector.find_git_repo import find_git_repositories
from git_inspector.reports import get_reports


def inspect_all(paths):
    repo_file_names = find_git_repositories(search_paths=paths)
    repos = list(map(Repo, repo_file_names))
    reports = get_reports(repos)
    return repos, reports
