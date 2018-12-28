import random

from git_inspector.py_find import get_git_repository_paths
from git import Repo, Remote,Commit


def inspect_all():
    repo_file_names = get_git_repository_paths("/")
    repos = [Repo(filename) for filename in repo_file_names]
    message = information_message(repos)
    print(message)


def information_message(repos):
    dirty_repos = [repo for repo in repos if repo.is_dirty()]
    dirty_repos_messages = [
        "dirty: {path}".format(
            path=repo.git_dir
        )
        for repo in dirty_repos]
    dirty_repos_message = "\n".join(dirty_repos_messages)

    summary_message = "{count_total} git repositories found: " \
              "{count_dirty} have changes.".format(
        count_total=len(repos),
        count_dirty=len(dirty_repos),
    )
    message = ""
    message += dirty_repos_message+("\n" if dirty_repos_message else "")
    message += summary_message
    return message
