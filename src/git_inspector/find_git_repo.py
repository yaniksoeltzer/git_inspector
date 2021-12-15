import logging
import os
from git import Repo

from .config import EXCLUDED_DIR_SELECTORS


def find_repos(absolute_search_paths):
    git_path_generator = find_git_directories(search_paths=absolute_search_paths)
    git_repo_generator = map(Repo, git_path_generator)
    return git_repo_generator


def find_git_directories(search_paths, excluded_dir_selectors=EXCLUDED_DIR_SELECTORS):
    absolute_excluded_dirs = \
        [d for d in excluded_dir_selectors if d.startswith("/")] \
        + [os.path.expanduser(d) for d in excluded_dir_selectors if d.startswith("~")]
    dir_selector = [d for d in excluded_dir_selectors if not d.startswith("~") and not d.startswith("/")]
    absolute_search_paths = [os.path.abspath(p) for p in search_paths]
    logging.error(absolute_excluded_dirs)
    for search_path in absolute_search_paths:
        for root, dirs, files in os.walk(search_path):
            if is_absolute_excluded(root, absolute_excluded_dirs):
                dirs[:] = []
            dirs[:] = [d for d in dirs if not is_relative_excluded(d, dir_selector)]
            if '.git' in dirs:
                yield root


def is_absolute_excluded(absolute_directory, absolute_excluded_dirs):
    return absolute_directory in absolute_excluded_dirs


def is_relative_excluded(directory, relative_dir_selector):
    return directory in relative_dir_selector
