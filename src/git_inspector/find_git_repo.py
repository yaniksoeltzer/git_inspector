import os
from git import Repo

from .config import EXCLUDED_DIRS


def find_repos(search_paths):
    git_path_generator = find_git_directories(search_paths=search_paths)
    git_repo_generator = map(Repo, git_path_generator)
    return git_repo_generator


def find_git_directories(search_paths, excluded_dirs=EXCLUDED_DIRS):
    for search_path in search_paths:
        if any([search_path.startswith(e) for e in excluded_dirs]):
            continue
        if search_path in excluded_dirs:
            continue
        for root, dirs, files in os.walk(search_path):
            if root in excluded_dirs:
                dirs[:] = []
            dirs[:] = [d for d in dirs if d not in excluded_dirs]
            if '.git' in dirs:
                yield root
