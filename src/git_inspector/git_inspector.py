from git import Repo
from src.git_inspector import find_git_repositories
from src.git_inspector import format_git_reports
from src.git_inspector import get_reports


def inspect(paths):
    repo_file_names = find_git_repositories(search_paths=paths)
    repos = list(map(Repo, repo_file_names))
    reports = get_reports(repos)
    output = format_git_reports(reports, repos)
    return output
