from git import Repo
from git_inspector.py_find import find_git_repository_paths
from git_inspector.report import GitInspectorReport


def inspect_all():
    repos = get_git_repos()
    report = GitInspectorReport(repos)
    print(report)


def get_git_repos():
    repo_file_names = find_git_repository_paths("/")
    repos = map(Repo, repo_file_names)
    return list(repos)
