from git import Repo
from git_inspector.find_git_repo import find_git_repositories
from git_inspector.reports import get_git_reports


def inspect_all(paths):
    repos = get_git_repos(paths)
    reports = get_git_reports(repos)
    return repos, reports


def get_git_repos(paths):
    repo_file_names = find_git_repositories(search_paths=paths)
    repos = map(Repo, repo_file_names)
    return list(repos)
