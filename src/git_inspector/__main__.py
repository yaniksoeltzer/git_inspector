#!/usr/bin/env python3
from .cli.continuous_git_reporter import ContinuousGitReporter
from .cli.exit_code import calculate_exit_code
from .cli.parse_arguments import parse_absolute_search_paths
from .find_git_repo import find_repos
from .inspect_repos import inspect_repos

absolute_search_paths = parse_absolute_search_paths()
git_repo_generator = find_repos(absolute_search_paths)

with ContinuousGitReporter() as reporter:
    inspect_repos(git_repo_generator, reporter)

exit_code = calculate_exit_code(reporter.all_reports)
exit(exit_code)
