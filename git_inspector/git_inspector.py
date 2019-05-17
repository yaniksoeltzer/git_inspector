from git import Repo
from git_inspector.py_find import find_git_repository_paths
from git_inspector.report_formatter import format_git_reports
from git_inspector.reports import get_git_reports


def inspect_all():
    repos = get_git_repos()
    reports = get_git_reports(repos)
    formatted_str = format_git_reports(reports,repos)
    print(formatted_str)


def get_git_repos():
    repo_file_names = find_git_repository_paths("/")
    repos = map(Repo, repo_file_names)
    return list(repos)
