from git import Repo
from git_inspector.py_find import find_git_repository_paths
from git_inspector.reports import GitInspectorReport, Report


def inspect_all():
    repos = get_git_repos()
    report = GitInspectorReport(repos)
    print(report)
    exit_status = exit_status_for(report)
    exit(exit_status)


def exit_status_for(report: Report):
    if report.number_of_alerts() > 0:
        return 1
    else:
        return 0


def get_git_repos():
    repo_file_names = find_git_repository_paths("/")
    repos = map(Repo, repo_file_names)
    return list(repos)
